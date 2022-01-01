---
aliases: [/note/recommender-libraries/]
categories: [情報推薦, 機械学習, プログラミング]
date: 2017-05-14
keywords: [推薦, ライブラリ, 実装, java, github, factorization, machines, mahout, librec, アルゴリズム]
lang: ja
recommendations: [/ja/note/hello-librec/, /ja/note/trends-in-real-world-recommender-systems-2017/,
  /ja/note/data-skeptic-recommender-systems/]
title: 推薦システムのためのOSSたち
---

**情報推薦＝機械学習** ではない。

もちろん機械学習アルゴリズムを使えば精度は高くなるかもしれないが、実際は推薦理由の説明が必要であったり、膨大なデータサイズや要求されるパフォーマンスに応えるために、『いかに機械学習をしない選択をするか』も重要になる。

さらに、[RecSys2016のLinkedInとQuoraのチュートリアルで語られたように](/note/recsys-2016/)、現実の推薦システムはヒューリスティクスに基づく単純な手法から深層学習まで、複数のものを組み合わせた **ハイブリッド** なものであることが多い。

- ヒューリスティクス/機械学習の混在したハイブリッドな推薦手法
- 適切な指標による精度の評価とモデルの改善
- サービスごとに異なる多様なデータフォーマットの扱い

ということを考えると、**推薦システム専用の実装** というものが必要になってくる。というわけで、推薦システム構築に使える/参考になるOSSをいくつか紹介する。

※チョイスは個人の経験に拠るものなのであしからず。この他にもGitHub上には無数にライブラリが存在するので、他にイケてるものがあればぜひ教えてください。

### MyMediaLite (C#)

