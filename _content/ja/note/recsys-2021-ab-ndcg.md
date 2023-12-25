---
categories: [情報推薦]
date: 2021-11-17
images: []
lang: ja
title: もしも推薦システムの精度と多様性が単一の指標で測れたら
lastmod: '2022-01-18'
keywords: [アイテム, 推薦, 評価, aspect, ランキング, カテゴリ, 指標, 好む, ユーザ, 結果]
recommendations: [/ja/note/reranking-for-popularity-bias/, /ja/note/data-skeptic-recommender-systems/,
  /ja/note/two-decades-of-amazon-recommender/]
---

RecSys 2021採択論文の中で気になっていた "[Towards Unified Metrics for Accuracy and Diversity for Recommender Systems](https://dl.acm.org/doi/10.1145/3460231.3474234)" を読んだ。

独特かつ曖昧な表記の数式が並ぶ「読んでいてイライラするタイプの論文」ではあったものの、推薦結果の *Relevance*（履歴に基づく類似度；古典的な“精度”に直結）と *Novelty*（ユーザにとっての推薦結果の新規性・多様性；セレンディピティに寄与）を相互に検討する際の論点、手法に求められる性質、実験のフレームワークのリファレンスとして有用な研究であるように思う。

一方、提案手法の筋の良さ、およびその実用性は疑わしい。定義の曖昧なパラメータを内在し、データに関して十分に事前知識のあるオフラインでの性能評価にユースケースを限定しているためだ。

いずれにせよ「精度の先にある、ユーザ本位で構築・評価される推薦システム」という業界のトレンドを反映した研究であることは確かであり、ざっくりと目を通しておいて損はないだろう。

> After taking a quick look at the list of accepted papers, for me, one of the biggest trends in 2021 is **user-centricity**, which focuses on how to allow users to intervene in a recommendation process while minimizing the risk of biases and maximizing diversity & fairness of recommendations.<br/><br/>*[User-Centricity Matters: My Reading List from RecSys 2021](/note/recsys-2021/)*

### 導入

Top-$k$アイテム推薦において、その結果の精度と多様性を同時に測るための新たな評価指標 <!--email_off-->$\alpha\beta$-$\mathrm{nDCG@}k$<!--/email_off--> を提案する。

議論の起点となるのは、 *Item aspect* という“カテゴリ”に相当する概念。あるアイテム $i$ は、1つ以上の Aspect $a\_{\phi}$ に紐付く。そして“良い”推薦結果というものを定義するにあたって、マクロな視点で「カテゴリ単位で、推薦結果全体がユーザにもたらす満足度」の定量的表現を検討する、というのが本論文の仕事であると言える。

なお提案手法は、情報検索における検索結果の多様化に関する議論 "[Search Result Diversification](https://dl.acm.org/doi/10.1561/1500000040)" を土台としている。

### 精度と多様性を兼ね備えた“良い”推薦結果とは？

ユーザの嗜好を過不足なくモデリングしつつ、アウトプットにはある程度の多様性を取り入れる&mdash;そのような「いいとこ取り」な推薦システムの構築を目指す場合、その良し悪しを定量的に評価するための指標は次の8つの性質を的確に捉えるべきである、と著者は言う。

1. **Priority Inside Aspect**: ある2つのアイテムの属するカテゴリ群が同一であれば、ユーザがより高評価を付けた（付けうる）アイテムがランキング上位で推薦される。
2. **Deepness Inside Aspect**: よりユーザの関心にマッチしているアイテムほど、ランキング上位にまとまって推薦されれる（必要以上に下位まで分散させない）。
3. **Non Priority on Saturated Aspect**: ユーザは、ある特定のカテゴリに属するアイテムを既に十分見せられた後で新たに2つのアイテムが提示された場合、（たとえ過去に低評価をつけていても）見飽きていない方のカテゴリと紐付くアイテムを好む。
4. **Top Heaviness Threshold**: ユーザは、興味にマッチするアイテムをランキング上位でピンポイントに見つけたい。興味があるからといって、ダラダラと似たような傾向のアイテムばかりが並ぶランキングを見たいわけではない。
5. **Top Heaviness Threshold Complementary**: ユーザに提示するアイテムの総数は多すぎないこと。ランク付けされた推薦結果を1位から最下位まですべて見るほど、彼ら・彼女らも暇ではない。
6. **Aspect Relevance**: ユーザはカテゴリ (Aspect) 単位で好みがあって、仮に2つのアイテムの両方が好きだったとしても、より好むカテゴリと紐付く方をより一層好む。
7. **Prefer More Aspect Combination**: ユーザは、ある2つのアイテムが等しく興味とマッチしている場合、これまでの推薦結果を振り返ってまだ十分に満足できていないカテゴリに属するアイテムをより一層好む。
8. **Missing Over Non-Relevant**: ユーザは、明らかに低評価をつける（自分は既にそれが嫌いであると知っている）アイテムよりは、全く見たことのない未知のアイテムを好む。

