---
aliases: [/note/igo-ruby-neologd/]
categories: [プログラミング, 自然言語処理]
date: 2017-09-17
keywords: [igo, 辞書, ruby, 久しぶり, 動い, 使っ, マルコフ連鎖, vps, yootakuti, ナウく]
lang: ja
recommendations: [/ja/note/hatena-keyword-to-ipadic/, /ja/note/twitter-bot/, /ja/note/recommender-libraries/]
title: igo-rubyを新語辞書NEologdでナウい感じにする
---

『[はてなキーワードを使ってigo-ruby(MeCab)用の辞書をナウい感じにする](/note/hatena-keyword-to-ipadic/)』に4年ぶりの続編です。

**[igo-ruby](https://github.com/kyow/igo-ruby)** はJava製の形態素解析器 [Igo](http://igo.osdn.jp/) のRuby版で、4年前から動いている僕の[twitter bot](https://github.com/takuti/twitter-bot)でも使っている。

4年前の記事では『人工知能』や『ニコニコ動画』といった新語をigo-rubyでナウく分かち書きするために、Wikipediaタイトルやはてなキーワードのデータを使って独自に辞書をカスタマイズした。

今回はもっと簡単に、継続的にメンテナンスされている新語辞書 **[NEologd](https://github.com/neologd/mecab-ipadic-neologd)** を使って同様のことを実現する。もはや最近はこっちのほうが自然なアプローチですなぁ。

### NEologdのビルド

[リポジトリ](https://github.com/neologd/mecab-ipadic-neologd)を取ってきて、手順通りビルドする：

```
$ cd /path/to/neologd/mecab-ipadic-neologd
$ ./bin/install-mecab-ipadic-neologd -n
```

すると `build/mecab-ipadic-2.7.0-20070801-neologd-YYYYMMDD` といったディレクトリができる。

これが4年前の記事で自前で生成した辞書を置いた `mecab-ipadic-2.7.0-20070801` というディレクトリに対応していて、以後の手順は全く変わらない。外部データを整形して独自にコストを計算していた手間をNEologdが肩代わりしてくれた形。感謝〜。

### 辞書生成

`igo.jar` を取ってきて：

```
$ wget 'http://osdn.jp/frs/redir.php?m=jaist&f=%2Figo%2F52344%2Figo-0.4.3.jar' -O igo.jar
```

igo用辞書 `ipadic-neologd` をつくる：

```
$ java -cp igo.jar net.reduls.igo.bin.BuildDic ipadic-neologd /path/to/neologd/mecab-ipadic-neologd/build/mecab-ipadic-2.7.0-20070801-neologd-YYYYMMDD utf-8
```

オリジナルのIPA辞書のエンコーディングがEUCだったのに対し、NEologdはUTF-8であることに注意。

### ためす

```rb
require 'igo-ruby'

tagger = Igo::Tagger.new('/path/to/ipadic-neologd')

p tagger.wakati('人工知能')
# ["人工知能"]

p tagger.wakati('ニコニコ動画')
# ["ニコニコ動画"]

p tagger.wakati('10日放送の「中居正広のミになる図書館」（テレビ朝日系）で、SMAPの中居正広が、篠原信一の過去の勘違いを明かす一幕があった。')
# ["10日", "放送", "の", "「", "中居正広のミになる図書館", "」", "（", "テレビ朝日", "系", "）", "で", "、", "SMAP", "の", "中居正広", "が", "、", "篠原信一", "の", "過去", "の", "勘違い", "を", "明かす", "一幕", "が", "あっ", "た", "。"]
```

めでたい。

僕の子 @[yootakuti](https://twitter.com/yootakuti) が動いているさくらVPSから契約更新の案内が届いて、久しぶりに存在を思い出していろいろ振り返っていた次第。辞書をNEologdに変えて、久しぶりにコードを更新して賢くしてあげても良いかもしれない。[マルコフ連鎖生成用ライブラリ](https://github.com/takuti/kusari)もNEologd対応させてみたりしてね。