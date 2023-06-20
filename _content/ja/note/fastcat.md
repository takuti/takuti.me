---
aliases: [/note/fastcat/]
categories: [プログラミング]
date: 2017-08-06
lang: ja
title: ローカルのRedis上でWikipediaカテゴリをシュッとdigる
lastmod: '2022-01-18'
keywords: [カテゴリ, computers, computer, ダンプ, wikipedia, mysql, 下位, hardware, データ, 上位]
recommendations: [/ja/note/recsys-2021-ab-ndcg/, /ja/note/job-title-normalization/,
  /ja/note/gensim-jawiki/]
---

Wikipediaは[APIがあったり](https://www.mediawiki.org/wiki/API:Main_page)、[データのMySQLダンプを惜しみなく公開していたりする](https://dumps.wikimedia.org/enwiki/latest/)。便利。しかし、いかんせん規模が大きいので、APIアクセスやRDBへの問い合わせに依存したデータ収集は辛いものがある。

今回はWikipediaデータの中でも、特に『カテゴリ』を効率的にdigる方法を **[fastcat](https://github.com/edsu/fastcat)** というPythonコードから学ぶ。

### ゴール

Wikipedia上の、あるカテゴリに対する上位・下位カテゴリの一覧を得る。

たとえば、英語版Wikipediaの `Computers` というカテゴリには、

- 上位カテゴリ
    - `Office equipment`
    - `Computing`
- 下位カテゴリ
    - `Computer hardware companies`
    - `Computer architecture`
    - `Classes of computers`
    - `Information appliances`
    - `Computing by computer model`
    - `Computer hardware`
    - `Computer systems`
    - `NASA computers`
    - `Data centers`
    - `Computers and the environment`

がある。

これが得られると何が嬉しいかというと、たとえばカテゴリをある種の“概念”とみなせば、上位・下位概念の獲得、概念辞書の構築に使える。また、『各カテゴリに属する記事』がダンプ [enwiki-latest-categorylinks.sql.gz](https://dumps.wikimedia.org/enwiki/latest/) から得られるので、これと組み合わせると、クラスタリングの教師データとしても使えるかもしれない。

### データ

さて、まずはこのカテゴリデータをゲットしよう。

先述の通り、カテゴリに関するMySQLダンプが公式から提供されているので、これを使えばよさそう。しかし、これはこれで相当骨の折れる仕事になりそうだ。

そこで、MySQLダンプを元に[DBpediaが独自に作成・公開](http://wiki.dbpedia.org/services-resources/documentation/datasets)している[SKOS categories データセット](http://downloads.dbpedia.org/3.9/en/skos_categories_en.nt.bz2)（※ファイル直リンク）を利用する。DBpediaはWikipediaの情報を構造的にアーカイブすることを目的としたプロジェクトで、様々なデータをRDFトリプル `<主語, 述語, 目的語>` の形で表現している。

SKOSカテゴリデータのRDFトリプルは `<カテゴリ, 関係, カテゴリ>` を表現している：

```
<http://dbpedia.org/resource/Category:Futurama> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2004/02/skos/core#Concept> .
<http://dbpedia.org/resource/Category:Futurama> <http://www.w3.org/2004/02/skos/core#prefLabel> "Futurama"@en .
<http://dbpedia.org/resource/Category:Futurama> <http://www.w3.org/2004/02/skos/core#broader> <http://dbpedia.org/resource/Category:Television_series_created_by_Matt_Groening> .
<http://dbpedia.org/resource/Category:Futurama> <http://www.w3.org/2004/02/skos/core#broader> <http://dbpedia.org/resource/Category:Comic_science_fiction> .
<http://dbpedia.org/resource/Category:Futurama> <http://www.w3.org/2004/02/skos/core#broader> <http://dbpedia.org/resource/Category:Wikipedia_categories_named_after_American_animated_television_series> .
<http://dbpedia.org/resource/Category:World_War_II> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2004/02/skos/core#Concept> .
<http://dbpedia.org/resource/Category:World_War_II> <http://www.w3.org/2004/02/skos/core#prefLabel> "World War II"@en .
<http://dbpedia.org/resource/Category:World_War_II> <http://www.w3.org/2004/02/skos/core#broader> <http://dbpedia.org/resource/Category:Wikipedia_categories_named_after_wars> .
<http://dbpedia.org/resource/Category:World_War_II> <http://www.w3.org/2004/02/skos/core#broader> <http://dbpedia.org/resource/Category:20th-century_conflicts> .
...
```

たとえば、次のトリプルは `World_War_II` の上位カテゴリ (`broader`) として `20th-century_conflicts` があることを意味する：

```
<http://dbpedia.org/resource/Category:World_War_II> <http://www.w3.org/2004/02/skos/core#broader> <http://dbpedia.org/resource/Category:20th-century_conflicts> .
```

### パース

というわけで、DBpediaが提供しているカテゴリの上下関係に関するトリプルをいい感じにパースしてあげればカテゴリの上下関係が得られる：

```py
import re
import bz2

ntriple_pattern = re.compile('^<(.+)> <(.+)> <(.+)> \.\n$')
category_pattern = re.compile('^http://dbpedia.org/resource/Category:(.+)$')

def get_name(url):
    m = category_pattern.search(url)
    return unquote(m.group(1).replace('_', ' '))

for line in bz2.BZ2File('skos_categories_en.nt.bz2'):
    # トリプルをパース
    m = ntriple_pattern.match(line.decode('utf-8'))

    if not m:
        continue

    # 主語、述語、目的語
    s, p, o = m.groups()

    # 『カテゴリの上下関係』を表していないトリプルはスキップ
    if p != 'http://www.w3.org/2004/02/skos/core#broader':
        continue

    # 主語が下位カテゴリ (narrower)、目的語が上位カテゴリ (broader) に相当
    narrower = get_name(s)
    broader = get_name(o)
```

### ローカルのRedisに保存

**[fastcat](https://github.com/edsu/fastcat)** のアイディアは、上位・下位カテゴリのlook upを効率的に行うために、パースした結果をローカルのRedisに保存しましょう、というもの。

Redisサーバを起動して、

```sh
$ redis-server /usr/local/etc/redis.conf
```

Python経由でRedisへ保存する。上位カテゴリなら `b:`、下位カテゴリなら `n:` というインデックスをつけておく：

```py
import redis

db = redis.Redis()

...

for line in bz2.BZ2File('skos_categories_en.nt.bz2'):
    ...

    narrower = get_name(s)
    broader = get_name(o)

    db.sadd('b:%s' % narrower, broader)
    db.sadd('n:%s' % broader, narrower)
```

（ローカルへのRedisのインストールはMacなら `$ brew install redis` です）

ちゃんと登録されているか見てみる：

```sh
$ redis-cli
127.0.0.1:6379> smembers 'n:World War II'
 1) "World War II sites"
 2) "People of World War II"
 3) "Military equipment of World War II"
 4) "Military units and formations of World War II"
 5) "Military logistics of World War II"
 ...
127.0.0.1:6379> smembers 'b:World War II'
 1) "Wars involving Ecuador"
 2) "Conflicts in 1943"
 3) "Wars involving Nepal"
 4) "Wars involving the Dominican Republic"
 5) "Wars involving Denmark"
 6) "Wars involving Canada"
 ...
```

一瞬でズラッとでてくる。よさそう。

### Pythonからdigる

こんな関数を作ってあげれば、コネクション `db = redis.Redis()` 経由で簡単に上位・下位カテゴリの一覧が得られる：

```py
def broader(db, cat):
    return list(map(lambda res: res.decode('utf-8'), db.smembers('b:%s' % cat)))

def narrower(db, cat):
    return list(map(lambda res: res.decode('utf-8'), db.smembers('n:%s' % cat)))
```

```py
>>> db = redis.Redis()
>>> broader(db, 'Functional programming')
['Declarative programming']
>>> narrower(db, 'Functional programming')
['Lambda calculus', 'Combinatory logic', 'Recursion schemes', 'Functional data structures', 'Functional languages', 'Implementation of functional programming languages', 'Higher-order functions', 'Dependently typed programming']
```

### 日本語版

以上がオリジナルの **[fastcat](https://github.com/edsu/fastcat)** がやっていたこと。DBpediaデータとRedisを組み合わせた、よいソリューションだと思う。研究の現場ならPDCAを加速させてくれる。やったね。

せっかくなので、これを日本語にも対応させて、パッケージ化してる： **[takuti/fastcat](https://github.com/takuti/fastcat)**

とはいえ、基本的にはデータの取得元が[日本語版SKOSカテゴリデータ](http://ja.dbpedia.org/dumps/20160407/jawiki-20160407-skos-categories.ttl.bz2)（※ファイル直リンク）に変わるだけである。日本語版DBpediaのコミュニティに感謝感謝。

幅優先でdigれば網羅的に子カテゴリを得ることができたりして便利：

```py
from queue import Queue

from fastcat import FastCat


def get_child_categories(category, max_depth=1):
    f = FastCat()

    q = Queue()
    q.put((category, 0))

    res = list()

    while not q.empty():
        cat, depth = q.get()
        if depth == max_depth:
            break

        child_categories = f.narrower(cat)
        for c in child_categories:
            q.put((c, depth + 1))

        res += child_categories

    return res
```

```py
>>> get_child_categories('関数型プログラミング', max_depth=2)
['関数型言語', '高階関数', 'ラムダ計算']
```

異常なクロールをしないことは現代人のマナーである一方、公式が提供する生データだけを馬鹿正直に使って非生産的な時間を過ごす必要もない。いい話。卒論時代の自分に教えてあげたい。