---
layout: post
title: "Java製の推薦システム用ライブラリ LibRec を動かしてみる"
lang: ja
date: 2017-04-23
---

**[LibRec](http://www.librec.net/)** というJava製の推薦システム用ライブラリがある。

[Treasure Dataインターンのとき](/note/td-intern-2016)やPython, Juliaで推薦アルゴリズムの実装をライブラリ化したとき ([FluRS](/note/flurs), [Recommendation.jl](/note/recommendation-julia)) にはこの実装を大いに参考にした。

しかし思い返すとこのライブラリ自体を実際に動かしたことがなかったので、[documentation](http://wiki.librec.net/doku.php?id=introduction)に従ってサンプルコードを読みつつ動かしてみる。

### 雰囲気

[CLIもあるらしい](http://wiki.librec.net/doku.php?id=CLIWalkthrough)けど、今回は普通にJavaでコードを書くタイプの例を試す。

Mavenプロジェクトなら `dependency` に `net.librec` を入れればすぐに使える:

```
<dependency>
    <groupId>net.librec</groupId>
    <artifactId>librec-core</artifactId>
    <version>2.0.0</version>
</dependency>
```

#### 1. Build data model

コードはデータモデルを生成するところから始まる:

<pre class="prettyprint">
// build data model
Configuration conf = new Configuration();
conf.set("dfs.data.dir", "/Users/takuti/src/github.com/guoguibing/librec/data");
TextDataModel dataModel = new TextDataModel(conf);
dataModel.buildDataModel();
</pre>

読み込むデータは `user-id item-id rating`（スペース区切り）からなるテキストファイルと[WekaのARFF](http://www.cs.waikato.ac.nz/ml/weka/arff.html)をサポートしている。

ファイルのパスやアルゴリズムのハイパーパラメータ（e.g., kNNの近傍数）はすべて `Configuration` 経由で設定する。その実体は [librec.properties](https://github.com/guoguibing/librec/blob/18176ed41027348ee2187d8686a1b2c0d4d39277/conf/librec.properties) で、この形式で記述した独自の設定をガッとまとめて読み込むことも可能:

<pre class="prettyprint">
Resource resource = new Resource("rec/cf/itemknn-test.properties");
conf.addResource(resource);
</pre>

`dataModel.buildDataModel()` では指定されたパス内のファイルをすべて読んで、train/testデータへの分割までやってくれる。このあたりの挙動もすべて [librec.properties](https://github.com/guoguibing/librec/blob/18176ed41027348ee2187d8686a1b2c0d4d39277/conf/librec.properties) に従っている。

#### 2. Build recommender context

さっき定義した `Configuration` と `dataModel` を使って、これから行うタスクのためのコンテキストを生成する:

<pre class="prettyprint">
// build recommender context
RecommenderContext context = new RecommenderContext(conf, dataModel);
</pre>

#### 3. Build similarity

求めたい類似度を設定して、計算して、それをコンテキストにセットする:

<pre class="prettyprint">
// build similarity
conf.set("rec.recommender.similarity.key" ,"item");
RecommenderSimilarity similarity = new PCCSimilarity();
similarity.buildSimilarityMatrix(dataModel);
context.setSimilarity(similarity);
</pre>

ここでは **アイテムに対して** (item-based)、**ピアソン相関係数** (PCC) に基づく類似度を計算させている。

#### 4. Build & run recommender

`Recommender` を生成してコンテキストを渡してあげる。ここでは近傍数 (`rec.neighbors.knn.number`) が5の `ItemKNNRecommender()` を生成:

<pre class="prettyprint">
// build recommender
conf.set("rec.neighbors.knn.number", "5");
Recommender recommender = new ItemKNNRecommender();
recommender.setContext(context);
</pre>

つまり、事前にコンテキストにセットしていた類似度の設定と合わせると、今回は『**ピアソン相関係数に基づく $k=5$ の item-based collaborative filtering**』を実行することになる。

ここまで来れば、実行はワンライン:

<pre class="prettyprint">
// run recommender algorithm
recommender.recommend(context);
</pre>

#### 5. Evaluation

`RMSEEvaluator` を生成して、それを `recommend()` 実行済の `recommender` の `evaluate()` に渡してあげることで評価が行われる:

<pre class="prettyprint">
// evaluate the recommended result
RecommenderEvaluator evaluator = new RMSEEvaluator();
System.out.println("RMSE:" + recommender.evaluate(evaluator)); // => RMSE:0.8352805769243591
</pre>

#### 6. Get results

`recommender.recommend()` で得られた推薦（予測）結果を `RecommendedItem` というオブジェクトのリストとして取得することができる。

取得対象の `RecommendedItem` にフィルターをかけることもできる。たとえば『**ユーザ#1またはアイテム#70を対象とする予測結果**』が見たければ、次のようにフィルターをかける:

<pre class="prettyprint">
// set id list of filter
List&lt;String&gt; userIdList = new ArrayList&lt;String&gt;();
List&lt;String&gt; itemIdList = new ArrayList&lt;String&gt;();
userIdList.add("1");
itemIdList.add("70");

// filter the recommended result
List&lt;RecommendedItem&gt; recommendedItemList = recommender.getRecommendedList();
GenericRecommendedFilter filter = new GenericRecommendedFilter();
filter.setUserIdList(userIdList);
filter.setItemIdList(itemIdList);
recommendedItemList = filter.filter(recommendedItemList);
</pre>

あとは煮るなり焼くなり。表示してみる:

<pre class="prettyprint">
// print filter result
for (RecommendedItem recommendedItem : recommendedItemList) {
    System.out.println(
            "user:" + recommendedItem.getUserId() + " " +
            "item:" + recommendedItem.getItemId() + " " +
            "value:" + recommendedItem.getValue()
    );
}

/*
user:1 item:1 value:3.72186572013805
user:1 item:9 value:3.6660434401297843
user:659 item:70 value:2.381236774589509
user:1065 item:70 value:2.9759100334538178
user:1 item:4 value:3.6802197608115867
user:918 item:70 value:2.660444061555275
*/
</pre>

確かにユーザ#1またはアイテム#70に対する結果のみが得られている。

以上、チュートリアルでした。

ここから先は、たとえばクエリを組み立ててDBに問い合わせる処理が来たりするのかな。

### 良さ

LibRecの強みは何と言っても豊富なアルゴリズム。

Most Popular（ひたすら一番人気のアイテムを推薦する）のような **Non-personalized Recommenders** から、古典的な**協調フィルタリング**、そして新しいところでは **Factorization Machines** や **Restricted Boltzmann Machine** を使った手法まで、実に70種類以上の推薦手法をサポートしている (cf. [Algorithm List](http://wiki.librec.net/doku.php?id=AlgorithmList))。

そして実装がシンプルで、とてもうまく設計されていると思う。

先の例だけ見ても、推薦システム構築の際の "**チェックポイント**" となりうるパーツが綺麗に分離されていることがわかる:

- Recommender
	- Context
		- Configuration
		- Data Model
		- Similarity
	- Evaluator
- Filter

「アルゴリズムを切り替えたいな」と思えば `Recommender recommender = new ItemKNNRecommender();` を別の Recommender にすれば良いし、類似度や評価指標の変更も同様にできる。

もちろん手法に応じて細かい設定項目は変わるけど、それらはすべて `Configuration` でラップしていて、手法にほぼ依存しないインタフェースを提供している。

これによって「さっきコンテキストをセットしたのにまた渡すの？」と思ってしまうような実装にはなるが、それはもはや些細な問題だと思う:

<pre class="prettyprint">
Recommender recommender = new ItemKNNRecommender();
recommender.setContext(context);
recommender.recommend(context);
</pre>

推薦アルゴリズムを自分で実装したことがある人なら分かると思うけど、複数の手法に対して同一のインタフェースを提供するのは結構難しい。評価値 (rating) 情報とランキング情報に対するデータ構造の違い（e.g., 行列 or リスト）や、アルゴリズムごとに異なる大量のハイパーパラメータ…考えただけで頭が痛い。それにもかかわらず、推薦というタスクは様々な設定（アルゴリズム、評価指標、類似度、データ、etc...）の組み合わせの試行錯誤が当たり前という現実もある。

その点、LibRecの実装から学ぶべきことは多い。

というわけで、突然中国語のdocumentが出てきたりしてたまに不安になるけど、これからも応援していきたいプロジェクト LibRec の話でした。