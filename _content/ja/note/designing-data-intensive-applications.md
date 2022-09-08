---
aliases: [/note/designing-data-intensive-applications/]
categories: [読書記録, コンピュータシステム]
date: 2017-12-30
images: [/images/ddia/poster.png]
lang: ja
title: '"Designing Data-Intensive Applications"は濃密すぎる一冊だったので2018年の自分にも読んでもらいたい'
lastmod: '2022-09-02'
keywords: [データ, data, ddia, dynamo, システム, 読ん, poster, データベース, 話題, 内容]
recommendations: [/ja/note/dynamo-style/, /ja/note/amazon-dynamo-paper/, /ja/note/data-stream-mining/]
---

分散システムに関する理解を整理するための一冊として素晴らしい、という声があり気になっていた "**[Designing Data-Intensive Applications](https://dataintensive.net/)**" を一通り読んだ：

https://twitter.com/frsyuki/status/846431130437890049

僕のような「用語としては知っている」程度の新人に「なぜそれが大切なのか」「なにが難しいのか」といったポイントを丁寧に説明してくれる、学びの多い充実の一冊だった。

冒頭では『早すぎる最適化（不要不急のスケーラブルなシステムの構築）は制約が増えてシステム設計が不自由になるだけなので無駄』という事実に触れ、適切なツールを選択することの重要性を説いている。本書が500項超を費やして伝えようとしているのは、そういったツールを取捨選択する際のエッセンスであり、具体的には、昨今の大規模なデータシステムを支える原理、モデル、ツール群の背景とその長所・短所である。

![ddia-poster](/images/ddia/poster.png)

