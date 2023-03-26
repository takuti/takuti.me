---
aliases: [/note/hivemall-on-mac/]
categories: [機械学習, 情報推薦]
date: 2017-02-11
lang: ja
title: MacのローカルにHivemallを導入してアイテム推薦をするまで
lastmod: '2022-01-18'
keywords: [hive, hadoop, mac, hivemall, 動かす, インストール, 映画, 推薦, ローカル, ライブラリ]
recommendations: [/ja/note/hivemall-on-docker/, /ja/note/recommender-libraries/, /ja/note/hive-fuzzy-search/]
---

昨年、Hive向けの機械学習ライブラリ **[Hivemall](https://hivemall.incubator.apache.org/)** が[Apache Software Foundationのincubatorプロジェクトになった](http://itpro.nikkeibp.co.jp/atcl/column/15/061500148/100300084/)。[Treasure Dataがオフィシャルでサポートしている](https://docs.treasuredata.com/articles/hive-hivemall)ということもあり、名前くらいは聞いたことがあるという人も多いと思う。

とはいえ、やれHadoopだHiveだとスケールの大きな話をされると、手元でちょっと試すなんて気分にはならないものである。というわけで、実際にMacのローカルでHadoop, Hiveの導入からHivemallを動かすまでをやってみた。

### Hadoopのインストール

```
$ brew install hadoop
```

（今回のバージョンは 2.7.3）

`/usr/local/Cellar/hadoop/{バージョン}` 以下を直接漁ることになるのでエイリアスを設定しておく。

```sh
export HADOOP_DIR=/usr/local/Cellar/hadoop/{バージョン}
```

`${HADOOP_DIR}/libexec/etc/hadoop/core-site.xml` の `<configuration>` を編集：

```xml
<configuration>
	<property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value>
  </property>
</configuration>
```

`${HADOOP_DIR}/libexec/etc/hadoop/hdfs-site.xml` の `<configuration>` を編集：

```
<configuration>
  <property>
    <name>dfs.replication</name>
    <value>1</value>
  </property>
</configuration>
```

HDFSをフォーマット：

```
$ hdfs namenode -format
```

localhostへのSSH接続を許可する必要があるので、Macの **システム環境設定 > 共有** からリモートログインを有効にする。さらに、SSH公開鍵を自身のauthorized_keysに追加する。

```
$ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```

これで `$ ssh localhost` ができる。

Hadoopの設定おわり。

起動・終了はエイリアスを設定しておくと便利：

```sh
alias hstart=${HADOOP_DIR}/sbin/start-all.sh
alias hstop=${HADOOP_DIR}/sbin/stop-all.sh
```

```
$ hstart
```

うごく。

```
$ hstop
```

とまる。

### Hiveのインストール

```
$ brew install hive
```

（今回のバージョンは 2.1.0）

適当に作業用ディレクトリ（今回は `~/hive` ）を掘って、そこでスキーマを初期化する：

```
$ mkdir ~/hive
$ cd ~/hive
$ schematool -initSchema -dbType derby
```

HadoopとHiveを起動する：

```
$ hstart
$ hive
hive>
```

### Hivemallのインストール

基本は[ここ](https://hivemall.incubator.apache.org/userguide/getting_started/installation.html)にある通り。

まずビルド済みのHivemall `hivemall-core-xxx-with-dependencies.jar` を[GitHubリポジトリ](https://github.com/myui/hivemall/releases)からダウンロードする。

そしてHiveの起動時スクリプトとして以下を `~/.hiverc` に書いてあげる：

```
add jar /path/to/hivemall-core-xxx-with-dependencies.jar;
```

これだけ。

Hivemallは機械学習に特化したHiveの関数セットなので、なにか仰々しいインストールスクリプトが走るというものではない。

### Hivemallでアイテム推薦

ここまででMacのローカルにHadoop、Hive、そしてHivemallが導入できた。最後に一例として、アイテム推薦をHivemall上でやってみよう。

使うアルゴリズムは **Matrix Factorization** で、これや推薦手法全般の概略は「[Courseraの推薦システムのコースを修了した](https://takuti.me/note/coursera-recommender-systems/)」を読んでほしい。

Hivemall公式のチュートリアルは[ここ](https://hivemall.incubator.apache.org/userguide/recommend/movielens_dataset.html)にある。

#### Step 1: MovieLens 1MデータセットでHiveテーブルを作る

[MovieLens 1M](https://grouplens.org/datasets/movielens/1m/)は推薦の分野では定番のデータセット。これを使って **Matrix Factorizationでアイテム（映画）の推薦** を成し遂げるべく、Hiveテーブルを作成していく。

まずHiveでのDB、テーブル作成用スクリプトを `create_db.hive` のような名前で以下の中身で作って、Hiveの作業用ディレクトリで走らせる：

```sql
create database movielens;
use movielens;

CREATE EXTERNAL TABLE ratings (
  userid INT,
  movieid INT,
  rating INT,
  tstamp STRING
) ROW FORMAT DELIMITED
FIELDS TERMINATED BY '#' -- 適当な1文字のセパレータ
STORED AS TEXTFILE
LOCATION '/dataset/movielens/ratings';
```

```
$ hive < create_db.hive
```

そしてデータをダウンロード：

```
$ curl -o ml-1m.zip -L http://files.grouplens.org/datasets/movielens/ml-1m.zip
$ unzip ml-1m.zip
$ cd ml-1m
```

使うのは `ratings.dat` で、ユーザごとのアイテム（映画）に対する評価値が入っている。このセパレータをテーブル作成時の適当な1文字にしておく（今回は `#` ）：

```
$ sed 's/::/#/g' ratings.dat > ratings.t
```

そしてこのデータをHDFSにコピーする：

```
$ hadoop fs -put ratings.t /dataset/movielens/ratings
```

Hiveに入ってデータを確認する：

```
$ hive
hive> use movielens;
hive> select * from ratings limit 5;
OK
1       1193    5       978300760
1       661     3       978302109
1       914     3       978301968
1       3408    4       978300275
1       2355    5       978824291
Time taken: 1.36 seconds, Fetched: 5 row(s)
```

よさそう。

（以下、すべてHiveのインタラクティブシェル `hive>` 上での入力）

#### Step 2: Hivemallから使う関数を呼び出す

 **Matrix Factorizationでアイテム推薦** のために使う関数たちを読み込んであげる。Matrix Factorizationで2つ　( `mf_predict` , `train_mf_sgd` ) 、推薦リストの生成に1つ ( `each_top_k` )、そしてユーティリティ関数を2つ ( `array_avg` , `to_ordered_map` ) 読んでいる。

```sql
create temporary function mf_predict as 'hivemall.mf.MFPredictionUDF';
create temporary function train_mf_sgd as 'hivemall.mf.MatrixFactorizationSGDUDTF';
create temporary function each_top_k as 'hivemall.tools.EachTopKUDTF';
create temporary function array_avg as 'hivemall.tools.array.ArrayAvgGenericUDAF';
create temporary function to_ordered_map as 'hivemall.tools.map.UDAFToOrderedMap';
```

ちなみに、これらを `~/.hiverc` の `add jar ...` の後に直接書いておけば、起動時に毎回関数を自動で読み込んでくれる。

#### Step 3: クエリで「おすすめ映画リスト」をつくる

あとは中間テーブルを作成しつつクエリを実行していけば「おすすめ映画リスト」が得られる。

まず `train_mf_sgd` にユーザIDと映画ID、評価値を渡せば、Matrix Factorizationが走ってモデルが返ってくる：

```sql
CREATE TABLE mf_model AS
SELECT
  idx,
  array_avg(u_rank) as Pu,
  array_avg(i_rank) as Qi,
  avg(u_bias) as Bu,
  avg(i_bias) as Bi
FROM (
  SELECT
    train_mf_sgd(userid, movieid, rating) AS (idx, u_rank, i_rank, u_bias, i_bias)
  FROM ratings
) t
GROUP BY idx
;
```

そして推薦対象のユーザID `userid` と、推薦リストのサイズ `k` を変数として設定して、

```sql
set hivevar:userid=1;
set hivevar:k=10;
```

対象ユーザに対して各映画の評価値を予測して、その上位k件の「おすすめ映画リスト」を返すクエリが以下：

```sql
WITH top_k AS (
  SELECT
    each_top_k(
		  ${k}, u.userid, mf_predict(u.pu, i.qi, u.bu, i.bi),
      u.userid, movieid
		) AS (rank, score, userid, movieid)
  FROM (
	  SELECT idx AS userid, pu, bu
	  FROM mf_model m
	  WHERE m.idx = ${userid}
	) u
  CROSS JOIN (
	  SELECT idx AS movieid, qi, bi
	  FROM mf_model m
	) i
)
SELECT
  userid,
  map_values(to_ordered_map(rank, movieid)) AS recommended_items
FROM
  top_k
GROUP BY
  userid
;
```

結果はこんな感じで、ID=1のユーザはID=926とか905とかの映画が好きなんだなぁという気持ちになって無事目標達成。

|userid|recommended_items|
|:---:|:---|
|1|[926,905,922,3030,928,910,3022,904,909,916]|

### まとめ

MacのローカルにHadoop, Hiveをインストールして、機械学習ライブラリHivemallを使ったアイテム推薦までやってみた。

Hadoop, Hiveに必要な設定は思っていたよりも少なかった。

アイテム推薦に関しては、「とりあえず動かす」ことに専念したので、

- 精度の評価はどうするのか
- Matrix Factorizationのパラメータはどうするのか
- ユーザがすでに評価した、既知の映画まで推薦してしまって良いのか

といった問題が残っている。このあたりはまたの機会に書こうと思う。

### 参考

- [INSTALLING HADOOP ON MAC PART 1](https://amodernstory.com/2014/09/23/installing-hadoop-on-mac-osx-yosemite/)
- [Macに10分でHadoop,Hive環境を作る](http://qiita.com/zaburo/items/6086ded8cbb43e2ddd39)
- [Hive installation issues: Hive metastore database is not initialized](http://stackoverflow.com/questions/35655306/hive-installation-issues-hive-metastore-database-is-not-initialized)