そして <!--email_off-->$\alpha\beta$-$\mathrm{nDCG@}k$<!--/email_off--> は上記すべての性質を定量的に評価することのできる指標である&mdash;すなわち性質を満たす推薦結果には高い値を、そうでない場合は低い値を返す&mdash;と。

いかにも都合よく並べられた仮定であるように思えるが、「精度の最大化だけを目的にスコアリング/ソートされたような、冗長で“つまらない”推薦結果は評価しない」という主張には共感する。

### <!--email_off-->$\alpha\beta$-$\mathrm{nDCG@}k$<!--/email_off--> の気持ち

では『提案手法』である <!--email_off-->$\alpha\beta$-$\mathrm{nDCG@}k$<!--/email_off--> とは一体どのようなものなのか。

Top-$k$ランキング推薦における評価指標 [Normalized Discounted Cumulative Gain](https://en.wikipedia.org/wiki/Discounted_cumulative_gain) (nDCG) とは、あるランク $1 \leq j \leq k$ における推薦の“質” (Gain) が $G\_j$ で与えられるとき、$G\_1, G\_2, \cdots, G\_j, \cdots, G\_{k - 1}, G\_k$ を総合的にみて次のように定量的な評価を与えるものである：

$$
\mathrm{nDCG@}k = \frac{\mathrm{DCG}_k}{\mathrm{IDCG}_k} = \frac{\sum_{j=1}^{k} G_j / \log_2(1+j)}{\mathrm{IDCG}_k}
$$

正規化係数 $\mathrm{IDCG}_k$ には近似解が用いられるわけだが \[[参考](https://takuti.github.io/Recommendation.jl/latest/evaluation/#Recommendation.NDCG)\]、それはさておき、nDCG の言う "Gain" の定義は一意ではなくカスタマイズの余地が残されているという点がキモだ。

というわけで本論文の仕事はつまるところ、精度と多様性を同時に数値化してくれるような独自の $G\_j$ を定義することにある。

先述の通り、僕らはユーザ $u$ の Aspect（カテゴリ）$a\_{\phi}$ に対する興味・関心をモデリングすることによって、推薦結果をマクロなレベルで評価・最適化したい。というわけで具体的には、次に示すような「$1, 2, \cdots, k-1$ 番目までランク付けされた推薦アイテム列 $i\_1, i\_2, \cdots, i\_{k-1}$ が与えられた時、$k$ 番目のアイテムとして $i$ がふさわしい確率」によってその推薦の“良さ”を判断する：

$$
1 - \prod_{\phi} \left( 1 - P\left(a_{\phi}\textrm{ への興味が満たされる} \mid u, i\right) \times P\left(i \textrm{ に } a_{\phi} \textrm{ であることを望む} \mid u, i_1, i_2, \cdots, i_{k-1} \right) \right)
$$

そして、この確率をTop-$k$推薦結果の "Gain" $G\_k$ とみなして nDCG の定式化に当てはめてあげよう、という発想になる。

ここで $P\left(a\_{\phi}\textrm{ への興味が満たされる} \mid u, i\right) = P(a\_{\phi} \mid u,i)$ は「あるアイテム $i$ が ユーザ $u$ の $a\_{\phi}$ への興味を満たすのにどれだけ貢献しているか」を表しており、アイテムに対する直接的な評価値 $r\_{u,i}$ を用いて次のように計算される：

$$
P(a_{\phi} \mid u,i )=\left\{ 
    \begin{array}{ll}
        0 & (i\textrm{ は }a_{\phi}\textrm{ に紐付かない}) \\
        \alpha(u,i) & (i\textrm{ は }a_{\phi}\textrm{ に紐付くが }r_{u,i} \textrm{ は未観測}) \\
        r_{u,i} / r_{\mathrm{max}} \times \beta(u) & (i\textrm{ が }a_{\phi}\textrm{ に紐付いて }r_{u,i}\textrm{ も分かっている}) 
    \end{array} \right.
$$

$\alpha(u,i)$ はユーザ・アイテムペアから想定される適当な値であり、論文中では小さな定数としている。$r\_{u,i}$ がわからない（＝事前知識が限られている）ためのナイーブな対応ではあるが、ユーザまたはアイテムの大域的なプロファイリングによって、より意味のある重み付けをすることは十分可能だろう。

$\beta(u)$ はユーザの評価の確度（どれだけ評価値が信用できるか；どれだけ評価がブレるか）を示すパラメータ。この値の最適化も、残念ながら著者は Future Work としている。

このように、Gain の計算に $\alpha$, $\beta$ という2つのパラメータが含まれる独自の nDCG であるから、提案手法を <!--email_off-->$\alpha\beta$-$\mathrm{nDCG@}k$<!--/email_off--> と呼んでいる。

先の確率の推定に至るまでの式変形は正直追いきれていない部分もあるため、ここでは著者プレゼンテーションのスライドを引用するに留めたい。

![ab-ndcg](/images/recsys-2021-ab-ndcg/formulation.png)

_\* "[Towards Unified Metrics for Accuracy and Diversity for Recommender Systems](https://dl.acm.org/doi/10.1145/3460231.3474234)"プレゼンテーション動画よりキャプチャ・引用。_

### いかにして「多様性」を測るか

「多様性」または「セレンディピティ」について議論することは難しい。過去に『[Podcast "Data Skeptic" の推薦システム回が良すぎて3回聞いた](/ja/note/data-skeptic-recommender-systems/)』でも触れたように **Serendipity = like + didn't expect** であり、単純に奇をてらった推薦をしたらセレンディピティかというと、そういう話でもない。

先に挙げた性質その1 "**Priority Inside Aspect**"、その2 "**Deepness Inside Aspect**" が暗に語っているように、ユーザの好みを適切にモデリングした推薦結果であることは大前提だ。その上で、どこまで「好み」という直接的なフィードバックのみに忠実に従うべきか、という“程度”に関する問題なのだ。

提案された評価指標において、その“程度”をコントロールするために重要な役割を果たしているのが $\beta(u)$ の存在だ。これによりシステムは「ユーザが過去に高評価を付けたアイテムは全て良い」という短絡的な思考に陥らずに済む。

たとえば映画の5段階評価 $(r\_{\mathrm{max}} = 5)$ で $i=$『鬼滅の刃』に★4をつけていた人 $u$ がいたとする。でも僕らは、この人の評価はジャンルに依らず結構ブレる（≒ジャンル問わず興味の幅が広い）と知っているので、信頼度は低めに見積もって $\beta(u)=0.2$ としよう。そのとき、映画『鬼滅の刃』に対する評価がこの人の $a\_{\textrm{アニメ}}$ 欲を満たすのにどれだけ貢献しているのかといえば、それは微妙で $r\_{u,i} / r\_{\mathrm{max}} \times \beta(u) = 4/5 \times 0.2 = 0.16$ となる。逆に、評価に一貫性のある人ならば、たとえば $\beta(u)=0.9$ として $4/5\times 0.9 = 0.72$ であり、『鬼滅の刃』はそれだけでこの人のアニメ映画欲をかなり満たしてくれるといえる。

改めて Item aspect の定義に戻ると、ひとつのアイテムに対して複数の $a\_{\phi}$ を取りうるので、『鬼滅の刃』がもたらす満足度は $P(a\_{\textrm{アニメ}} \mid u,i )$ だけでなく $P(a\_{\textrm{ファンタジー}} \mid u,i )$ や $P(a\_{\textrm{フィクション}} \mid u,i )$ などによっても測られることに注意したい。

先の定式化における第一の確率 $P(a\_{\phi} \mid u,i)$ は、この（正規化された）「重み付き評価値」をダイレクトに用いている。ゆえにこの確率は、アイテム評価値とカテゴリ別満足度を相互に見つつ、推薦結果の *Relevance*（精度）を測る役割を担っているといえる。

他方、第二の確率 $P\left(i \textrm{ に } a\_{\phi} \textrm{ であることを望む} \mid u, i\_1, i\_2, \cdots, i\_{k-1} \right)$（先のキャプチャ画像中の $P(a\_{\phi}\mid u,S)$；$S$ はランク付けされたアイテム列 $i\_1, i\_2, \cdots, i\_{k-1}$ ） では *Novelty*（新規性・多様性）を測っている。この確率の定式化には先の「満足度」とは反対の値が組み込まれていて、「$k-1$個の映画を見てもまだ満足できていないカテゴリ」を重視する：

$$
\prod_{\ell=1}^{k-1} \left( 1 - P(a_{\phi} \mid u, i_{\ell}) \right)
$$

先の例で言えば、$j=1$で既に『鬼滅の刃』をオススメしていたとしても、$P(a\_{\textrm{アニメ}} \mid u,i\_1 ) = 0.16$ と低い値を示しているのであれば、たとえ多様性を考慮したとしてもまずは引き続き $a\_{\textrm{アニメ}}$ をオススメしたい、という話になる。したがって、たとえば同カテゴリに紐付く映画『呪術廻戦』は $j=2$ でも有望な候補となりうる。一方、仮に $\beta(u)=0.9$ で $P(a\_{\textrm{アニメ}} \mid u,i\_1 ) = 0.72$ であった場合、$j=2$ 以下、より早い段階で「もうアニメは十分です」というタイミングが訪れ、過度なアニメ映画の推薦は <!--email_off-->$\alpha\beta$-$\mathrm{nDCG@}k$<!--/email_off--> の低下に直結する。

### ランキング評価指標を評価する

新たなランキング評価指標をいかに評価するか。本論文が行った実験は次の三種類：

1. 推薦結果の順位（ランク）を無理やり変えた時に、評価指標はどのような値を示すか
2. ランキング内での大小様々な順位変化をどれだけ差別化して捉えられるか
3. テストデータを減らした時に、指標が過度に反応しないか

例えばTop-$k$推薦結果の1位と$k$位を入れ替えて評価させてみる。このとき、<!--email_off-->$\alpha\beta$-$\mathrm{nDCG@}k$<!--/email_off--> はきちんと反応して低下すべきである。それもできるだけ敏感に、顕著に。

推薦されたアイテムの順番を“あえて”入れ替えるという話を聞くと、2017年のGroupLensの研究 "[Cycling and Serpentining Approaches for Top-N Item Lists](https://dl.acm.org/citation.cfm?id=2998211)" を思い出す。

<iframe src="//www.slideshare.net/slideshow/embed_code/key/zjZEohHOa3yb9U" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/QianZhao12/toward-better-interactions-in-recommender-systems-cycling-and-serpentining-approaches-for-topn-item-lists" title="Toward Better Interactions in Recommender Systems: Cycling and Serpentining Approaches for Top-N Item Lists" target="_blank">Toward Better Interactions in Recommender Systems: Cycling and Serpentining Approaches for Top-N Item Lists</a> </strong> from <strong><a href="https://www.slideshare.net/QianZhao12" target="_blank">Qian Zhao</a></strong> </div>

「ご丁寧に上から順番に、明らかに高評価をつけるようなアイテムが列挙されていても退屈だ」という課題意識は <!--email_off-->$\alpha\beta$-$\mathrm{nDCG@}k$<!--/email_off--> の研究のモチベーションと類似している。

ミネソタ大学の研究はMovieLensサイト上でのオンライン評価を中心に議論が展開されていたが、このような実アプリケーションを <!--email_off-->$\alpha\beta$-$\mathrm{nDCG@}k$<!--/email_off--> で評価した時にどのような知見が得られるのかは大変興味深い。

その点において、やはり今回紹介した論文が「オフラインでの精度評価」に議論を限定してしまっている点が個人的にはとても惜しい。後続研究に期待である。

### 雑感

というわけで、精度と多様性を統合した新しい推薦システム評価指標 <!--email_off-->$\alpha\beta$-$\mathrm{nDCG@}k$<!--/email_off--> を見た。冒頭にも述べたとおり、推薦結果の多様性という漠然とした問いに対して「“良い”ランキング推薦結果とはどのようなものか」を慎重に考え直すことによって立ち向かう、時代を反映した有意義な論文であったように思う。

しかし、そもそも精度と多様性を統合した単一の指標というものが本当に必要なのだろうか？

実験・評価用途であれば、精度指標 (Precision, Recall, nDCG) に加えて（比較的ナイーブな、独自の定義の下に）Novelty, Diversity も別途測定している研究は多数存在する。両者は常にトレードオフの関係にあるので、この場合は最終的には「手法Aは Precision が物凄く良いけれど、Diversity は手法Bに劣る」みたいな議論が展開される。これは <!--email_off-->$\alpha\beta$-$\mathrm{nDCG@}k$<!--/email_off--> として両者を畳み込んでしまった後ではおそらく困難な議論だ。

また、推薦アルゴリズムの学習に（損失関数として）用いるには明らかに議論が不足している。これは、Learning to Rank を始めとするランキング最適化手法の大衆化に伴い特に重要になっている視点だ。そもそも $\alpha$ や $\beta$ といったパラメータの値すら曖昧なのだ。なにをもって「最適な <!--email_off-->$\alpha\beta$-$\mathrm{nDCG@}k$<!--/email_off-->」とするかは未だ自明ではない。

新しいパラメータを導入して作られた「わたしのかんがえたさいきょうの○○」は、ユースケースを限定してカリカリにチューニングされた状況下では良いのかもしれないが、そうでなければ議論をややこしくするだけの恐れもある。あなたにとっての「良い推薦システム」の定義はなんですか？まずはそんな根本的な問いについて今一度本気を出して考えてみることが、いまを生きる研究者・開発者には求められているのかもしれない。