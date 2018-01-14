---
date: 2017-10-28
lang: ja
recommendations: [/note/why-spark/, /note/the-amazon-way-on-iot/, /note/trends-in-real-world-recommender-systems-2017/]
title: Courseraの"Functional Programming in Scala Specialization"を修了した
---

ここ1年くらい暇を見つけてちまちまと遊んでいたCourseraの "**[Functional Programming in Scala Specialization](https://www.coursera.org/specializations/scala)**" という一連のプログラムを修了した。

4つのコースから構成されていて、（修了証は出ないけど）課題を含めてすべて無料で受講できた。課題はスケルトンコードとデータが与えられて、指定されたメソッドを実装する、というよくある形式。

1. **Functional Programming Principles in Scala**
  - 関数型プログラミングの基礎
  - パターンマッチとか高階関数とかImmutableなデータ構造の話とか
2. **Functional Program Design in Scala**
  - 発展的な関数型プログラミングの概念いろいろ
  - モナモナしたり、遅延評価したり
3. **Parallel Programming**
  - タスク並列化とデータ並列化
  - `.par` を付けるとできる、Scala の並列コレクションに対する操作いろいろ
4. **Big Data Analysis with Scala and Spark**
  - Sparkを使おう
  - `RDD`, `Dataset`, `DataFrame` それぞれの操作

**Functional Programming Principles in Scala** では、`var`（と `val` ）を絶対に使わないという強い意志を持って、再帰を駆使してコードを書く。~~普段ノリでScalaを書いていると気がついたらJavaになっているが、~~このコースが最初にあったおかげで、始終冷静にScalaが書けた気がする。ハマりどころは特に無いけど、Scalaじゃなくても良いよね感がすごいので飽きる。

**Functional Program Design in Scala** は講義が苦痛だが、どの資料をあたってもモナドとは常にそういうものである。諦めよう。課題では `Stream` や [ScalaCheck](https://github.com/rickynils/scalacheck) が出てくる。遅延評価の話と `Stream` の導入はわかりやすくて良かった。

そして **Parallel Programming**。ここからがこのプログラムのメイン。まずは Parallel Programming（並列プログラミング）と Concurrent Programming（並行プログラミング）の違いから講義が始まる。受講当時ちょうど [The Art of Concurrency](http://shop.oreilly.com/product/9780596521547.do) を読んでいたこともあって、この点は以前記事にもまとめた：

- **[Parallel Programming vs. Concurrent Programming](/note/parallel-vs-concurrent/)**

call-by-nameで引数を評価することの重要性や、再帰的な処理・コレクション操作の並列化など、これまでの『関数型言語としてのScala』の講義を踏まえて教えてくれたのが印象的で、「あーここでその話が出てくるのかー」という体験が多くて良かった。

課題では [k-means](https://en.wikipedia.org/wiki/K-means_clustering) を実装したのが特に楽しかった。馴染みのある実用的なアルゴリズムが動くと嬉しくなる。

最後のコース **Big Data Analysis with Scala and Spark** では、その名の通りSparkを学ぶ。Stack Overflowなどの実データ（？）を対象に課題に取り組めるのも嬉しい。

このコースは『なぜSparkか』というところから話が始まる。わかりやすくて納得感があったので、記事でもまとめた：

- **[なぜSparkか](/note/why-spark/)**

そして `RDD` の解説が始まる。キャッシュの重要性を口酸っぱく言われるので、これについてもブログでまとめておいた：

- **[Comparison of Running Time of Cached/Uncached Spark RDD](/note/spark-rdd-cached-vs-uncached/)**

課題になると、**Parallel Programming** で実装した k-means を今度はSpark RDDを使って実装する。これがかなりハマって、しばらく放置していたら修了まで随分時間がかかってしまった…。

そんな「RDDを効率的・効果的に扱うのは大変だよね？」という文脈から、[Catalyst](https://databricks.com/blog/2015/04/13/deep-dive-into-spark-sqls-catalyst-optimizer.html)による最適化の恩恵を受けるべく `DataFrame` が紹介される。そして最後には `RDD` と `DataFrame` のハイブリッド的存在として `Dataset` が登場して完結。

### まとめ

『関数型言語としてのScala』から『Sparkによるビックデータ解析』までを学べる、楽しいプログラムだった。おすすめ。

もっと効率よく学べる資料も世の中にたくさんあるんだろうけど、課題がかなりよくできていたので個人的には非常に満足度が高い。並列コレクションやRDDのキャッシュを適切に扱えないとタイムアウトやOOMで不合格になるので、あやふやな理解とノリで書いたコードでは通らない。厳しい。試行錯誤の末 Discussion Forum に助けを求めにいったこともしばしば。