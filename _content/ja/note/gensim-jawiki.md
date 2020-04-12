---
date: 2017-07-22
lang: ja
recommendations: [/ja/note/fastcat/, /ja/note/recommender-libraries/, /ja/note/incremental-plsa/]
title: gensimでWikipedia日本語版からコーパスを作ってトピックモデリング
---

しましょう。

[gensim](https://radimrehurek.com/gensim/) とは、人類が開発したトピックモデリング用のPythonライブラリです。

良記事『[LSIやLDAを手軽に試せるGensimを使った自然言語処理入門](http://blog.yuku-t.com/entry/20110623/1308810518)』のサンプルコードが少々古いので、最新版で改めてやってみる次第。

### 準備

[Index of /jawiki/latest/](https://dumps.wikimedia.org/jawiki/latest/) から **jawiki-latest-pages-articles.xml.bz2** を入手する。下手すると数時間かかる。

### コーパス

基本的には[英語版Wikipediaからコーパスを作る公式サンプル](https://github.com/RaRe-Technologies/gensim/blob/develop/gensim/scripts/make_wikicorpus.py)がそのまま使える。

我々は `gensim.corpora.WikiCorpus` が内部的に使っている分かち書き用の関数 `gensim.corpora.wikicorpus.tokenize` を日本語向けに置き換えればよろしい：

```py
import gensim.corpora.wikicorpus as wikicorpus
import MeCab


tagger = MeCab.Tagger()
tagger.parse('')


def tokenize_ja(text):
    node = tagger.parseToNode(to_unicode(text,  encoding='utf8', errors='ignore'))
    while node:
        if node.feature.split(',')[0] == '名詞':
            yield node.surface.lower()
        node = node.next


def tokenize(content):
    return [
        to_unicode(token) for token in tokenize_ja(content)
        if 2 <= len(token) <= 15 and not token.startswith('_')
    ]


wikicorpus.tokenize = tokenize
```

全貌は[gist](https://gist.github.com/takuti/356167894f454e4f28392a2cf8903b8d)にあげた。

このスクリプトを走らせて数時間待つとコーパスができる：

```
$ python jawikicorpus.py /path/to/jawiki-latest-pages-articles.xml.bz2 jawiki
```

コーパスをシリアライズするときに `metadata=True` をつけておくと、Wikipedia記事タイトルとそのインデックスのマッピングが保存できる。あとで便利なので保存しておこう：

```py
MmCorpus.serialize(dst + '_bow.mm', wiki, progress_cnt=10000, metadata=True)
```

### トピックモデリング

作成したコーパスで、LDAによるトピックモデリングを試す。

先ほど生成された `jawiki_wordids.txt.bz2`（単語-インデックスのマッピング）と `jawiki_tfidf.mm`（記事×単語の行列で要素にTF-IDF値をもつ）を読み込んで、`gensim.models.LdaModel` に渡してあげればよい：

```py
from gensim.corpora import Dictionary, MmCorpus
from gensim.models import LdaModel

dictionary = Dictionary.load_from_text('jawiki_wordids.txt.bz2')
tfidf_corpus = MmCorpus('jawiki_tfidf.mm')
lda = LdaModel(corpus=tfidf_corpus, id2word=dictionary, num_topics=100)
lda.save('lda_100.model')
```

再び数時間待つ。トピック数はテキトーに100にしたけど、たぶん少ない。

保存したモデルで遊んでみる。

モデルを読み込んで：

```py
lda = LdaModel.load('lda_100.model')
```

コーパスも読み込んで：

```py
tfidf = MmCorpus('jawiki_tfidf.mm')
```

`metadata=True` で保存した記事タイトル-インデックスのマッピングも読み込んだなら：

```py
docno2metadata = unpickle('jawiki_bow.mm.metadata.cpickle')
title2docno = {tup_title[1]: int(docno) for docno, tup_title in docno2metadata.items()}
```

夏！！！

```py
for title in ['ビール', 'カブトムシ', '海', '夏祭り']:
    topics = lda[tfidf[title2docno[title]]]
    topic = sorted(topics, key=lambda t: t[1], reverse=True)[0][0]
    print('=== %s (topic %d) ===' % (title, topic))
    for word, p_word in lda.show_topic(topic, topn=10):
        print('%.5f\t%s' % (p_word, word))
```

```
=== ビール (topic 99) ===
0.04528 植物
0.02466 料理
0.02348 栽培
0.01843 品種
0.01610 ビール
0.01584 醸造
0.01410 ワイン
0.01373 kt
0.01318 生産
0.01272 農業
=== カブトムシ (topic 46) ===
0.00462 顕微鏡
0.00352 地震
0.00339 '''()
0.00303 障害
0.00268 生育
0.00248 哲学
0.00238 発生
0.00236 意味
0.00230 効果
0.00224 患者
=== 海 (topic 32) ===
0.02139 フェリー
0.01960 航路
0.01791 就航
0.01597 運航
0.01130 建造
0.01113 船舶
0.00976 諸島
0.00939 海洋
0.00835 造船
0.00803 ハワイ
=== 夏祭り (topic 62) ===
0.01825 寺院
0.01744 日蓮宗
0.01113 神社
0.00987 文化財
0.00772 大字
0.00706 古墳
0.00676 共編
0.00670 辞典
0.00647 学区
0.00625 角川
```

（Wikipedia記事『ビール』『カブトムシ』『海』『夏祭り』が属するトピックとそのトピックワード上位10件）

`'''()` といった異物が混入している問題は、コーパス作成時に置き換えた `tokenize()` を工夫すれば解決すると思う。

保存したモデルで他のドキュメントのトピックを推定したいときは、単語-インデックスのマッピング `jawiki_wordids.txt.bz2` を使ってそのドキュメントのBag-of-Wordsを適切に表現してあげればよい。