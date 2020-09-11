---
aliases: [/note/hive-fuzzy-search/]
categories: [プログラミング, 自然言語処理]
date: 2017-08-20
keywords: [search, postgresql, hive, mapreduce, 試し, 再現, ならでは, join, live, fuzzystrmatch]
lang: ja
recommendations: [/ja/note/hivemall-on-mac/, /ja/note/postgresql-fuzzy-search/, /ja/note/why-spark/]
title: HiveでテキストのFuzzy Search
---

先週は[PostgreSQL上でテキストのFuzzy Searchを試した](/note/postgresql-fuzzy-search)。そのときは [fuzzystrmatch](https://www.postgresql.org/docs/9.6/static/fuzzystrmatch.html) や [pg_trgm](https://www.postgresql.org/docs/9.6/static/pgtrgm.html) といったモジュールが活躍していた。

では、同じことをHiveで実現するとどうなるだろう。

### データ

適当にテーブル `sample` をつくっておく：

```
hive> CREATE TABLE sample AS
    > SELECT 1 AS id, 'I live in Tokyo.' AS document
    > UNION ALL
    > SELECT 2 AS id, 'Are you happy?' AS document
    > ;
```

```
hive> SELECT * FROM sample;
OK
sample.id       sample.document
1       I live in Tokyo.
2       Are you happy?
Time taken: 0.066 seconds, Fetched: 2 row(s)
```

なお、Hive環境のセットアップについては以下の記事も参考にされたい：

- [MacのローカルにHivemallを導入してアイテム推薦をするまで](/note/hivemall-on-mac)
- [Hivemall on Dockerを試すぜ](/note/hivemall-on-docker)

### 完全一致

`WHERE`句を使えばもちろん完全一致検索になる：

```
hive> SELECT * FROM sample WHERE document = 'I live';
OK
sample.id       sample.document
Time taken: 0.338 seconds
```

```
hive> SELECT * FROM sample WHERE document = 'I live in Tokyo.';
OK
sample.id       sample.document
1       I live in Tokyo.
Time taken: 0.079 seconds, Fetched: 1 row(s)
```

### LIKE

`LIKE` も素直に使える：

```
hive> SELECT * FROM sample WHERE document LIKE '%Tokyo%';
OK
sample.id       sample.document
1       I live in Tokyo.
Time taken: 0.093 seconds, Fetched: 1 row(s)
```

大文字・小文字を無視する `ILIKE` 相当の処理は明示的に小文字に変換してから：

```
hive> SELECT * FROM sample WHERE lower(document) LIKE '%tokyo%';
OK
sample.id       sample.document
1       I live in Tokyo.
Time taken: 0.078 seconds, Fetched: 1 row(s)
```

### 正規表現

`LIKE` の右辺値が正規表現になった、`RLIKE` がある。PostgreSQLの `~` 相当：

```
hive> SELECT * FROM sample WHERE document RLIKE '.*Tokyo.*';
OK
sample.id       sample.document
1       I live in Tokyo.
Time taken: 0.075 seconds, Fetched: 1 row(s)
```

### 編集距離

みんな大好き[Levenshtein Distance](/note/levenshtein-distance)。

PostgreSQLでは別途 [fuzzystrmatch](https://www.postgresql.org/docs/9.6/static/fuzzystrmatch.html) というモジュールが必要だったけど、Hiveは[1.2.0からこれを標準でサポートしている](https://issues.apache.org/jira/browse/HIVE-9556)。残念ながらPostgreSQLの `levenshtein_less_equal()` に相当する柔軟な関数はないけれど。

`I love Tokyo` からの編集距離を求めてみる：

```
hive> SELECT id, levenshtein(document, 'I love Tokyo') FROM sample;
OK
id      c1
1       5
2       11
Time taken: 0.068 seconds, Fetched: 2 row(s)
```

`I love Tokyo` という“クエリ”から編集距離5以下のテキストのみをFuzzy Searchすると：

```
hive> SELECT * FROM sample WHERE levenshtein(document, 'I love Tokyo') <= 5;
OK
sample.id       sample.document
1       I live in Tokyo.
Time taken: 0.076 seconds, Fetched: 1 row(s)
```

イイね。

### 文字のn-gram

Hiveには配列のn-gramを出力する `ngrams(array, int n, int k)` という関数がある。`array` の `n`-gram を求めて、その頻度（近似値）の上位 `k` 件を出力する。たとえば、 `I live in Tokyo. You live in Osaka.` というテキスト内の単語について 2-gram を上位3件出力してみると：

```
hive> SELECT ngrams(split('I live in Tokyo. You live in Osaka.', ' '), 2, 3);
OK
_c0
[{"ngram":["live","in"],"estfrequency":2.0},{"ngram":["I","live"],"estfrequency":1.0},{"ngram":["Tokyo.","You"],"estfrequency":1.0}]
Time taken: 6.29 seconds, Fetched: 1 row(s)
```

`["live","in"]` という 2-gram が2回出現するため最上位に出力され、残りはすべて1回なので適当な2つが第2位、第3位として出力される。

入力には `array` をとるので、単語の n-gram ならば先の例のようにスペース区切りで分割 `split(document, ' ')`、文字の n-gram ならば `split(document, '')` と分割したものを渡すことに注意。

PostgreSQLはtri-gramに限定した検索機能をモジュール [pg_trgm](https://www.postgresql.org/docs/9.6/static/pgtrgm.html) で提供していた。n-gram (n=3) に限定されてしまうが、検索に特化した `%` という演算子の存在は大きかった。

一方、Hiveで文字のtri-gramを求めると次のような雰囲気（上位10件を出力）：

```
hive> SELECT id, ngrams(split(document, ''), 3, 10) FROM sample GROUP BY id;
OK
id      c1
1       [{"ngram":[" ","T","o"],"estfrequency":1.0},{"ngram":[" ","l","i"],"estfrequency":1.0},{"ngram":["I"," ","l"],"estfrequency":1.0},{"ngram":["T","o","k"],"estfrequency":1.0},{"ngram":["i","n"," "],"estfrequency":1.0},{"ngram":["i","v","e"],"estfrequency":1.0},{"ngram":["l","i","v"],"estfrequency":1.0},{"ngram":["o","k","y"],"estfrequency":1.0},{"ngram":["v","e"," "],"estfrequency":1.0},{"ngram":["y","o","."],"estfrequency":1.0}]
2       [{"ngram":[" ","h","a"],"estfrequency":1.0},{"ngram":[" ","y","o"],"estfrequency":1.0},{"ngram":["e"," ","y"],"estfrequency":1.0},{"ngram":["h","a","p"],"estfrequency":1.0},{"ngram":["o","u"," "],"estfrequency":1.0},{"ngram":["p","p","y"],"estfrequency":1.0},{"ngram":["p","y","?"],"estfrequency":1.0},{"ngram":["u"," ","h"],"estfrequency":1.0},{"ngram":["y","?",""],"estfrequency":1.0},{"ngram":["y","o","u"],"estfrequency":1.0}]
Time taken: 14.782 seconds, Fetched: 2 row(s)
```

ごちゃごちゃしてきた…。結果を `LATERAL VIEW explode()` で展開して、各テキストの tri-gram を列挙してみる：

```
hive> WITH document_trigrams AS (
    >   SELECT
    >     id,
    >     ngrams(split(document, ''), 3, 10) AS trigrams_top10
    >   FROM
    >     sample
    >   GROUP BY
    >     id
    > )
    > SELECT
    >   id,
    >   concat_ws(',', trigram.ngram) AS trigram
    > FROM
    >   document_trigrams
    >   LATERAL VIEW explode(trigrams_top10) t AS trigram
    > ;
OK
id      trigram
1        ,T,o
1        ,l,i
1       I, ,l
1       T,o,k
1       i,n,
1       i,v,e
1       l,i,v
1       o,k,y
1       v,e,
1       y,o,.
2        ,h,a
2        ,y,o
2       e, ,y
2       h,a,p
2       o,u,
2       p,p,y
2       p,y,?
2       u, ,h
2       y,?,
2       y,o,u
Time taken: 5.31 seconds, Fetched: 20 row(s)
```

これなら検索に使えそう。クエリの tri-gram も同様に求めて、各テキストの tri-gram とどれだけ一致するか見てあげればよい。

たとえばtypoを含むクエリ `I live in Kyoto` からテキストを検索すると、`JOIN` + `count` で tri-gram の一致度が測れて：

```
hive> WITH document_trigrams_exploded AS (
    >   SELECT
    >     id,
    >     concat_ws(',', trigram.ngram) AS trigram
    >   FROM (
    >     SELECT
    >       id,
    >       ngrams(split(document, ''), 3, 10) AS trigrams_top10
    >     FROM
    >       sample
    >     GROUP BY
    >       id
    >   ) t1
    >   LATERAL VIEW explode(trigrams_top10) t2 AS trigram
    > ),
    > query_trigrams_exploded AS (
    >   SELECT
    >     concat_ws(',', trigram.ngram) AS trigram
    >   FROM (
    >     SELECT ngrams(split('I live in Kyoto', ''), 3, 10) AS trigrams_top10
    >   ) t1
    >   LATERAL VIEW explode(trigrams_top10) t2 AS trigram
    > )
    > SELECT
    >   l.id,
    >   count(1) AS num_matched_trigrams
    > FROM
    >   document_trigrams_exploded l
    > JOIN
    >   query_trigrams_exploded r
    >   ON l.trigram = r.trigram
    > GROUP BY
    >   id
    > ;
OK
l.id    num_matched_trigrams
1       6
Time taken: 17.536 seconds, Fetched: 1 row(s)
```

`I live in Tokyo.`（テキスト）と`I live in Kyoto`（クエリ）は上位10件の文字のtri-gramのうち6個が一致した、と分かる。逆に、`Are you happy?` とは1つも一致しない。

このカウントを `HAVING` 句でフィルタリングしたり、その上位N件を出力したりすれば文字のtri-gramに基づくFuzzy Searchが実現できそう。

PostgreSQLと比べると随分長い道のりになってしまった…。

### PostgreSQLのTSVectorっぽい何か

PostgreSQLには、自然言語的にもっと直感に即した“それっぽさ”を見る **TSVector** という表現があった。stop word の除外や大文字・小文字の統一まですべてやってくれる便利な子だ：

```
sample=# select to_tsvector('Left of the Dial');
    to_tsvector
-------------------
 'dial':4 'left':1
(1 row)
```

Hiveで同様のことを実現するには `split()` や `lower()` を組み合わせればよさそう：

```
hive> SELECT collect_list(token) AS tokens
    > FROM (
    >   SELECT split(lower('Left of the Dial'), ' ') AS tokens
    > ) t1
    > LATERAL VIEW explode(tokens) t2 AS token
    > WHERE NOT array_contains(array('of', 'the', 'a', 'an'), token)
    > ;
OK
tokens
["left","dial"]
Time taken: 12.633 seconds, Fetched: 1 row(s)
```

TSVectorと違って字句の出現位置は得られないけど、だいたい同じ雰囲気。`array('of', 'the', 'a', 'an')` は予め定義した stop word のリストで、本来はもっと多い。

なお、Hivemallの [`tokenize()`](https://hivemall.incubator.apache.org/userguide/misc/tokenizer.html) と [`is_stopword()`](https://hivemall.incubator.apache.org/userguide/misc/generic_funcs.html#text-processing-functions) を使うともう少し楽です：

```
hive> SELECT collect_list(token) AS tokens
    > FROM (
    >   SELECT tokenize('Left of the Dial', true) AS tokens
    > ) t1
    > LATERAL VIEW explode(tokens) t2 AS token
    > WHERE NOT is_stopword(token)
    > ;
OK
tokens
["left","dial"]
Time taken: 5.168 seconds, Fetched: 1 row(s)
```

この結果を使えば、あとは n-gram の場合と同様に `JOIN` + `count`、そしてクエリの `token` とどれだけ一致するかによって字句レベルの検索が実現できる。

### サウンド距離

Levenshtein Distance同様、[Hive1.2.0からサウンド距離を求めるために使える関数 `soundex()` がサポートされている](https://issues.apache.org/jira/browse/HIVE-9738)。この関数自体は、文字列を[Soundexと呼ばれる発音コード](https://en.wikipedia.org/wiki/Soundex)に変換するだけのもの。『テキスト間のサウンド距離』を得るためには、その発音コードたちを比較する必要がある。

テキスト内の単語をSoundexに変換してみる：

```
hive> SELECT
    >   id,
    >   soundex(word)
    > FROM
    >   sample
    > LATERAL VIEW explode(split(document, ' ')) t AS word
    > ;
OK
id      _c1
1       I000
1       L100
1       I500
1       T200
2       A600
2       Y000
2       H100
Time taken: 0.038 seconds, Fetched: 7 row(s)
```

`I live in Tokyo.` の発音コードは `Ixxx`, `Lxxx`, `Ixxx`, `Txxx` となっておりそれっぽい。

では、クエリ `I live in Kyoto` の発音コードと比較してみよう：

```
hive> WITH document_soundex AS (
    >   SELECT
    >     id,
    >     soundex(word) AS soundex
    >   FROM
    >     sample
    >   LATERAL VIEW explode(split(document, ' ')) t AS word
    > ),
    > query_soundex AS (
    >   SELECT
    >     soundex(word) AS soundex
    >   FROM (
    >     SELECT 'I live in Kyoto' AS query
    >   ) t1
    >   LATERAL VIEW explode(split(query, ' ')) t2 AS word
    > )
    > SELECT
    >   l.id,
    >   count(1) AS num_matched_soundex
    > FROM
    >   document_soundex l
    > JOIN
    >   query_soundex r
    >   ON l.soundex = r.soundex
    > GROUP BY
    >   id
    > ;
OK
l.id    num_matched_soundex
1       3
Time taken: 13.174 seconds, Fetched: 1 row(s)
```

`I live in` の3つの発音コードが一致する。

もちろんこのままだとFuzzy Searchにならないので、実際には`soundex()`を文字のn-gramに対して適用する、など工夫が必要。

### まとめ

[PostgreSQLで試したFuzzy Search](/note/postgresql-fuzzy-search)と同等のことをHiveでやるとどうなるか、という話。それなりに同じような結果が再現できる。

PostgreSQL同様、複数の方法を組み合わせたクエリも当然書ける。ただし、HiveではそれがMapReduceタスクとして処理されるということを忘れてはならない。

MapReduceならではの制約というものは結構あって、たとえば [`LIKE` によるJOINはできなかったりする](https://stackoverflow.com/questions/31340218/hive-like-operator)。