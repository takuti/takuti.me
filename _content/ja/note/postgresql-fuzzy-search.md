---
aliases: [/note/postgresql-fuzzy-search/]
categories: [エンジニアリング, データ・アルゴリズム]
date: 2017-08-09
lang: ja
title: あのときのビールをもう一度（PostgreSQLでFuzzy Searchを試す）
lastmod: '2026-03-20'
keywords: [levenshtein, distance, seven, 検索, ホット, order, trgm, postgresql, fuzzystrmatch,
  weeks]
recommendations: [/ja/note/levenshtein-distance/, /ja/note/hive-fuzzy-search/, /ja/note/designing-data-intensive-applications/]
---

**[Seven Databases in Seven Weeks](https://pragprog.com/book/rwdata/seven-databases-in-seven-weeks)** を読んでいたら、PostgreSQLでテキスト検索をする話が出てきた。[先日 Levenshtein Distance（編集距離）について書いたばかり](/note/levenshtein-distance)でホットな話題なので、少し遊んでみよう。

```sh
$ postgres --version
postgres (PostgreSQL) 9.6.3
```

※インデックスと英語以外の言語の場合については割愛。

### データ

お気に入りの[アメリカのクラフトビールデータセット](https://www.kaggle.com/nickhould/craft-cans)を使う。適当に `create table` してCSVからデータを読み込む：

```sql
create table beers (
    key int,
    abv real,
    ibu real,
    id int,
    name varchar(128),
    style varchar(64),
    brewery_id int,
    ounces real
);
\copy beers from 'beers.csv' with csv;
```

```
sample=# select * from beers limit 5;
 key |  abv  | ibu |  id  |        name         |             style              | brewery_id | ounces
-----+-------+-----+------+---------------------+--------------------------------+------------+--------
   0 |  0.05 |     | 1436 | Pub Beer            | American Pale Lager            |        408 |     12
   1 | 0.066 |     | 2265 | Devil's Cup         | American Pale Ale (APA)        |        177 |     12
   2 | 0.071 |     | 2264 | Rise of the Phoenix | American IPA                   |        177 |     12
   3 |  0.09 |     | 2263 | Sinister            | American Double / Imperial IPA |        177 |     12
   4 | 0.075 |     | 2262 | Sex and Candy       | American IPA                   |        177 |     12
```

やったぜ。

今回は[RecSys2016に参加したとき](/note/recsys-2016)にいい感じのパブで飲んだ、[Notch Brewing](http://www.notchbrewing.com/)（マサチューセッツ州）のビール "**Left of the Dial**" (ABV 4.3%) を当該データセットから探す。1年前の思い出をもう一度！~~（そんなに好みのビールじゃなかったけど）~~

<blockquote class="instagram-media" data-instgrm-captioned data-instgrm-version="7" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:512px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:8px;"> <div style=" background:#F8F8F8; line-height:0; margin-top:40px; padding:50.0% 0; text-align:center; width:100%;"> <div style=" background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAsCAMAAAApWqozAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAMUExURczMzPf399fX1+bm5mzY9AMAAADiSURBVDjLvZXbEsMgCES5/P8/t9FuRVCRmU73JWlzosgSIIZURCjo/ad+EQJJB4Hv8BFt+IDpQoCx1wjOSBFhh2XssxEIYn3ulI/6MNReE07UIWJEv8UEOWDS88LY97kqyTliJKKtuYBbruAyVh5wOHiXmpi5we58Ek028czwyuQdLKPG1Bkb4NnM+VeAnfHqn1k4+GPT6uGQcvu2h2OVuIf/gWUFyy8OWEpdyZSa3aVCqpVoVvzZZ2VTnn2wU8qzVjDDetO90GSy9mVLqtgYSy231MxrY6I2gGqjrTY0L8fxCxfCBbhWrsYYAAAAAElFTkSuQmCC); display:block; height:44px; margin:0 auto -44px; position:relative; top:-22px; width:44px;"></div></div> <p style=" margin:8px 0 0 0; padding:0 4px;"> <a href="https://www.instagram.com/p/BKji_1DDncp/" style=" color:#000; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none; word-wrap:break-word;" target="_blank">woo~🍺</a></p> <p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;">A post shared by @takuti on <time style=" font-family:Arial,sans-serif; font-size:14px; line-height:17px;" datetime="2016-09-19T23:09:25+00:00">Sep 19, 2016 at 4:09pm PDT</time></p></div></blockquote> <script async defer src="//platform.instagram.com/en_US/embeds.js"></script>

### 完全一致

まずは愚直に `where` 句で完全一致検索をしてみよう：

```
sample=# select * from beers where name = 'Left of the Dial';
 key | abv | ibu | id | name | style | brewery_id | ounces
-----+-----+-----+----+------+-------+------------+--------
(0 rows)
```

無い…。

### LIKE と ILIKE

そんなはずはない！というわけで、Fuzzy Search を試みる。

`LIKE` でビール名の前後に何らかの文字列があることを許容すれば：

```
sample=# select * from beers where name LIKE '%Left of the Dial%';
 key  |  abv  | ibu |  id  |         name         |    style     | brewery_id | ounces
------+-------+-----+------+----------------------+--------------+------------+--------
 1504 | 0.043 |     | 1917 | Left of the Dial IPA | American IPA |        271 |     12
(1 row)
```

あったー！ABVも記録と一致している。まさにこれだ。

`ILIKE` は `LIKE` の大文字・小文字を無視する版で、全部小文字で検索してもお目当てのビールがヒットするようになる：

```
sample=# select * from beers where name LIKE '%left of the dial%';
 key | abv | ibu | id | name | style | brewery_id | ounces
-----+-----+-----+----+------+-------+------------+--------
(0 rows)

sample=# select * from beers where name ILIKE '%left of the dial%';
 key  |  abv  | ibu |  id  |         name         |    style     | brewery_id | ounces
------+-------+-----+------+----------------------+--------------+------------+--------
 1504 | 0.043 |     | 1917 | Left of the Dial IPA | American IPA |        271 |     12
(1 row)
```

### 正規表現

もう少し柔軟に、正規表現を使った検索も可能。

先の `LIKE` 相当の正規表現マッチは `~` で探して次の通り：

```
sample=# select * from beers where name ~ '.*Left of the Dial.*';
 key  |  abv  | ibu |  id  |         name         |    style     | brewery_id | ounces
------+-------+-----+------+----------------------+--------------+------------+--------
 1504 | 0.043 |     | 1917 | Left of the Dial IPA | American IPA |        271 |     12
(1 row)
```

`~*` で探せば、大文字・小文字を無視してくれて `ILIKE` 相当の結果も得られる：

```
sample=# select * from beers where name ~ '.*left of the dial.*';
 key | abv | ibu | id | name | style | brewery_id | ounces
-----+-----+-----+----+------+-------+------------+--------
(0 rows)

sample=# select * from beers where name ~* '.*left of the dial.*';
 key  |  abv  | ibu |  id  |         name         |    style     | brewery_id | ounces
------+-------+-----+------+----------------------+--------------+------------+--------
 1504 | 0.043 |     | 1917 | Left of the Dial IPA | American IPA |        271 |     12
(1 row)
```

### 編集距離

とはいえ、検索クエリは `LIKE` と正規表現だけでカバーできるほど単純なものではない。特にtypo、これが厄介。

そこで**編集距離** (Levenshtein Distance) を使って、もう少しtypoにロバストなクエリにする。

PostgreSQLでは `fuzzystrmatch` モジュールに関数 `levenshtein` などが含まれている：

```
sample=# create extension fuzzystrmatch;
CREATE EXTENSION
sample=# select levenshtein('kitten', 'sitting');
 levenshtein
-------------
           3
(1 row)
```

"Left of the Dial" からの編集距離が10以下のビールは結構ある：

```
sample=# select * from beers where levenshtein(lower(name), lower('Left of the Dial')) <= 10;
 key  |  abv  | ibu |  id  |         name         |          style           | brewery_id | ounces
------+-------+-----+------+----------------------+--------------------------+------------+--------
  274 | 0.054 |     | 1411 | Sawtooth Ale         | American Blonde Ale      |        407 |     12
  383 | 0.072 |  60 | 1801 | Last Stop IPA        | American IPA             |        308 |     12
  428 | 0.073 |     | 1785 | Le Flaneur Ale       | American Wild Ale        |         10 |     16
  690 | 0.072 |     | 1623 | Lift Off IPA         | American IPA             |        358 |     16
  695 |  0.06 |     | 2371 | Neato Bandito        | Euro Pale Lager          |        127 |     12
 1101 | 0.068 |  90 | 1903 | Let It Ride IPA      | American IPA             |        277 |     12
 1385 | 0.075 |  85 | 2159 | City of the Sun      | American IPA             |        209 |     16
 1493 | 0.045 |  50 | 2692 | Get Together         | American IPA             |          0 |     16
 1504 | 0.043 |     | 1917 | Left of the Dial IPA | American IPA             |        271 |     12
 1650 |  0.06 |  20 | 1791 | Hot Date Ale         | Chile Beer               |        314 |     16
 1658 | 0.065 |     | 2559 | Blood of the Unicorn | American Amber / Red Ale |         52 |     16
 1702 |  0.08 |     | 1375 | Nectar of the Hops   | Mead                     |        421 |     16
 2171 | 0.041 |     | 1780 | Rise to the Top      | Cream Ale                |        142 |     12
 2337 |       |     |  652 | West Sixth IPA       | American IPA             |        100 |     12
(14 rows)
```

また、`levenshtein_less_equal(string 1, string 2, max distance)` は `max distance` より小さい編集距離の文字列に対してはその正確な編集距離を、それ以外については `max distance` より大きな適当な値（ここでは `max distance + 1`）を返す関数：

```sql
select
    name,
    levenshtein(lower(name), lower('Left of the Dial')), /* 正確な編集距離 */
    levenshtein_less_equal(lower(name), lower('Left of the Dial'), 11) /* 編集距離11以下だけ真面目に計算する */
from
    beers
limit
    5;
```

```
        name         | levenshtein | levenshtein_less_equal
---------------------+-------------+------------------------
 Pub Beer            |          14 |                     12
 Devil's Cup         |          14 |                     12
 Rise of the Phoenix |          11 |                     11
 Sinister            |          14 |                     12
 Sex and Candy       |          13 |                     12
(5 rows)

```

これいいですね。『[いまさら編集距離 (Levenshtein Distance) を実装するぜ](/note/levenshtein-distance)』でも書いたとおり Levenshtein Distance は動的計画法によって計算されるので、明らかに `max distance` より距離が大きくなるケースをさっさと切り捨てるのは小粒でぴりりと辛い工夫。

編集距離6以下を探せば、"Left of the Dial IPA" のみがヒットするようになる：

```
sample=# select * from beers where levenshtein_less_equal(lower(name), lower('Left of the Dial'), 6) <= 6;
 key  |  abv  | ibu |  id  |         name         |    style     | brewery_id | ounces
------+-------+-----+------+----------------------+--------------+------------+--------
 1504 | 0.043 |     | 1917 | Left of the Dial IPA | American IPA |        271 |     12
(1 row)
```

そして問題のtypoだが、この通り `Dial` を `Daniel` にtypoしても問題ない：

```
sample=# select * from beers where levenshtein_less_equal(lower(name), lower('Left of the Dniel'), 6) <= 6;
 key  |  abv  | ibu |  id  |         name         |    style     | brewery_id | ounces
------+-------+-----+------+----------------------+--------------+------------+--------
 1504 | 0.043 |     | 1917 | Left of the Dial IPA | American IPA |        271 |     12
(1 row)
```

『どの程度typoを許容するか』と『ヒットする件数』はトレードオフの関係にあるので、閾値を定めるのは結構大変。

### 文字のtri-gram

編集距離以上にtypoにロバストなのが、文字の**tri-gram**による検索。

文字のtri-gramは[単語のマルコフ連鎖](/note/twitter-bot)の文字版、のようなイメージ。PostgreSQLでは `pg_trgm` モジュールをいれることでtri-gramのマッチ（文字列の部分的な一致）による柔軟な検索ができる。

たとえば `Avatar` という文字列からは `av` や `ata` のようなtri-gramが得られて、我々はそのtri-gramの意味で一致する文字列を探すことができる：

```
sample=# create extension pg_trgm;
CREATE EXTENSION
sample=# select show_trgm('Avatar');
              show_trgm
-------------------------------------
 {"  a"," av","ar ",ata,ava,tar,vat}
(1 row)
```

実際には、`where` 句の `=` や `~` を `%` に置き換えるだけでtri-gramベースの検索が走る。

末尾の `IPA` が抜け落ちたくらいは問題ない：

```
sample=# select * from beers where name % 'Left of the Dial';
 key  |  abv  | ibu |  id  |         name         |    style     | brewery_id | ounces
------+-------+-----+------+----------------------+--------------+------------+--------
 1504 | 0.043 |     | 1917 | Left of the Dial IPA | American IPA |        271 |     12
(1 row)
```

`Dial` が `Dia` になっちゃっててもOK：

```
sample=# select * from beers where name % 'Left of the Dia';
 key  |  abv  | ibu |  id  |         name         |    style     | brewery_id | ounces
------+-------+-----+------+----------------------+--------------+------------+--------
 1504 | 0.043 |     | 1917 | Left of the Dial IPA | American IPA |        271 |     12
(1 row)
```

`Dial` が完全に抜け落ちていると、tri-gramに `of` や `the` を含む他のビールまでヒットするようになる：

```
sample=# select * from beers where name % 'Left of the';
 key  |  abv  | ibu |  id  |         name         |          style          | brewery_id | ounces
------+-------+-----+------+----------------------+-------------------------+------------+--------
 1047 |  0.07 |  68 | 2294 | The Power of Zeus    | American Pale Ale (APA) |        168 |     12
 1385 | 0.075 |  85 | 2159 | City of the Sun      | American IPA            |        209 |     16
 1504 | 0.043 |     | 1917 | Left of the Dial IPA | American IPA            |        271 |     12
(3 rows)
```

大文字・小文字や `Dial` のtypoくらいじゃへこたれない：

```
sample=# select * from beers where name % 'left of the daniel';
 key  |  abv  | ibu |  id  |         name         |    style     | brewery_id | ounces
------+-------+-----+------+----------------------+--------------+------------+--------
 1504 | 0.043 |     | 1917 | Left of the Dial IPA | American IPA |        271 |     12
(1 row)
```

### TSVector

自然言語として、もっと直感に即した“それっぽさ”を見たければ **TSVector** という表現が使える。

"Left of the Dial" のTSVector表現はこんな感じ：

```
sample=# select to_tsvector('Left of the Dial');
    to_tsvector
-------------------
 'dial':4 'left':1
(1 row)
```

これによって語順に依存しない、字句（トークン）の存在有無に基づく検索が可能。`of` や `the` のような stop word の除外、大文字・小文字の統一といった基本的な前処理は勝手にやってくれる。

ビール名のTSVector `to_tsvector(name)` について、`left` と `ipa` を含むものを列挙すれば期待通り "Left of the Dial" が得られる：

```
sample=# select * from beers where to_tsvector(name) @@ to_tsquery('english', 'left & ipa');
 key  |  abv  | ibu |  id  |         name         |    style     | brewery_id | ounces
------+-------+-----+------+----------------------+--------------+------------+--------
 1504 | 0.043 |     | 1917 | Left of the Dial IPA | American IPA |        271 |     12
(1 row)
```

なお、`to_tsvector() @@ to_tsquery()` は次の構文と等価：

```
sample=# select * from beers where name @@ 'left & ipa';
 key  |  abv  | ibu |  id  |         name         |    style     | brewery_id | ounces
------+-------+-----+------+----------------------+--------------+------------+--------
 1504 | 0.043 |     | 1917 | Left of the Dial IPA | American IPA |        271 |     12
(1 row)
```

残念ながらtypoはカバーできない：

```
sample=# select * from beers where name @@ 'left & daniel';
 key | abv | ibu | id | name | style | brewery_id | ounces
-----+-----+-----+----+------+-------+------------+--------
(0 rows)
```

### サウンド距離

「なんとなく覚えているけど、正確には書けない！」というときのために、システムはtypoにロバストであってほしい。ここまで見てきたのは、そのためのスペルに基づく様々なFuzzy Search手法。

一方、スペルではなく“発音の近さ”（**サウンド距離**）で検索する方法もある。

この機能は `levenshtein` のときにいれた `fuzzystrmatch` モジュールに含まれている。

`IPA`（あいぴーえー）を `ipear`（あいぺあー）と読んでみよう。 `ipear` の発音は次のように記号化される：

```
sample=# select dmetaphone('ipear'), dmetaphone_alt('ipear'), metaphone('ipear', 8), soundex('ipear');
 dmetaphone | dmetaphone_alt | metaphone | soundex
------------+----------------+-----------+---------
 APR        | APR            | IPR       | I160
(1 row)
```

明らかにtypoの域を越えているので、素のtri-gramでは何もヒットしない：

```
sample=# select * from beers where name % 'ipear';
 key | abv | ibu | id | name | style | brewery_id | ounces
-----+-----+-----+----+------+-------+------------+--------
(0 rows)
```

しかし（記号化された）**発音のtri-gram**を比較すれば：

```
sample=# select * from beers where metaphone(name, 8) % metaphone('ipear', 8);
 key  |  abv  | ibu |  id  |   name   |    style     | brewery_id | ounces
------+-------+-----+------+----------+--------------+------------+--------
   97 | 0.065 |     | 2578 | IPA      | American IPA |         35 |     12
  591 | 0.057 |  58 | 2380 | IPA #11  | American IPA |        121 |     16
  892 | 0.074 |  74 | 1777 | 2020 IPA | American IPA |        240 |     16
 1114 | 0.068 |  55 |  558 | I-10 IPA | American IPA |        527 |     12
 1192 | 0.068 |     | 2493 | I.P. Eh! | American IPA |         59 |     12
 1906 |  0.07 | 113 |   24 | 113 IPA  | American IPA |        371 |     12
(6 rows)

```

おぉーIPAめっちゃ出てくるー。

### まとめ

以上、柔軟な検索を実現するためのFuzzy Search手法たちでした。

実際のところ、RDB上でのFuzzy Searchって世の中ではどれだけ実用されているんだろうか。アルゴリズムの計算量、インデックスがどれだけ効果的に使えるか、期待する出力、etc..に応じて適切な検索手法を選択する必要があるので、なかなか難しい話題だと思う。

そして複数の手法を組み合わせたハイブリッドFuzzy Searchも可能なので、さらに悩む。"Seven Databases in Seven Weeks" では次のようなクエリが紹介されている：

```sql
select * from actors
where metaphone(name,8) % metaphone('Robin Williams',8)
order by levenshtein(lower('Robin Williams'), lower(name));
```

（Levenshtein Distance で `order by` とか絶対やりたくないけど…。）

まぁ細かいことは気にせず、みんなも思い出のビールを検索してみよう！（？）

- [fuzzystrmatch](https://www.postgresql.org/docs/9.6/static/fuzzystrmatch.html)
- [pg_trgm](https://www.postgresql.org/docs/9.6/static/pgtrgm.html)