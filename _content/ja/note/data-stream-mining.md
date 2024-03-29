---
aliases: [/note/data-stream-mining/]
categories: [機械学習, コンピュータシステム]
date: 2015-12-08
lang: ja
title: ストリームデータ解析の世界
lastmod: '2022-01-18'
keywords: [スケッチ, データ, 解析, ストリーム, 近似, 性質, 手法, 推定, 計算, 理論]
recommendations: [/ja/note/designing-data-intensive-applications/, /ja/note/leakage/,
  /ja/note/trends-in-real-world-recommender-systems-2017/]
---

【**[機械学習アドベントカレンダー2015](http://qiita.com/advent-calendar/2015/machinelearning)** 8日目】

**ストリームデータ解析** という分野がある。ある生成元から絶えずデータが到来する環境で、いかにそれらを捌くかという話。「時間計算量はほぼ線形であって欲しいし、空間計算量も小さく抑えつつ精度を担保したいよね」ということを考える世界。個人的に最近はそのあたりの情報を追いかけていたので、整理も兼ねてその世界を俯瞰したい。

### すごいリンク集

はじめに、この分野で外せないと思うリンクを3つ挙げておく。

#### ■ [SML: Data Streams](http://alex.smola.org/teaching/berkeley2012/streams.html)

YahooやGoogleの研究所を経てCMUの教授をしているAlex Smola先生の講義の一部（スライド＋動画あり）。理論からシステムアーキテクチャまで包括した実際的な機械学習ならこの人。この人の機械学習サマースクールの講義は[最高](http://takuti.me/note/mlss-kyoto-2015/)だった。

古典的なものから最近のものまで、代表的なアルゴリズムについて直感的な説明といい感じの理論的な解析をしてくれる。

#### ■ [Mining of Massive Data Sets](http://www.mmds.org/)

スタンフォードの大規模データ解析に関する講義ページ。質の高いスライドや本が無料で提供されていて素晴らしい。[Courseraでも開講されている](https://www.coursera.org/course/mmds)というのは知らなかったので、次に開講されたらぜひ受講したい。

本の Chapter 4 で *Mining Data Streams* を扱っていて、こちらは読み物として楽しい感じ。どういう問題を考えて、いかにアプローチするか、という部分の気持ちが伝わる。

#### ■ [Muthu Muthukrishnan, Streaming Algorithms Research](http://www.cs.rutgers.edu/~muthu/streams.html)

ラトガース大学のアルゴリズム屋さん。理論から応用まで幅広く手がけていて[dblp見ると威圧感ある](http://dblp.uni-trier.de/pers/hd/m/Muthukrishnan:S=.html)。自分のページでビートたけしの言葉を引用しているあたりも好感度高い。

2010年以前の古典的なストリームデータ処理アルゴリズムの理論的解析はこの人のサーベイ論文が優秀。

### ストリームデータとは

そもそもどのようなデータを **ストリームデータ** と呼ぶのか？

一般に、以下の性質を備えたものがストリームデータと呼ばれる。

- データが絶えず、急速に生成され続けている
- データの総量が有限ではない（無限に到来し続けるものとみなせる）
- 時間経過とともにデータの性質・傾向が変動する

Twitterのタイムラインがまさにそれで、「世界の全ツイートを対象にテキストマイニングだ！」と考えても、その作業をしている間にも新しいツイートが増え続けているので矛盾する。さらに流行り廃りで話題は時々刻々と変動するので、5年前のツイートだけを解析して「Twitterを使う日本人は皆ドロリッチが好き」と結論付けることはできない。

ゆえに、ストリームデータを解析したい場合、以下のような要求を満たす手法が欲しい。それを考えるのがストリームデータ解析という分野。

1. 時間/空間に制約がある中で近似的にデータの性質を **要約** （近似）する
	- ほぼ線形な時間計算量。
	- 小さな空間計算量で近似誤差に対して筋の良い上界を与える。
2. 入力データは既知の解析結果を更新するために利用したら捨てる （on-the-fly, single-passな手法）
3. データの性質の変動に対応できる（過去の解析結果にいつまでも引きずられない）
	- ストリームからデータをサンプリングしてランダム性も踏まえて考える。
	- データ列に対して窓幅を決めて、その単位で解析を行う。

1に関して、データの性質を限られた時間/空間で精度保証付きで近似することをデータの **スケッチ** とも呼ぶ。

（この呼び方、本当にセンスがあると思うんですよね。スケッチですよスケッチ、美術の。）

### 具体的な問題と手法

「じゃあ何をスケッチしたいのか」という話になる。データ解析といっても得たい結果は様々で、特にストリーム上の近似的なデータ解析となるとあまり凝ったことはできない。

（凝ったことを実現した上で計算量を軽くしたり、きっちりと精度の議論をするというのがこの分野の研究で一番チャレンジングな部分でもある。）

これまで考えられてきた捉えたいデータの性質には以下のようなものがある。

- 平均や分散
- 出現頻度
- サンプル間の距離（類似度）
- Cardinality

このような値が推定できればリアルタイムにストリームデータに対して意味のある処理・解析ができるよね、という想い。

具体的な手法は1900年代中盤から2015年まで、アプリケーションとしての議論も含めて様々なものが提案されているが、ここでは個人的にお気に入りの資料たちを紹介するに留めたい。

<hr>

#### ■ [今年のSIGKDDベストペーパーを実装・公開してみました | Preferred Research](https://research.preferred.jp/2013/08/sketch/)

PFNのHidoさんの記事。データのスケッチという考え方を知ったきっかけで、実装も公開されているので分かりやすい。

2013年のKDDベストペーパーになった手法 ***Frequent Directions*** は、ベクトル列なデータの基底をコンパクトなスケッチ行列で表現する手法。小さい行列に対して繰り返し特異値分解を行うアルゴリズムなので計算量はそれほど重くならないし、行列の低ランク近似の文脈で誤差解析に関する知見は豊富にあるので議論がしやすい、というのがウリ。

このアイディアの根幹は、数十年前から議論されてきたアイテムの出現頻度に関するスケッチ手法にある。

Frequent Directions のアルゴリズムはとても単純で、説明されれば「まぁ確かにそうですよね」程度の内容。「これがデータ解析戦国時代のトップカンファレンスのベストペーパーか？」という気分にもなるが、計算量や精度にシビアなデータのスケッチという文脈から出発したことによって、手堅い理論的解析ができているところが見どころなんだと思う。

<hr>

#### ■ [大規模グラフ解析のための乱択スケッチ技法](http://www.slideshare.net/iwiwi/ss-41752585)

<iframe src="//www.slideshare.net/slideshow/embed_code/key/8ciBz7oZZmN3ou" width="510" height="420" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>

iwiwiさんの資料。乱択スケッチという、データのスケッチの議論にランダム性を取り入れた考え方に関する最新事情の紹介。グラフに対するスケッチのお話は知見がなかったので新鮮だった。

Web上のデータを扱うとJaccard係数による類似度の議論は避けて通れない道であり、LSHやMinHashはそれを高速に実現する手法。派生手法がWWWでベストペーパーを取っていることからもそのアツさがうかがえる。

なお集合の類似度推定に関しては以下がわかりやすい。

[LSH (Locality Sensitive Hashing) を用いた類似インスタンスペアの抽出 - mixi Engineers&#39; Blog](http://alpha.mixi.co.jp/entry/2010/10773/)

<hr>

#### ■ [AK Data Science Summit &#8211; Streaming and Sketching &#8211;](http://research.neustar.biz/ak-data-science-summit-june-20-2013/)

2013年に開催されたストリームデータ解析やデータのスケッチに関する某集会の資料がまとまっている。事例紹介や歴史を振り返るような内容が主なのでスライドだけ見ても楽しめる。

冒頭の『すごいリンク集』で紹介した[Muthuさん](http://www.cs.rutgers.edu/~muthu/)も登壇している。

個人的にお気に入りなスライドは以下の2つ。

<div style="width: 100%;">
<script async class="speakerdeck-embed" data-id="baddb7f0c0b1013039a5220f55e8ad8b" data-ratio="1.33333333333333" src="//speakerdeck.com/assets/embed.js"></script>
</div>

▲ SQLを介してデータにアクセスする、いわゆるRelational Databaseの誕生から近年主流のスケッチ手法 HyperLogLog の紹介まで、データのCardinality推定の歴史を見ることができる感動のシナリオ。

<br>

<div style="width: 100%;">
<script async class="speakerdeck-embed" data-id="db4ecfd0c0b001309432669adddd97a5" data-ratio="1.29456384323641" src="//speakerdeck.com/assets/embed.js"></script>
</div>

▲ ツールとしてのデータのスケッチの話。最小二乗みたいなよくある問題でデータのスケッチを利用する場合の手続きとか、雰囲気を感じることができて楽しい。

### アプリケーションとしてのストリームデータ解析

先のTwitterの例からも、ストリームデータ解析がアプリケーションとしての応用可能性に富んだ分野であることは容易に想像できる。

- 検索クエリ内の頻出語の推定
- クリック履歴からの異常検知
- その他ネットワーク上のパケットのモニタリング

現実の問題で厳密解が必要なシチュエーションは少なく、スケッチ手法の応用で案外うまく動くため有名企業でも実用されていると聞く。

さらに、ストリームデータ解析手法は規模に応じてスケールすることが容易であり、センサネットワークで複数のデータ生成元から得られたセンサデータのスケッチを統合する、といったことも可能になる。

ここまで来ると、エンジニアリング的な挑戦も見えてくる。

ストリームデータを捌く基盤として **[Fluentd](http://www.fluentd.org/)** が考えられるし、[合わせて使われる](http://docs.fluentd.org/articles/cep-norikra)ストリーム処理サーバ **[Norikra](http://norikra.github.io/)** の土台となっているCEP (Complex Event Processing) はアカデミックでも議論される考え方だ。

どう？おもしろい分野でしょう？（という気持ちが伝わっていることを願います。）

### まとめ

絶えず到来するデータを高速で処理し、近似的な値によってデータストリーム全体の性質を推定する **ストリームデータ解析** という分野を紹介した。

アルゴリズムの提案と理論的解析というコンピュータサイエンスの本質的な面白さと同時に、それをアプリケーションに落とし込むエンジニアリング面での挑戦もあって最高に楽しいな、と思っている昨今。

機械学習・データマイニング系の会議ではここ数年 "Data Streams" というセッションが設けられることも珍しくなく、基礎と応用の狭間を生きる人にとっては良い選択肢なのではないかと感じる。

### よくある質問と答え

Q. つまりオンライン学習だよね？

A. はい。

（スタンフォードの大規模データ解析の資料いわく "Stochastic Gradient Descent (SGD) is an
example of a stream algorithm" とのこと）