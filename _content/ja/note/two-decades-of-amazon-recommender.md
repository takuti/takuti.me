---
aliases: [/note/two-decades-of-amazon-recommender/]
categories: [情報推薦]
date: 2017-06-10
images: [/images/jekyll/2014-09-01-amazon.png, /images/recommender/cf.png]
lang: ja
title: Amazonの推薦システムの20年
lastmod: '2022-01-18'
keywords: [アイテム, 推薦, 購入, 協調フィルタリング, 閲覧, amazon, ユーザ, テレビ, 商品, 本稿]
recommendations: [/ja/note/coursera-recommender-systems/, /ja/note/slim/, /ja/note/recsys-2021-ab-ndcg/]
---

[IEEE Internet Computing](https://www.computer.org/csdl/mags/ic/index.html)の2017年5・6月号に "**[Two Decades of Recommender Systems at Amazon.com](https://www.computer.org/csdl/mags/ic/2017/03/mic2017030012.html)**" という記事が掲載された。

2003年に同誌に掲載されたレポート "**[Amazon.com Recommendations: Item-to-Item Collaborative Filtering](http://ieeexplore.ieee.org/document/1167344/)**" が ***Test of Time***、つまり『時代が証明したで賞』を受賞したことをうけての特別記事らしい [^1]。

![amazon](/images/jekyll/2014-09-01-amazon.png)

「**この商品を買った人はこんな商品も買っています**」という推薦で有名なAmazonが[1998年にその土台となるアルゴリズムの特許を出願](https://www.google.com/patents/US6266649)してから20年、彼らが

- 推薦アルゴリズムをどのような視点で改良してきたのか
- 今、どのような未来を想像するのか

その一端を知ることができる記事だった。

### アイテムベース協調フィルタリング

20年前も現在も、Amazonの推薦を支えているアルゴリズムは **アイテムベースの協調フィルタリング** だ。

**協調フィルタリング** (Collaborative Filtering; CF) とは、

1. 履歴に基づいてユーザ/アイテム間の類似度を計算して、
2. 「あなたと似ている人が買ったアイテム」や「今閲覧しているアイテムと似ているアイテム」を推薦する

という手法で [^2]、たとえばレーティングを元にユーザ間・アイテム間の類似度を計算するなら次のようなイメージになる：

![Collaborative Filtering](/images/recommender/cf.png)

特に、実サービスの上では、

- ユーザ
	- 総数が物凄いスピードで **増え続ける**
	- 一人ひとりの嗜好は **日々変動する**
- アイテム
	- ユーザ数に比べるとはるかに **少ない**
	- 「一緒に買われる傾向」のようなものはある程度 **普遍的なもの**
	
といった特徴から、アイテム間の類似度を利用した協調フィルタリング、すなわち「今閲覧しているアイテムと似ているアイテム」の推薦が精度、スケーラビリティ、計算効率などの面で好まれる。これが **アイテムベースの** 協調フィルタリング。

今回『時代が証明したで賞』を受賞した記事は、まさにAmazonがこのアイテムベース協調フィルタリングについて書いたものである [^3]。

一企業が実サービス上での推薦アルゴリズムについて公表したこの記事のインパクトは計り知れず、今や多くの有名サービスが類似アルゴリズムを実装している。そして、Microsoft ResearchいわくAmazonのページビューの3割は推薦によるものであり[\[1\]](https://arxiv.org/abs/1510.05569)、Netflixがストリーミングしている動画の再生時間の8割もまた推薦によってもたらされている[\[2\]](http://dl.acm.org/citation.cfm?id=2843948) [^4] らしい。

Amazonというサービスの20年前と現在の最大の違いは、扱っている商品の種類にある。創業当時のAmazonはインターネット書店だった。それが今では生活用品から衣類、PCまでなんでも買えてしまう。そのような変化の中で、Amazonはアイテムベース協調フィルタリングをどのように改良していったのだろうか。

### “類似度”の定義

協調フィルタリングの本質は似ているユーザ/アイテムを見つけることにある。では、似ていることを測る指標・類似度をどのように定めるのか、という話になる。

『時代が証明したで賞』を受賞した記事を執筆した当時、彼らがサービスの裏側で行っていた処理は単純なものだった。それは、アイテム $X$ を購入したユーザのうち、どれだけのユーザがアイテム $Y$ も買ってくれるかという期待値 $E\_{XY}$ を、

$$
E_{XY} = |X\textrm{を買ったユーザ}| \times \frac{|Y\textrm{を買ったユーザ}|}{|\textrm{全ユーザ}|} = |X\textrm{を買ったユーザ}| \times P(Y)
$$

と計算する程度のものだったらしい。この期待値に基づいて「今閲覧しているアイテム ($X$) と似ているアイテム ($Y$)」を決定する。しかし **実際のユーザには各々にバイアス（購入傾向の偏り）があり**、この単純なモデリングでは不十分だとすぐに気がついたという。

そこで、[Amazonが2009年に出願した特許](https://www.google.com/patents/US8239287)では「**“誰が” $X$ を買ったのか**」も加味した推定を行っている。それを雑に書くと：

$$
\begin{array}{ccl}
E_{XY} &=& \sum_{c \ \in \ X\textrm{を買ったユーザ}} \left[ 1 - \left(1 -  \frac{|\textrm{全ユーザの}Y\textrm{の購入履歴}|}{|\textrm{全ユーザの全アイテムの購入履歴}|}\right)^{|c \ \textrm{の} X \textrm{以外の購入履歴}|} \right] \\ \\
&=& \sum_{c} \left[ 1 - P(Y\textrm{以外の購入})^{|c \ \textrm{の} X \textrm{以外の購入履歴}|} \right] \\ \\ 
&=& \sum_{c} \left[ 1 - P(c \ \textrm{が}Y\textrm{を一度も購入しない}) \right] \\ \\
&=& \sum_{c} P(c \ \textrm{が}Y\textrm{を少なくとも一度は購入する})
\end{array}
$$

こんな雰囲気。

たとえば「これまで $X$ しか買ったことがない！」という人がいれば、その人は $Y$ を買う見込みナシとして $E_{XY}$ には一切含まれない：

$$
P(c \ \textrm{が}Y\textrm{を少なくとも一度は購入する}) = 1 - P(Y\textrm{以外の購入})^{0} = 1 - 1 = 0 
$$

一方、$X$以外のアイテムを多く買っている人ほど、 $P(c \ \textrm{が}Y\textrm{を少なくとも一度は購入する})$ は1に近づく：
$$
\lim_{n \rightarrow \infty}  \left[ 1 - P(Y\textrm{以外の購入})^{n} \right] = 1 - 0 = 1
$$
すなわちアイテム $Y$ を高確率で買ってくれるであろうユーザとして、1に近い値が $E_{XY}$ に加算されることになる。

さらに、これだけでは単に買ったユーザが多い **人気アイテムほど $E\_{XY}$ が大きくなってしまう** ので、最終的には実測値（実際に $X$ と $Y$ を両方買ったユーザの数）$N\_{XY}$ を使って正規化しているとのこと：

- $N\_{XY} - E\_{XY}$
- $\frac{N\_{XY} - E\_{XY}}{E\_{XY}}$
- $\frac{N\_{XY} - E\_{XY}}{\sqrt{E\_{XY}}}$

・・・

このように、『似ているアイテム』を発見する方法には様々なバリエーションがあるが、万能なものは存在しない。No free lunchである。しかし同時に、**“類似”アイテムを発見する適切な方法さえ設定できれば、シンプルな協調フィルタリングという手法が実データの上で非常にうまく動く** 可能性がある。

うまく動いた例として、本稿では商品の互換性の問題を紹介している。

「このメモリカードはこのカメラで動作するのか？」

その質問に答えるためには、通常は人力での検証が不可欠だ。しかしデータが十分にあり、ひとたび類似度が適切に定められると、自然と互換性のあるアイテムが推薦上位にあがってきたらしい。アイテムに関する情報を一切与えずとも、ユーザの行動が暗にアイテムの互換性を示していたということだろう。面白い。

### 時系列の重要性

そのようなAmazon上で実際に観察された面白い傾向の中でも、**ユーザの『閲覧』と『購入』のギャップ** に関するものは、当たり前だけど特に重要な結果と言える。

いわく、本や音楽のような低価格なアイテムは閲覧したアイテムと購入したいアイテムが一致しやすい。ユーザは見たら見ただけ買ってくれる。一方、テレビのような高価なアイテムはたくさん閲覧しても、最終的に購入するのは1つだけなので、閲覧と購入の間にはギャップがある。

Amazon上でテレビをたくさん閲覧しても、最終的に購入するのは1つ。だとすれば、テレビ購入直後の推薦は特に大事にしたい。そのタイミングでは、テレビではなくBDプレーヤーなどのオプション商品を薦めるべきだ。

このような話から、ユーザの閲覧・購買行動の時系列を考慮することが重要な課題となる。

アイテムの傾向を見極める際も同様だ。『本を2冊購入した』という状況を例にとると、次のどちらのケースがより強く「この2冊は似ている」と言えるかは一目瞭然だろう：

- 最初に購入された本Aと、その数カ月後に購入された本B
- 同じ日に購入された本A, B

さらに、カメラの後にはSDカードが買われやすく、シリーズ物の漫画や小説は次巻が欲しくなるものだ。

そう、**『時間的順序』は推薦において非常に重要な役割をはたす** のだ。

時間という点では、新規ユーザへの推薦や、ライフサイクルの早いアイテム（例：アパレル商品）の推薦には cold-start 問題が付きまとう。**限られた情報の中でいかにユーザの興味、アイテムの傾向を推薦に取り入れるか**、というチャレンジがあり、ここには多くのヒューリスティクスが投入されているものと想像できる。

本稿では、

- 赤ちゃん商品を購入したユーザがいれば、その4年後には補助輪付きの自転車をオススメしてあげよう
- 本はまとめ買いの傾向があるので、一度購入したら次もしっかり関連した本を薦めよう
- 歯磨き粉のような消耗品は次の購入時期を見積もりやすいので、時期がきたらオススメしてあげよう

といった具体的なノウハウも紹介されていた。一体、こういうひとつひとつのルールをどうやって実装しているんだろうか…。

また、**どの商品がユーザの興味をモデリングするために有意義なのか** も考慮しなければならない。本やBDのようなメディア系コンテンツはユーザの興味を顕著に表す一方で、文房具のような汎用的な商品はユーザを特徴づけるとは言い難い。ホチキスを一度買っただけで文房具が大量に推薦されても困る。このバランスは難しい。

そして、ユーザの閲覧ログをみたときに「この人は絶対に新しいテレビを探しているな」と分かるのならテレビを推薦すべきだが、なにを探しているのか、なにが欲しいのか、**モチベーションがよくわからないときは推薦の多様性、セレンディピティも忘れてはいけない**。

このあたりのバランスはとても難しいので長期的な最適化が要求される。Amazonが実際にどのようなアーキテクチャ、更新頻度で推薦のモデルを組み立てているのか、もっと詳しく言及されていれば良かったけど、さすがに企業秘密か。

### 推薦の未来

本稿の最後には「推薦の未来、それは "**Recommendations Everywhere**" だ」と述べられている。

なお、Netflixも「[これからは "Everything is a Recommendation" だ](https://medium.com/netflix-techblog/netflix-recommendations-beyond-the-5-stars-part-1-55838468f429)」と似たようなことを言っているが、これは少し意図が異なる。Netflix の言う "Everything" は、**画面に表示されるコンポーネントのひとつひとつ、全てが推薦技術によってもたらされる** という意味だ。

一方、本稿の言う "Everywhere" はもっと壮大な話で、**サービスが自分のことを何でも知っていて、いたるところでパーソナライズされた情報が表示される** という未来図。まぁわかりやすく言えば「これからはAIだ」である。

自分のあらゆる行動がパラメータに反映され、まるで友達のようにサービスが自分のことを詳しく知っている未来…と書いているけど、それはもう未来でも何でもなくて、Googleが実現している現在の話だよね、とも思った。

いずれにせよ、既に成熟しているかに思われたAmazonの推薦は、やっぱり今後もどんどん進化していくのだろう。Echoのような実世界デバイスからの情報を利用すればできることも増えるしね。

### 感想

**Amazon = 協調フィルタリング** の認識はあれど、「最新のアルゴリズムはどうなのか」についてはあまり表に出ていない印象だったので、抽象的ながらもこのような形でまとめて解説してくれたのは嬉しい。

個人的に一番大事にしていることは『**情報推薦＝機械学習ではない**』という認識なので、シンプルな手法を真面目に考えて改良して、ヒューリスティクスとうまく付き合って生きている感がにじみ出ていた本稿には好感を抱く。もちろん細部では機械学習もしっかり取り入れているのだろうけど。

最近はindustryの推薦システムといえばNetflix、という風潮だけど、Amazonもこれを機にもっと詳細をいろいろ発表してくれないかな〜と思ったり。


[^1]: ちなみに、たとえば[国際会議WWWでは2015年にGoogleのPageRank論文に『時代が証明したで賞』を授与している](http://www.www2015.it/brin-and-page-win-the-first-seoul-test-of-time-award/)。
[^2]: 詳細は『[【実践 機械学習】レコメンデーションをシンプルに、賢く実現するための3か条](/note/practical-machine-learning)』『[Courseraの推薦システムのコースを修了した](/note/coursera-recommender-systems)』などを参照してください。
[^3]: 『協調フィルタリング』という表現は似たようなアルゴリズムの総称なので、この手法の考案者がAmazonというわけではない。アイテムベースなら "**[Item-based collaborative filtering recommendation algorithms](http://dl.acm.org/citation.cfm?id=372071)**" あたりがオリジナルかな。
[^4]: まぁ検索経由でNetflixの動画にたどり着くというシナリオがそもそも想像しづらいけど…。そして[Netflixは画面のすべてを“推薦”とみなしている節がある](https://medium.com/netflix-techblog/netflix-recommendations-beyond-the-5-stars-part-1-55838468f429)ので、「8割が推薦経由！」と言われてもそれほど驚く数字ではない。