※ [ddia-references/ddia-poster.jpg](https://github.com/ept/ddia-references/blob/master/ddia-poster.jpg) より

本書は大きくわけて "**Foundations of Data Systems**," "**Distributed Data**," "**Derived Data**" の3パートから構成される。

### Part I. Foundations of Data Systems

第1部では、データシステムの信頼性、スケーラビリティ、保全性を担保することの大切さと難しさを伝え（第1章）、特にストレージに焦点をあてて、データモデル（リレーショナルモデル vs ドキュメントモデル）と代表的なDB、クエリ言語を紹介していく（第2章）。このあたりの内容は "**[Seven Databases in Seven Weeks](https://pragprog.com/book/rwdata/seven-databases-in-seven-weeks)**" に通じるところもあった。データの一対多 (one-to-many) と多対多 (many-to-many) の関係が丁寧に比較されていて、リレーショナルデータベース、ドキュメント指向データベース、列指向データベースそれぞれの必要性や強み、弱みについて直感的な理解を与えてくれる。

いろいろなストレージの世界を俯瞰したら、次は実際にデータを保持・探索することを考える（第3章）。この章がまぁ素晴らしい。この本のインデックスの説明は、これまでに読んだいかなる解説よりも分かりすかったと言っても過言ではない。だって、*"the world's simplest databse"* を作って $\mathcal{O}(n)$ で検索するところから話が始まるんですよ？

```sh
#!/bin/bash

db_set() {
  echo "$1,$2" >> database
}

db_get() {
  grep "^$1," database | sed -e "s/^$1,//" | tail -n 1
}
```

```
$ db_set 123456 '{"name":"London","attractions":["Big Ben","London Eye"]}'
$ db_get 123456
{"name":"London","attractions":["Big Ben","London Eye"]}
```

ここから議論を初めて、B-tree や Bloom filter といった具体的なデータ構造、アルゴリズムに言及していく。

データの保持に関しては、高可用性やレイテンシがキモでサービスの核を担う OLTP (On-line transaction processing) と、ETLや分析用途で利用される集約操作が主の OLAP (On-line analytical processing; データウェアハウス) の比較が易しい。

そして第1部を締めくくるのは、保持され、やり取りされるデータの“実体”、すなわちデータのシリアライズ（エンコーディング）とメッセージパッシングに関する話題（第4章）。[MessagePack](https://msgpack.org/index.html)がシリアライゼーションフォーマットの1つとしてしっかり取り上げているのをみてニヤニヤしたり、[gRPC](https://grpc.io/)への言及から今っぽい流れを感じたりできて楽しい。

データシステムの構築に際して、第1章で挙げたデータシステムの信頼性、スケーラビリティ、保全性の点で、それぞれの選択肢がどのように優れて（劣って）いて、各々の使いドコロはどこなのか。本書では、最初から最後まで一貫してこのような流れで話が進む。

### Part II. Distributed Data

第2部の話題はデータの分散処理。個人的には、ここが一番「用語としては知っているけど、理解が及んでいない」というポイントだったので、舐めるように読んだ。

特に、Replication, Partitioning, Consistent Hashing などについては、並行して読んでいたAmazonのDynamoDBの原論文の内容と絡めて別の記事でまとめた：

- [AmazonのDynamoDB論文を眺めた](/note/amazon-dynamo-paper)
- ["Dynamo-style" に学ぶ Replication, Partitioning, Consistent Hashing の気持ち](/note/dynamo-style)

このような話題に加えて、（まだ十分に咀嚼できていないけれど）トランザクション、Consensusアルゴリズム、Linearizability などを解説しているのがこの第2部。『分散システムの難しさ（＝面白さ！）』がギュッと凝縮されているところだと言えよう。

### Part III. Derived Data

第3部では、ここまでの内容を総合してデータシステムを構築することと、その際のアーキテクチャについて考える。

バッチ処理 (MapReduce) と、ストリーム処理（イベント処理）の2つの切り口から、HDFSやメッセージブローカについてかなり踏み込んだところまで解説を試みている印象があった。

ここまで打ってきた布石の上に成り立つ重厚なパートであることは確かなのだけど、エッセンスを上手く伝えてくれた第1部、第2部と比較すると、中途半端に踏み込みすぎている感が否めなかった。これなら他の文献をあたるかな、という気分。

ちなみに、ストリーム処理の“気持ち”は以前まとめたことがある：

- [ストリームデータ解析の世界](/note/data-stream-mining)

このときの知識と、その実践の間にあるエンジニアリング的な部分とのギャップを埋めるのがココ（第11章）の内容だろう。

そして最終章 "**The Future of Data Systems**" ではデータシステムの一部としての機械学習に触れ、なかなかエモい話が展開されていた：

> *Data and models should be our tools, not our masters.*

（思わず赤線でマークしてしまった。）

### 全体として

緻密なサーベイと丁寧な構成の上に成り立っている一冊であることが手に取るように分かり、安心して読み進められる。

なにより、この本はリファレンスがすごい。ブログ記事からGitHubリポジトリ、論文まで、大量の外部ソースを逐一参照しているので説得力がある。さすが、[著者が現役の研究者](http://martin.kleppmann.com/)だけのことはある。すべての参考文献は [github.com/ept/ddia-references](https://github.com/ept/ddia-references) にもまとまっている。

そして、進化の早い分野なので "At the time of writing, ..." といった記述が多々あったのも印象的。データシステムの“イマ”のスナップショットとして、素直にワクワクできる一冊でした。

あと余談ですが、同時期にこの本を読んでいたエンジニアの友人が2〜3人いて、話題の一冊という感じでした。それぞれ会社も役割も違うのに、飲んだときにこの本の内容についてイロイロ話すことができた、というのは嬉しい体験だった。それくらい、広く程よく書かれた、次の一歩につながる有意義な本だったということ。

### 2018年、もう一度読みたい

2017年ももう終わりです。[Data Science Engineerというポジションで働き始めて](/note/master-graduate/)9ヶ月、良かったこと、悪かったこと、達成感、焦燥感いろいろありましたが、この本の内容を『自分ごと』として読めるようになったことが何よりの収穫であり、喜びでもあります。

学生のときはスケーラビリティに言及した本や論文を読んでも、どこか他の世界の話のように感じていたのです。もちろん、それが大切だということは頭ではわかっているのだけど。

2018年は、こうして現実感をもって向き合うことが出来るようになった文献やコードをさらに深掘りしてゆきましょう。

そのために、一度では消化しきれないほどの充実っぷりだった本書ももう一度（二度、三度）読んで、[世界地図](https://www.oreilly.com/ideas/drawing-a-map-of-distributed-data-systems)を頭に焼き付けたいですね。

おつかれさまでした。