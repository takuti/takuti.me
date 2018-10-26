---
date: 2016-10-04
lang: ja
recommendations: [/note/master-graduate/, /note/hivemall-events-2018-autumn/, /note/yahoo-egads/]
title: 'Treasure Dataインターンにみる機械学習のリアル #td_intern'
---

8月1日から9月30日まで、大学院の同期で小学生時代は落ち着きがなかった [@ganmacs](https://twitter.com/ganmacs) と、小学校の給食ではソフト麺が出なかった [@amaya382](https://twitter.com/amaya382) と一緒に **Treasure Data** (TD) **Summer Internship** に参加した。

- [Treasure Data インターンで最高の夏過ごしてきた  #td_intern - memo-mode](http://ganmacs.hatenablog.com/entry/2016/10/07/094427)
- [トレジャーデータでインターンしてた話 #td_intern - 水底](http://amaya382.hatenablog.jp/entry/2016/10/01/210752)

[インターンの途中で1週間アメリカへ行ってしまう](http://takuti.me/note/recsys-2016/)という事情を酌んだ上で採用していただき、限られた期間で物凄く適切な課題設定とメンタリングを行なってくださった[@myui](https://twitter.com/myui)さんには頭が上がらない。本当にありがとうございました。

TDインターン全体としての見どころは、

- 全方位ウルトラエンジニアで気を抜くと死ぬ環境
- 丸の内の一食1000円オーバーの飲食店事情
- ラウンジの炭酸強めでおいしい炭酸水

にあったと思う。うん。

※いろいろ書きますが、内容は全て僕個人の考えで、TDや[@myui](https://twitter.com/myui)さんの意見を代表するものではありません。念のため。

### Treasure Data Summer Internship 2016

6月ごろから募集が行われていて、選考やインターン中の雰囲気は基本的に以下の記事に書かれている通りだった。

- [Treasure Data Summer Intern 2015 - myui&#39;s memo](http://myui.hateblo.jp/entry/2015/10/06/Treasure_Data_Summer_Intern_2015)
- [Treasure Data 2015サマーインターンに参加した](http://qiita.com/NeokiStones/items/dde03c52623d4e657f46)

僕のインターンを通してのテーマは ***Real-world Machine Learning*** だったように思う。具体的にやったことを列挙すると以下のような感じで、1つの機能をじっくり腰を据えて実装する、というよりは様々な側面から現場での機械学習に触れるような内容だった。

- [Hivemall](https://github.com/myui/hivemall)へのユーザ定義関数 (UDF) 実装
	- ランキング問題用の評価関数 6種類 [#326](https://github.com/myui/hivemall/pull/326)
	- 異常検知のフレームワーク 2種類
		- **ChangeFinder** [#329](https://github.com/myui/hivemall/pull/329), [#333](https://github.com/myui/hivemall/pull/333) （春のインターン生の実装の一部として）
		- **Singular Spectrum Transformation** [#356](https://github.com/myui/hivemall/pull/356)
- TD社内のDatadogメトリクスからの異常検知
	- [takuti/datadog-anomaly-detector](https://github.com/takuti/datadog-anomaly-detector)
- チュートリアル記事「**Random Forestを用いたTreasure Data (Hivemall) 上でのサービス解約予測**」の執筆
	- [下書き](https://gist.github.com/takuti/08f06176bff97f8b957d9b52537b1aa4)
- 機械学習絡みのセールス/コンサル目的のミーティングへの同席

### HivemallへのUDF実装

HiveのUDFを実装するのは最初"お作法"的なものがよくわからず戸惑ったけど、既存の実装や[プログラミングHive](https://www.oreilly.co.jp/books/9784873116174/)を参考にしつつ何とか進めた。少しだけお近づきになれた気がする。

ランキング問題用の評価関数というのは地味だけど、僕の興味と密接に関係していて、応用上重要な役割を果たす関数でもあるのでウキウキしながら実装した。（推薦とは多くの場合において本質的にはランキング問題となる。）理解不足だったり、そもそも間違えて解釈していたところが明らかになったのも良かった。（参考：**[Metric Learning to Rank](https://bmcfee.github.io/papers/mlr.pdf)**）

異常検知に関しては、線形計算が好物なので **Singular Spectrum Transformation** を論文読みながら実装してるときが一番ノリノリだった。**ChangeFinder** はハイパーパラメータの闇が深いので厳しい。

![hivemall](/images/td/hivemall-icon.png)
▲ キメラ感の無いクールなHivemallロゴ

Hivemallが実現した[クエリで記述するプログラミング不要の機械学習](http://www.slideshare.net/myui/hivemall-hadoop-summit-2014-san-jose#7)というパラダイムを[@myui](https://twitter.com/myui)さんは **ポストMahout** と位置づけている。しかし現実には「プログラミングのほうが楽だ」という意見もあるだろうし、最適解はデータの規模や解析基盤の構成、データサイエンティストの技量に応じて異なって然るべきだ。

インターン参加中に[HivemallのApache Incubatorプロジェクト入り](http://itpro.nikkeibp.co.jp/atcl/column/15/061500148/100300084/)が決定し、今後より多くの機能がサポートされていくことと思うが、機械学習戦国時代に生きる僕たちは常に **ポストHivemall** の可能性も見据える必要があるのだと思う。

実際にHivemallを触りながら、漠然とそんなことを考えていた。

### TD社内のDatadogメトリクスからの異常検知

Datadogは[公式でメトリックに対する外れ値スコア計算をサポート](https://www.datadoghq.com/blog/introducing-outlier-detection-in-datadog/)していて、メトリックごとのスコアに閾値を設けてアラートを設定すれば、異常検知っぽいことができる。しかしDatadogのアラートは *AND* や *OR* のような演算を組み合わせた複雑な条件設定には対応していないので、大量のメトリクスを画面いっぱいに表示して監視するようなシーンで、複数メトリクスの状態から総合的に判断される異常みたいなものが定義できない。

というわけでDatadogの外側にその機構を作ってみましょう、という話になり、インターンを通して以下のようなシステムをEC2上に作って評価・改善を行なった。

![dd-anomaly](/images/td/dd-anomaly.png)

1. DatadogからAPI経由で指定メトリクスの値を取ってきて、
2. 複雑な入力にも対応できる異常検知フレームワーク **ChangeFinder** を実装したPythonデーモンが異常スコアを計算して、
3. スコアをくっつけたレコードをFluentに投げて、
4. Fluentは
	- 異常スコアのモニタリング用にそれをDatadogにPOSTしつつ
	- 複数メトリクスに対する複雑な条件によるフィルタリング（検知）のためにComplex Event Processing (CEP) エンジンNorikraにも渡して、
5. Norikra側で引っかかった異常はFluent経由でSlackに通知される。

TDインターンは全てガチなので、当然これも「インターンの課題として作って終わり」的なモノではなくて、日常的なメトリクス監視業務の一部として実際に使うことを想定して作った。けれど、話はそんなに簡単ではなかった。

まずDatadog APIに依存している時点でメトリクス収集の頻度には制限があるし、**ChangeFinder** は先述の通りハイパーパラメータの闇が深すぎて正直使いづらすぎる。そしてNorikra、これは良し悪し以前の議論の余地が多分に残されている。

https://twitter.com/takuti/status/762199014863278080

https://twitter.com/frsyuki/status/781722538887958528

https://twitter.com/tagomoris/status/781722722233561088

というわけで、経験値として得たものは多かったけど、やり残したことや反省点も多くあるので、これに関してはもう少し使いやすい形まで仕上げて後日改めてブログ記事にでもしたい。

重要なのは、手法がどれほど理論的に素晴らしいものであっても、実際にはそれ以外の部分に様々な困難が存在するということ。そしてそれらに立ち向かうことがいかに難しいことであるか。

### チュートリアル記事の執筆

TDは「エンジニアがすごい会社」というイメージが強すぎて実際どんなビジネスをしているのか正直謎だったけど、[Data Management Platform (DMP) を提供する会社](https://www.treasuredata.com/jp/service)ですよ、みなさん。ゆえに、お客様はデータに関する様々な課題を抱えていて、それに対してDMPの活用方法・事例を示すことが我々の重要な役割のひとつ。

今回はその一例として、[pandas-td](https://github.com/treasure-data/pandas-td) も利用しつつTD上でのサービス解約予測を行なった。データは[これ](http://www.dataminingconsultant.com/DKD.htm)で、3333サンプルしかないのでscikit-learnとか使ったほうが全然楽なのだけど、そこはご愛嬌。

機械学習・データサイエンスの文脈で第三者に手法の"良さ"を正しく伝えるためには、まず僕らが数式の気持ちになってあげることが大切だと思う。記事やスライドに数式をそのまま書いたら負け、でもモデルの裏側にある概念は正しく伝える…まぁこれが大変なのだけれども…。

### セールス/コンサル目的のミーティングへの同席

こればかりは残念ながら詳細を書くことができないが、TDはセールスの会社（[CTO談](http://tenshoku.mynavi.jp/it-engineer/knowhow/naoya_sushi/12)）であり、その一端を感じることのできる素晴らしい機会だった。

「技術はユーザの存在があってこそ」という気持ちがずっとあって、これは機械学習も例外ではない。どのアルゴリズムを使うか？目的変数はなにか？ハイパーパラメータはどうするか？特徴ベクトルは？といったことは全てデータや目的、システム上の制約などに依存する。そしてユーザありきの機械学習では大抵の場合、目的を達成するためにヒューリスティクスが多分に投入される。そのあたり、バランスがとても重要なのだ。数学的に面白い方向性や、少し特殊な問題設定の大喜利的な提案、計算リソースにモノを言わせる手法はたくさんあるけれど、その点なんか違うよね〜と感じてしまう。むつかしい。

そういった世界で"ちょうどいい"解決策を個々のユーザに示すためには、やっぱりコミュニケーションとか、経験に基づく勘とかが大事で、ミーティングへの同席はそれを再認識する良いきっかけになった。

### まとめ

良くも悪くも、現実の機械学習は多様なスキルの組み合わせの上に成り立っている。TDインターンを通してその楽しさと難しさを痛感した。

2ヶ月はあっという間だったけれど、楽しくて優秀な同期2人と、とても尊敬できるメンター、そして凄い（それ以外のうまい表現が見つからない）社員のみなさんのおかげで、濃密な時間を過ごすことができた。本当にありがとうございました。

M2の夏休みをフルタイムインターンに捧げるというのは一見リスキーだけど、まぁ毎週ジムにいったり、途中で国際会議ショートペーパー1本書いて投稿するくらいの余裕はあったので、来年も募集があったらみなさん積極的に応募するとよいです。特に機械学習系のみなさん、研究所やデータサイエンティスト的なポジションのインターンも良いけれど、TDもかなり良いですよ。論文のIntroductionの説得力が増すと思います。

最後に僕の最終発表のスライドを貼っておきます。何か変なことを言っていたり、俺ならこうする！みたいな話があったらぜひお聞かせください。

<script async class="speakerdeck-embed" data-id="60d7198f9d5048b6bb1187830c0357b2" data-ratio="1.33333333333333" src="//speakerdeck.com/assets/embed.js"></script>