---
categories: [コンピュータシステム, データサイエンス, 機械学習]
date: 2021-12-19
images: []
lang: ja
title: AWSのマネージドAirflow "MWAA" 所感
lastmod: '2022-09-02'
keywords: [airflow, aws, mwaa, オペレーター, apache, emr, cloudwatch, ワークフロー, モニタリング, ロギング]
recommendations: [/ja/note/the-amazon-way-on-iot/, /ja/note/why-spark/, /ja/note/amazon-dynamo-paper/]
---

[Google Cloud Composer](https://cloud.google.com/composer/docs/concepts/overview)のリリース（2018年7月19日GA）から遅れること2年数ヶ月、AWSは2020年11月24日に **Managed Workflows for Apache Airflow** (**MWAA**) をリリースした。

- [Introducing Amazon Managed Workflows for Apache Airflow (MWAA)](https://aws.amazon.com/blogs/aws/introducing-amazon-managed-workflows-for-apache-airflow-mwaa/)

それから1年、遅ればせながら自分でも軽く試してみた。AWSコンソールからAirflow UIに飛ぶのに違和感を覚えつつも[^1]、種々のAWSサービスとの連携を考えると「むしろなんで今まで無かったんだろう」という気さえする。

### 概要

公式のデモ動画が分かりやすいので、まずはそれを見てみよう。

<span class="iframe-container">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/ZET50M20hkU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</span>

ポイントは次の通り。

- DAGファイル（Pythonコード）は専用のS3バケットに置く
- OSSのAirflowに完全準拠
- （事前に設定した上限値までの）Workerの自動スケール
- KMS管理下の鍵によるデータ暗号化
- CloudWatch連携によるログ・メトリクスの一元化
- 各タスクの実行に際して用いられるIAM Roleを指定

もちろん設定・デプロイはCDK (CloudFormation) 経由で行うこともできて、サンプルは [aws-samples/amazon-mwaa-examples](https://github.com/aws-samples/amazon-mwaa-examples) などにある。ユースケースとしては、たとえばS3のファイル操作はAirflowの `S3KeySensor` と `PythonOperator` の組み合わせによってフレキシブルに実現できて、その他各種AWSサービス用のオペレーターも豊富。

### AirflowのAWSオペレーターたち

Airflow本体のコードベースに内包されていて、MWAAリリース以前から開発の続く [`apache-airflow-providers-amazon`](https://github.com/apache/airflow/tree/main/airflow/providers/amazon/aws/operators) が各種オペレーターを提供している。ETL + MLに必要であろう主要サービスは一通りカバーされている印象。

MWAAに限らない一般的な話になってしまうので深入りはしないが、たとえば前処理から最終的な予測結果生成までのフローを組むとすれば次のようなイメージ。

```
[prep_data_1, prep_data_2, ...] >> build_features >> predict >> post_process >> publish
```

- 特徴量エンジニアリングはSparkのDataFrame処理で実現したいので、EMRオペレーターを用いる。[ドキュメント](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/operators/emr.html)にも記載されているように、ここは単一オペレーターではなくて、`EmrCreateJobFlowOperator >> EmrAddStepsOperator >> EmrStepSensor >> EmrTerminateJobFlowOperator` のチェインから構成される。
- 予測は `SageMakerTransformOperator` から、学習済みSageMakerモデルによるBatch Transformジョブで行う。
- 再びSpark on EMRで、予測結果の後処理。具体例として、『[後処理による人気アイテムの“格下げ”で確保する推薦多様性](/ja/note/reranking-for-popularity-bias/)』で書いた後処理 `rerank` を差し込むならココだろう。多様性の指標をCloudWatchに書き出してモニタリングするのもアリかもしれない。多様性がある閾値を下回ったらアラートあるいはタスク失敗、とか。
- そして途中/最終結果の吐き出しはデータフォーマットや保存先に応じて適当なオペレーターを選ぶ。

あるいは、データのマイグレーション用途であればRedshift, Glue, Database Migration Service (DMS) オペレーターあたりが活躍しそうだ。ETLの"Transform"に際して必要な単純なバッチ処理には `ECSOperator` が使えるだろうか。

### なぜMWAAか

ハマりどころとしては、MWAAそれ自体よりも、各オペレータが扱うAWSサービスたちが問題になることの方が多そうだ。個人的には、この点がMWAAを使うことの最大の理由であるように感じた。

たとえばパーミッション周りは、状況に応じて適切にKMSキーやIAM role/policyを設定しないとワークフローが最後まで走りきらず、何かと苦戦しそうな雰囲気。ここで仮に自前でAirflow環境を構築・運用していたとすれば、問題がAirflow環境それ自体に起因するものか、Airflow <> AWS間でおかしなことが起こっているのか、それともAWS上の設定に限った話なのかを切り分けるところから始めなければならない。

一方でワークフロー実装に際しては、こまめにイロイロといじって試行錯誤を繰り返したいこともまた事実。したがって、Airflow環境それ自体を疑う状況というのは可能な限り避けたいものである[^2]。

AWS Podcastの8月の放送回ではそのあたりの動機、「なぜAWSがマネージドAirflowを作ったのか」をプロダクトマネージャーから直接聞くことができる。

<iframe allow="autoplay *; encrypted-media *; fullscreen *" frameborder="0" height="175" style="width:100%;max-width:660px;overflow:hidden;background:transparent;" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-top-navigation-by-user-activation" src="https://embed.podcasts.apple.com/us/podcast/464-diving-deep-into-amazon-mwaa/id1122785133?i=1000531401750"></iframe>

当然といえば当然だが、冒頭の言及からかなり機械学習ユースケースを意識している様子が伺える。[公式アナウンス記事](https://aws.amazon.com/jp/blogs/aws/introducing-amazon-managed-workflows-for-apache-airflow-mwaa/)のサンプルデータもMovieLensで“匂わせ”感がある。

とはいえ主要な動機はやはり、ネットワーキング（サービス間連携）、スケーリング、モニタリング、ロギングにおける設定・オペレーションの簡素化にある。タスクワーカーひとつひとつがVPC上のプライベートサブネットに接続されたFargateコンテナであり、これによってユーザは先に挙げたような種々の煩わしさから解放される。

![mwaa-architecture](/images/amazon-mwaa/mwaa-architecture.png)

※ 画像ソース：[What Is Amazon Managed Workflows for Apache Airflow (MWAA)?](https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html)

「多様性の指標をCloudWatchに書き出してモニタリング」と先述したように、個人的にはモニタリング・ロギングに際して享受できるメリットが特に大きいと感じる。

ワークフローとは、処理を自動化してラクをするための道具であると同時に、異常をいち早く検知するための“仕組み”でもある。そしてそれは、社内SREやインフラエンジニアのためである以前に、エンドユーザの体験を高いレベルで維持し続けるために欠かせない要素となる。

その点において、Airflow単体のロギング機構は必ずしも有用であるとは言い難いし、インフラ稼働状況・タスク出力それぞれの各種メトリクスを可視化する際のベストプラクティスやツール選択は議論の分かれるところ。ゆえに、ここで「とりあえずCloudWatch」として話を前に進められることは、かなりのアドバンテージであるように思う。

以上も踏まえて、第一歩としてローカルで試すための公式Dockerイメージは [aws/aws-mwaa-local-runner](https://github.com/aws/aws-mwaa-local-runner) より入手可能。ただし `apache-airflow-providers-amazon==1.3.0` とやたら古いので注意（執筆時点での最新版は `2.5.0`）。EMRクラスター依存のタスクを1時間以上走らせたらboto3が `ExpiredTokenException` を吐いて、「そんなギャグみたいな死に方する？」と思っていたら、最新版では既に解決している話 ([apache/airflow #16771](https://github.com/apache/airflow/pull/16771)) だったりした。

というわけで、MWAAの概要と雑感でした。試すのが遅すぎた感は否めないが、リリースから1年経った今、果たしてどれだけ使われているのだろうか。

そして、そもそもデータエンジニアリングの現場では既にAirflowがワークフローエンジンのデファクトという理解で良いのだろうか。Luigiは元気だろうか・・・。そんなことを考えていたら、GitHubスター数に基づくグラフと考察を見かけたので貼っておく。

- [Airflow vs. Luigi vs. Argo vs. MLFlow vs. KubeFlow: Choosing a task orchestration tool](https://www.datarevenue.com/en-blog/airflow-vs-luigi-vs-argo-vs-mlflow-vs-kubeflow)

Luigi...

[^1]: EMRでHadoop, Tez, SparkのUIに飛ぶのは「まぁそういうもの」という認識が強いが、Airflowの比較的フレッシュなUIは「エンタープライズ感」があまり無いので不思議な感覚に陥る。私だけでしょうか。

[^2]: もちろん、究極的には常にあらゆる可能性を疑わなければならないわけだが。“手が届く範囲においては”（オンプレを含む）自前での環境構築も必ずしも悪ではない。