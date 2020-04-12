---
date: 2017-12-09
lang: ja
recommendations: [/ja/note/dynamo-style/, /ja/note/the-amazon-way-on-iot/, /ja/note/designing-data-intensive-applications/]
title: AmazonのDynamoDB論文を眺めた
---

"[Seven Databases in Seven Weeks](https://pragprog.com/book/rwdata/seven-databases-in-seven-weeks)" や "[Designing Data-Intensive Applications](https://dataintensive.net/)" でも度々参考文献に挙がっていたので、AmazonのDynamoDB論文を眺めて思いを馳せていた：

- **[Dynamo: Amazon's Highly Available Key-Value Store](https://dl.acm.org/citation.cfm?id=1294281)** (SOSP 2007)

ここでは特に2章・バックグラウンドの内容を整理しつつ、AmazonがDynamoDBに込めた想いに触れてみる。拙記事『[The Amazon Way on IoT - Amazonのビジネスから学ぶ、10の原則](/note/the-amazon-way-on-iot/)』でも紹介した、Amazonの "Customer Obsession"（お客様第一）という理念を踏まえて読むと大変味わい深くてよろしい。

### 教訓: システムの Reliability と Scalability は、いかにアプリケーションの“状態”を管理するかに依る

“状態”とは、Amazonの『ショッピングカートの中身』のようなものを指し、『カートへの商品の追加・削除』がその“管理”に相当する。このように、何らかのビジネスロジックに紐付くサービスは往々にしてステートフルとなり、その扱い方がサービスの信頼性のキモとなる[^1]。

そして、そのような“状態”を複雑なクエリで問い合わせるというケースはあまりなく、主キーで一意に定まるものをピックアップすることのほうが多いので、従来行われてきたRDBによる管理は過度な複雑化といえる。

そこでAmazonは **Dynamo** というKVSを開発し、scalability と availability の両立を、2つの既存手法の組み合わせによって実現した：

1. データは **consistent hashing** によってパーティショニング、レプリケーション
2. 一貫性は **object versioning** の下で“ゆるく”担保

この論文は、既存の技術の組み合わせでいかにプロダクションレベルのシステムを作っていくか、という点でひとつの例を示すもの。

### RDBではなくKVS

先述の通り、リレーショナルスキーマを要するデータ横断的な処理は状態の保持には不要だと経験的にわかっている。

なので、Dynamoはデータをblobのようなバイナリオブジェクト (たいてい1MB以下) で保持し、ユニークなキーによって一意に取得可能にした。

### Eventual Consistencyでよい

ACID (Atomicity, Consistency, Isolation, Durability) を満足させると可用性が低下することは経験的にわかっているので、Dynamoは可用性が向上するなら一貫性 ("C"; Consistency) を諦めても構わないという姿勢をとる。

そう、Eventual Consistency である。

Dynamoは高可用性を担保するために [optimistic replication](https://en.wikipedia.org/wiki/Optimistic_replication) (i.e., lazy replication) を採用しているため、処理のある時点においては容易に一貫性が壊れる。

だが、競合解決処理を経ることで、いずれ (eventually) レプリカは何らかの状態に落ち着く (consistent)。

[Data-Intensive (ry](https://dataintensive.net/) でも書かれいていたけど、昨今ではACIDを満足しないシステムを **BASE** (Basically Available, Soft state, and Eventual consistency) と呼ぶ風潮もあり、このような考え方は広く受け入れられている。

ところで、『いずれ』とはいつなのか。どのタイミングで競合を解決するのか。

従来のデータストアは書き込み時に競合の解決を行い、読み込みは極力シンプルに、という考えの下に成り立っていた。しかしこれは、場合によっては "rejectされるwrite" が存在するということ。

ユーザにとって "write reject" は「クリックしたのに反映されない」的なシナリオであり、これはユーザ体験の低下に直結する。なのでDynamoは "always writable" を重視して、コンフリクト解決はread時に考え、writeでは行わない。

少しくらいネットワークが途切れても、サーバが死んでても、ユーザはショッピングカートのアイテム (state) の変更 (write) が確実にできるように、というAmazonの強い想いがある。

さらに、もうひとつ Eventual Consistency に際して考えるべきは『だれが（どこで）コンフリクトを解決するか』という点。

データストア側で解決を試みる場合、我々は "last write wins" という単純な手段しか持ち合わせていない。

しかし適切な競合解決プロセスというものはアプリケーション依存であり、たとえばショッピングカートの中身がコンフリクトしたら、両者をマージして1つのカートにして返すという明確なゴールがある。だから、Amazonはアプリケーション（クライアント）側での競合解決を重視する[^5]。

### SLA重要

Amazonのようなdecentrizedなサービスでは1リクエストに対して動くサービスが複数あり、相互依存が激しい。そんな環境下で各コンポーネントのchain時のパフォーマンス要求を明確にするために、SLA  (Service Level Agreement) は特に重視している。

具体的には、Amazonには99.9パーセンタイルの値で処理効率を測るという厳密なSLAがある[^2]。

サービスを提供する側 (Amazon) が本当に大切にしたいヘビーユーザはたくさんログを持っていて、往々にして一処理あたりの時間も長くなりがちだ。でもmean, median, expected varianceのような“平均値”に基づくSLAを設定してしまうと、この少数の大切なお客さんに対するパフォーマンスが多少悪くても「SLAを満たしている」となりかねない。

Amazonは“大多数のお客さん”ではなく、“お客さん全員”が満足しうるサービスを目指したい。ゆえに、平均値で測るSLAでは不十分なのだ[^3]。

一般に、サービス内のビジネスロジック（Amazonの“購買”のような）が比較的軽量なとき、ストレージはシステムのSLAを満足するために特に重要な要素だと言える。なのでDynamoは処理効率、コスト、可用性、耐障害性といったトレードオフをユースケースに応じて柔軟に選択（調整）できるように設計する。

### Dynamo: お客様第一で設計されたストレージ

この他、Dynamoの設定に際して：

- **Incremental scalability**
  - システムオペレータとシステム自体への影響を最小にしつつ、ノード単位でスケールアウトできる。
- **Symmetry**
  - Dynamoのノードはみんな平等で、どれかが特別な役割、ということはない。
  - 経験的に、こうするとプロビジョニングやメンテナンスが単純化されてよい。
- **Decentralization**
  - P2P的システムにする。Symmetryと同じ気持ち。
  - centralizedなシステムは全体的なシステムダウンを招く。
- **Heterogeneity**
  - 各ノードがキャパに対してどの程度の仕事を割り振られているか、システムはそのバランスを常に考慮する。
  - そうすれば、新しい大きなキャパのノードを追加したときに、全ノードの設定をアップグレードする必要がなくなる。

といったことも考慮された。

いずれにせよ、トレードオフのひとつひとつをcustomer obsession的な視点で選択し、合理的にシステムを設計していく姿勢が見て取れる濃厚な "Background" の章で、個人的にはここがこの論文の一番の見どころだと思った。もちろん後半の partitioning, replication, object versioning の実装に関する具体的な言及や、実験とそこから得た教訓の話が主役ではあるのだけど。

体裁の整った本の記述からは得られない、広く使われるシステムの根底にあるアイディアに触れられるのはよいですね。なお、僕は若者なので、この論文が書かれた当時それがどれだけ革新的なことだったのかを測るものさしは持ち合わせていない。

[^1]: 一方、ステートレスなサービスとは、他のサービスたちのデータを集約するような内部コンポーネントなどを指す。
[^2]: もちろん具体的なパーセンタイルの設定はコストとのトレードオフ。
[^3]: これはAmazonの話。会社のゴール次第なので「平均値で測れば十分」という場合もありうる。
[^5]: 論文「まぁ、世の開発者たちは状況に応じたコンフリクト時の例外処理を考えるのが面倒なので "last write wins" だけになりがちだけど…。」