---
date: 2017-05-07
lang: ja
recommendations: [/note/hivemall-on-mac/, /note/recommender-libraries/, /note/td-intern-2016/]
title: Hivemall on Dockerを試すぜ
---

[@amaya382](https://twitter.com/amaya382)くんが Hivemall on Docker についていろいろと整備してくれた。

https://twitter.com/amaya382/status/856860886807568384

一方、個人的には Hivemall on Mac について以前記事を書いた：『[MacのローカルにHivemallを導入してアイテム推薦をするまで](/note/hivemall-on-mac/)』

だいたいHomebrewで完結するのでMacローカルだけを考えればこれでも問題ないけど、煩雑なインストール・設定無しでDockerコンテナで話が進むに越したことはない。というわけで先の記事のフォローアップとして Hivemall on Docker をMacのローカルで試してみる。環境は次の通り：

- macOS Sierra 10.12.3
- [Docker for Mac](https://docs.docker.com/docker-for-mac/install/#download-docker-for-mac) Stable channel (version 17.03.1-ce-mac5)

```
$ docker -v
Docker version 17.03.1-ce, build c6d412e
$ docker-compose -v
docker-compose version 1.11.2, build dfed245
$ docker-machine -v
docker-machine version 0.10.0, build 76ed2a6
```

### コンテナ起動まで

基本的には[ドキュメント](https://hivemall.incubator.apache.org/userguide/docker/getting_started.html)に従う。

まず[リポジトリ](https://github.com/apache/incubator-hivemall)を取ってきて、

```
$ cd /path/to/incubator-hivemall
```

ビルドは `docker-compose` なら：

```
$ docker-compose -f resources/docker/docker-compose.yml build
```

`docker build` なら：

```
$ docker build -f resources/docker/Dockerfile .
```

筋トレしながら待つ。

おわったら、コンテナ起動は `docker-compose` なら：

```
$ docker-compose -f resources/docker/docker-compose.yml up -d && docker attach hivemall
```

`docker run` なら：

```
$ docker run -it \
	-p 8088:8088 \
	-p 19888:19888 \
	-p 50070:50070 \
	hivemall
```

このとき、

- `docker-compose.yml` で `volumes: "../../:/opt/hivemall/"` を指定する
- `docker run` にオプション `--volume $(pwd):/opt/hivemall` を渡す

のいずれかでホストの `/path/to/incubator-hivemall` をコンテナ上の `/opt/hivemall` (`$HIVEMALL_PATH`) にマウントできる。

すると、ローカルで開発→ビルド→コンテナ起動＆マウント、という感じでスムーズにHivemall開発ができます。やったね。

### Hivemallのビルド＆データセット準備

コンテナに入ったならば、とりあえずHiveを起動してみる：

```
# hive
```

このとき、`/opt/hivemall` に存在するHivemallがビルド済みである（i.e., `/opt/hivemall/target/hivemall-core-(バージョン)-with-dependencies.jar` が存在する）必要がある。もしビルドされていなければ、（コンテナ内から）ビルドをしてあげる：

```
# cd $HIVEMALL_PATH && ./bin/build.sh
```

準備OK。

ここで、分類問題のテストデータとして有名な [Iris データセット](https://en.wikipedia.org/wiki/Iris_flower_data_set) をHDFSに読み込んでくれるスクリプトがおまけとして `$HOME/bin/prepare_iris.sh` に用意されているので、これを使ってみる：

```
# cd $HOME && ./bin/prepare_iris.sh
```

Hiveに入って、読み込んだばかりの Iris データセットを確認：

```
# hive
hive> use iris;
hive> select * from iris_raw limit 5;
OK
1       Iris-setosa     [5.1,3.5,1.4,0.2]
2       Iris-setosa     [4.9,3.0,1.4,0.2]
3       Iris-setosa     [4.7,3.2,1.3,0.2]
4       Iris-setosa     [4.6,3.1,1.5,0.2]
5       Iris-setosa     [5.0,3.6,1.4,0.2]
``` 

よさそう。

ここまでくれば、[HivemallのIrisチュートリアルのData preparation](https://hivemall.incubator.apache.org/userguide/multiclass/iris_dataset.html)は終わっているので、RandomForestなり何なりで分類を試すことができる。

便利な時代になりました。

### まとめ

- Hivemall on Docker が整備されている。
- Dockerコンテナで話が進むので「ちょっとHivemall試したい」というときの汎用的かつ簡単な方法としてGood。
- 『[MacのローカルにHivemallを導入してアイテム推薦をするまで](/note/hivemall-on-mac/)』と比較すると、導入までのステップ数は激減。