- [公式サイト/ドキュメント](http://www.mymedialite.net/)
- [GitHubリポジトリ](https://github.com/zenogantner/MyMediaLite) 
- [論文](https://www.ismll.uni-hildesheim.de/pub/pdfs/Gantner_et_al2011_MyMediaLite.pdf)

実装が C# というのがネックだけど、推薦アルゴリズムのオープンソース実装で最も有名なのはおそらくこれ。2010年秋ごろから開発されていて、このあと挙げるような他のライブラリはみんな論文でMyMediaLiteを引用している。

対応しているアルゴリズムは協調フィルタリング、Matrix Factorization系が中心。Average Rating や Most Popular のような機械学習をしないベースライン手法も選べる。

他のライブラリの実装を見るとみんな似たり寄ったりな感じで、「このライブラリはMyMediaLiteチルドレンなんだなー」と気付くこともしばしば。

残念ながらここ数年は開発が滞り気味。

ちなみに論文は[Factorization Machines](http://www.algo.uni-konstanz.de/members/rendle/pdf/Rendle2010FM.pdf)の作者の[Rendle先生](https://scholar.google.com/citations?user=yR-ugIoAAAAJ)も共著者に入っている。

### LibRec (Java)

- [公式サイト/ドキュメント](https://www.librec.net/)
- [GitHubリポジトリ](https://github.com/guoguibing/librec)
- [論文](http://ceur-ws.org/Vol-1388/demo_paper1.pdf)

2014年から開発されているJavaの推薦アルゴリズム実装で、先日『[Java製の推薦システム用ライブラリ LibRec を動かしてみる](/note/hello-librec)』でも言及した。

僕が知る中で今最も盛んに開発が行われているライブラリで、つい最近 version 2.0 になってからはドキュメントとかもグッと良くなった。

MyMediaLiteを参考にしつつも、よく練られた設計や豊富な対応アルゴリズムによって独自の地位を築いている印象がある。

似たようなJava製ライブラリだと [PREA](http://prea.gatech.edu/) があるけど、こっちはもう全く更新されていない様子。

### LensKit (Java)

- [公式サイト/ドキュメント](http://lenskit.org/)
- [GitHubリポジトリ](https://github.com/lenskit/lenskit)
- [論文](http://files.grouplens.org/papers/p133-ekstrand.pdf)

2010年ごろから開発されているJava製のライブラリ。ミネソタ大学のチーム [GroupLens](https://grouplens.org/) に以前在籍していた[Michael Ekstrand先生](https://md.ekstrandom.net/)が中心になって開発している。これ自体が彼の博士研究の一貫でもあった。

アルゴリズムは協調フィルタリングとMatrix Factorizationがメインで極めてシンプル。

実装はともかく、論文に関しては一読の価値がある。（今やほとんど聞かないけど）Dependency Injection的な思想で、どのようにコンポーネントを切り分けて推薦ライブラリを実装するか、ということを解説している。このあたりはLibRecの設計に近い印象を受けた。

なお、Ekstrand先生には[Courseraの推薦システムのコース](/note/coursera-recommender-systems/)で会えます。

### Apache Mahout あるいは Hivemall (Java)

先に挙げたライブラリとは少し毛色が違うけど、Spark, Hadoop上で情報推薦を実現する際は [Apache Mahout](http://mahout.apache.org/) や [Hivemall](https://hivemall.incubator.apache.org/) が選択肢になる。

特にMahoutは推薦アルゴリズムの実装・利用に力を入れていて、『[Introduction to Cooccurrence Recommenders with Spark](http://mahout.apache.org/users/algorithms/intro-cooccurrence-spark.html)』などにそのことが細かく紹介されている。そういえば、[以前読んだフリー書籍の "Practical Machine Learning" ](/note/practical-machine-learning/)はMahoutを使った推薦システムの構築を激推しする内容だった。

あと、つい先日開催された **GPU Technology Conference Silicon Valley** のセッション "[Apache Mahout's new recommendation algorithm and using GPUs to speed model creation](https://gputechconf2017.smarteventscloud.com/connect/sessionDetail.ww?SESSION_ID=118703)" がすごく気になる。引き続きウォッチしていきたい。

一方、Hivemallはクエリを組み上げていくことで[協調フィルタリング](https://hivemall.incubator.apache.org/userguide/recommend/item_based_cf.html)、[Matrix Factorization](https://hivemall.incubator.apache.org/userguide/recommend/movielens_mf.html)、[Factorization Machines](https://hivemall.incubator.apache.org/userguide/recommend/movielens_fm.html)による推薦（予測）ができる。さらに、Factorization Machinesの拡張版で未だオープンソース実装が少ない[Field-aware Factorization Machines](https://www.csie.ntu.edu.tw/~r01922136/slides/ffm.pdf)までサポートされている点はポイントが高い。しかし、『クエリで行う情報推薦』が嬉しいかどうかはあなた次第。

なお、Hivemallでアイテム推薦については『[MacのローカルにHivemallを導入してアイテム推薦をするまで](/note/hivemall-on-mac/)』も参照されたい。

そうそう、Sparkで推薦といえば **MLlib** を忘れてはいけない。Pythonインタフェースがあるのも嬉しい。これについては [Collaborative Filtering - RDD-based API](https://spark.apache.org/docs/2.1.0/mllib-collaborative-filtering.html) から。

### fastFM (Python)

- [公式サイト/ドキュメント](http://ibayer.github.io/fastFM/)
- [GitHubリポジトリ](https://github.com/ibayer/fastFM)
- [論文](http://www.jmlr.org/papers/volume17/15-355/15-355.pdf)

Factorization Machinesに特化したPythonライブラリで、Rendle先生の昔の所属先の博士学生（？）のBayer氏が開発している。

scikit-learnに準ずるインタフェースを提供しつつ、[コア部分を完全に分離してC言語 (Cython) で実装している点](https://github.com/ibayer/fastFM-core)はお見事。

Factorization Machines自体は汎用的な予測モデルなので推薦限定というわけではないけれど、背景を鑑みると、やっぱりこのライブラリの主な用途は推薦になるんだと思う。

評価値予測なら二乗損失によるRegression、アイテム推薦ならBayesian Personalized Rankingによるランキング予測を行う。

実は、Python製のまともな推薦システム特化型ライブラリというのはかなりレアな存在。既存ライブラリの中で人気なのは [Surprise](http://surpriselib.com/) だろうか。（お恥ずかしながら僕は最近これを知りました。）

LL言語でみんな簡単に独自実装できるので、推薦システムという広い文脈では“全部入り”なライブラリの需要があまりないのかなぁ、と思う。推薦システム専用の実装が欲しければ自分で書けばいいじゃない、という空気感。

Pythonなら、fastFMのようにあるアルゴリズムや機能に特化したライブラリのほうが使ってもらえそう。

### まとめ

これまでに何度も実装を参考にしたり、頻繁に名前を聞いたようなOSSライブラリをまとめた。

Spark, Hadoopは例外だけど、紹介したライブラリの主なユースケースは、

- プロダクション用の推薦ロジックの研究開発段階で利用する
- 研究者が論文の評価実験のために使う

になるんだろうなぁと思ってる。でも実際のところ、どうなんだろう。「LibRec使って書いたコードを夜間バッチで走らせてます」みたいな事例があったら知りたいけど。

そして余談だけど、僕も修士研究のときに推薦アルゴリズムの実装をライブラリ化した：

- [Recommendation.jl: Building Recommender Systems in Julia](/note/recommendation-julia) [[GitHub](https://github.com/takuti/Recommendation.jl)]
- [FluRS: A Python Library for Online Item Recommendation](/note/flurs) [[GitHub](https://github.com/takuti/flurs/)]

しかしこれらはまだまだ実用レベルに達していないので、もっと頑張る必要がある。

推薦アルゴリズムの実装は、汎用的なものにしようとすると意外と考えることが多くて難しい。けどそれが楽しい :)