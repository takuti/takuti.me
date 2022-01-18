---
aliases: [/note/incremental-plsa/]
categories: [情報推薦, 自然言語処理, 機械学習]
date: 2017-06-04
lang: ja
title: Q&Aサイトにおける質問推薦、そして Incremental Probabilistic Latent Semantic Analysis
keywords: [plsa, 質問, 推薦, incremental, ユーザ, 短期, 文書, negative, トピック, positive]
recommendations: [/ja/note/data-skeptic-recommender-systems/, /ja/note/trends-in-real-world-recommender-systems-2017/,
  /ja/note/two-decades-of-amazon-recommender/]
---

トピックモデリングの一手法として有名な **Probabilistic Latent Semantic Analysis (PLSA)** を incremental（逐次更新可能, オンライン型）アルゴリズムに拡張して、Yahoo!知恵袋のようなQ&Aサイトの質問推薦に応用した論文を読んだ：

- Hu Wu, et al. **[Incremental Probabilistic Latent Semantic Analysis for Automatic Question Recommendation](http://dl.acm.org/citation.cfm?id=1454026)**. RecSys 2008.

推薦システムのトップ会議 RecSys の2008年の採択論文なのでとても古く、アブストでは "web 2.0" という渋い記述も見られる。しかし、**Latent Semantic Indexing (LSI) → PLSA → Latent Dirichlet Allocation (LDA)** と発展してきたトピックモデリング業界、PLSAの研究は既に成熟しているので、比較的素直なオンライン拡張としてはこのあたりがstate-of-the-artだというのが個人的な認識。

（さらに発展的な問題設定には、[window sizeの概念を取り入れたonline PLSA](http://ieeexplore.ieee.org/document/6737290/)や、[トピック数の増減まで考えるincremental PLSA](http://dl.acm.org/citation.cfm?id=2798027)がある。）

### 概要

- PLSAを応用してQ&Aサイト上で質問推薦をしたい
- 特に、推薦アルゴリズムが incremental なら嬉しいことがいろいろあるので "incremental" PLSA を使いたい
	- 処理効率、新規ユーザへの推薦、ユーザ/アイテムデータの傾向の時間変化への適応など
- 既存の incremental PLSA と呼ばれる手法は計算量や過去のパラメータへの依存性の面でイマイチだったので、まずは新しいタイプの incremental PLSA を提案して、それを質問推薦アルゴリズムに拡張する
- 質問推薦アルゴリズムとしては、ユーザの長期的/短期的な関心の双方をモデリングできて、推薦結果に対する positive/negative なフィードバックを効果的に反映できるようなハイパーパラメータを導入したところが新しい
- 既存の incremental PLSA やバッチ版PLSAよりも良いPerplexityと推薦精度が得られて、かつ効率的

### Q&Aサイトにおける質問推薦

Yahoo!知恵袋のようなQ&Aサイトでは、ユーザを適切な質問（回答）とマッチングさせることが重要。誰でも関心のない質問には答えないし、回答に興味のない質問を見ることはない。

そのようなモチベーションから、著者たちは中国のQ&Aサイト Wenda の質問推薦機能を実装した。推薦に至るまでのフローは単純：

1. ユーザがある質問のページを閲覧する
2. 次の情報に基づいて、そのユーザにオススメの質問たちが画面に表示される
	- ユーザの質問/回答履歴
	- 閲覧中の質問

この手の推薦システムには、（というか推薦システム全般に言えることだが、）

- Incrementalなアルゴリズムである
	- 新規ユーザや新たな質問/回答が生まれるたびに推薦モデルをいい感じに更新したい
- ユーザの長期的/短期的な興味の両方を考慮したモデルである
	- 長期的な興味は普遍的なもので、ある程度履歴が溜まっていれば割り出せる
	- 短期的な興味はサイトを訪問するたびに変わりうるので、『ユーザの直近の行動』のデータを効果的に利用したい
- ユーザの positive/negative なフィードバックを両方捉えられる
	- 推薦した質問に positive なリアクション（クリックとか）があった場合、その特徴を積極的にモデルに取り込みたい
	- 逆に、ユーザが negative な反応を示したら、推薦が不適切だったものとしてモデルを修正したい

といったことが要求される。

### PLSAを応用した質問推薦

ある文書集合 $\mathcal{D}$ があったとき、PLSAでは文書データの生成プロセスを、

1. $P(d)$ に従ってある文書 $d \in \mathcal{D}$ が選択される
2. 選択された文書の潜在的なトピック $z \in \mathcal{Z}$ が $P(z|d)$ に従って決定される
3. 選択されたトピックに応じて、文書内の単語 $w \in \mathcal{W}$ が $P(w|z)$ に従って生成される

というような形でモデル化する。

EMアルゴリズムで推定されるパラメータを決定するPLSAの定式化には *Asymmetric Formulation* と *Symmetric Formulation* の2種類があり、それぞれ次のような雰囲気：

- Asymmetric Formulation
	- E-step
		- $P(z|d,w)$
	- M-step
		- $P(w|z)$
		- $P(z|d)$
- Symmetric Formulation
	- E-step
		- $P(z|d,w)$
	- M-step
		- $P(w|z)$
		- $P(d|z)$
		- $P(z)$

一般的には、LSI（特異値分解）との関連を議論しやすく、文書/単語よりはるかに少ない“トピック”に関するパラメータ $P(z)$ の推定が独立している後者が好まれていると思う。

しかし今回は特に前者の Asymmetric Formulation のほうに注目している。なぜか。

まず、質問推薦の文脈では文書＝質問文（つまり $d = q \in \mathcal{Q}$ ）になる。そして、あるユーザ $u_i$ が質問 $q_c$ を閲覧しているときに、推薦候補の全質問 $q_j \in \mathcal{Q} \setminus \\{ q_c \\}$ に対して、類似度：

- question-question similarity: $S_{q_c, q_j}$
- user-question similarity: $S_{u_i, q_j}$

を求めて、各推薦候補 $q_j$ を $S_{q_c, q_j} + S_{u_i, q_j}$ でスコアリングすることがゴールとなる。質問推薦とはすなわち、このスコアが高くなるような質問を対象ユーザに提示すること。

そして、それぞれの類似度の計算でPLSAによって得られたパラメータを利用する：

$$
S_{q_c, q_j} = \sum_z P(z|q_c) P(z|q_j)
$$

$$
S_{u_i, q_j} = \sum_z P(z|u_i) P(z|q_j)
$$

おわかりいただけただろうか。質問（文書）ごとのトピック分布 $P(z|q)$ を利用している。というわけで、EMアルゴリズムの結果として $P(z|d)$ が自然に得られる Asymmetric Formulation に限定して話を進めている（と解釈した）。

ちなみに $P(z|u_i)$、すなわち『ユーザの関心』をいかにモデリングするかという話だが、これは『ユーザが過去に回答/質問した $N_u$ 個の質問文 $\\{q_1, q_2, \cdots, q_{N_u}\\}$ 』を対象として、次のように定義している：

$$
P(z|u) = \frac{1}{N_u} \sum_{i=1}^{N_u} P(z|q_i)
$$

### Incremental PLSA への拡張

というわけで、PLSAを使うとそれっぽく質問推薦ができるので、PLSAを incremental にしてより良い推薦アルゴリズムにしましょう、という話になる。

オンライン型のPLSAアルゴリズムは過去にいくつも提案されているけど、この論文で挙げている代表的なものは3種類：

- **Fold-In**
	- PLSAの原論文で書かれている、新たな文書に対して $P(z|d)$ を得るための方法
	- 元々テストデータに対してトピックを推定するときの話なので、厳密には "incremental" とは言い難い
	- 単語についてはすべて学習済みと仮定していて $P(w|z)$ は更新されないので論外
- **IPLSA**
	- PLSAの式変形から素直に得られるオンライン拡張版
	- ちゃんと $P(z|d)$ と $P(w|z)$ の両方が更新される
	- 更新のたびにバッチ版PLSAと同じだけの計算量を要するので、重くて使いづらい
- **MAP-PLSA**
	- MAP推定に基づいて既知のPLSAパラメータを更新する手法
	- もちろん $P(z|d)$ と $P(w|z)$ の両方が更新できる
	- 計算量も IPLSA と比べると軽い
	- "But the results can also be biased, especially for $P(w|z)$" と指摘しているけど、これが具体的に何を意味しているのかいまいち読み取れなかった
		- $P(w|z)$ が過去の値に強く引っ張られてしまうという意味かな

というわけで、既存の incremental PLSA と呼ばれる手法はイマイチなので、新たなアルゴリズムを提案する。手法は Generalized EM に基づいていて、対象となる質問 $q$ に対してパラメータを次のように更新する：

#### E-step

$$
P(z|q,w) = \frac{P(z|q)P(w|z)}{\sum_{z' \in \mathcal{Z}} P(z'|q)P(w|z')}
$$

#### M-step

$$
P(z|q) = \frac{\sum_w n(q, w) \times P(z|q, w)}{\sum_{z' \in \mathcal{Z}} \sum_w n(q, w) \times P(z'|q, w)}
$$

$$
P(w|z) = \frac{\sum_q n(q, w) \times P(z|q,w) + \alpha \times P(w|z)^{(n-1)}}{\sum_{w' \in \mathcal{W}} n(q, w') \times P(z|q, w') + \alpha \times \sum_{w' \in \mathcal{W}}P(w'|z)^{(n-1)}}
$$

このとき $w$ は『質問 $q$ に含まれる単語』を意味していて、$n(q,w)$ は質問 $q$ 内の単語 $w$ の出現頻度。

$P(w|z)$ を更新するとき、正規化のために全ての単語 $w' \in \mathcal{W}$ を見ていることに注意。ただし、$w'$ が質問 $q$ に存在しなければ $n(q, w') = 0$ となる。

既存手法の問題だと指定していた（と思われる）『$P(w|z)$ が、更新しても過去の値に引っ張られる問題』については、Mステップで1つ古いパラメータ $P(w|z)^{(n-1)}$ を $\alpha$ 倍だけ取り込むという自由度を与えることで対処している。直感的には $\alpha$ が小さいほど、新しい質問 $q$ の中身を強く反映することになる。

### Incremental PLSA を取り入れた質問推薦システム

PLSAがオンラインアルゴリズムになり、トピックやユーザの関心についてのパラメータを適応的に更新する準備が整った。これを用いると、質問推薦システムの一連の挙動が次のように書ける：

1. ユーザ $u$ が新しい質問 $q$ を投稿した、または既存の質問 $q$ に回答した
	- $u$ について：
		- もし新規ユーザなら、$P(z|u)$ をランダムに初期化、正規化する
		- 既存ユーザなら、$P(z|q)$ を $P(z|u)$ で初期化する
	- $q$ 内の各単語 $w$ について：
		- もしシステムに存在しない新たな単語なら、すべての $z \in \mathcal{Z}$ について $P(w|z)$ をランダムに初期化、正規化する
2. $P(z|q)$ が収束するまで先のEMステップを回す
3. 質問 $q$ のすべての質問者/回答者 $u$ について：
	- （“新しい質問”に対する更新なら、これは投稿ユーザ1人のみ）
	- $P(z|u)$ を $P(z|u) + \beta \times P(z|q)$ で更新、正規化する

ここでポイントとなるのが Step 3。従来のPLSAを応用した質問推薦システムで $P(z|u) = \frac{1}{N_u} \sum_{i=1}^{N_u} P(z|q_i)$ と計算していた『ユーザの関心』に関するパラメータを、変化のあった質問 $q$ について重み $\beta$ で調整していることがわかる。

このようなアルゴリズムにすることで、質問推薦システムの要求を $\beta$ の調整によって満たすことができる：

- ユーザの長期的/短期的な興味の両方を考慮したい
	- 長期的に、つまりバランスよく $P(z|u)$ を設定したいなら、$\beta = \frac{1}{N_u + 1}$ にしておけばいい
	- 短期的な興味を反映したいなら、$\beta$ をそれよりも大きな値にして、注目している質問 $q$ の内容を強く反映させればいい
		- たとえば $q$ が新しい質問のときなど
- ユーザの positive/negative なフィードバックを両方捉えられる
	- $\beta$ が正の値なら、質問 $q$ に対する positive なフィードバックとしてその内容を $P(z|u)$ に反映することになる
	- 質問 $q$ に対する negative なフィードバックならば、$\beta$ を負の値にして $P(z|u)$ を更新すればよい
		- $P(z|u)$ が負になりうるので、その時は確率分布をシフトさせて正規化、などの対応が必要

### 実験

質問サイト Wenda の38375件の質問に対して Incremental PLSA を適用する。そして得られたパラメータについて：

- Perplexity
- 10人の被験者それぞれに20件の質問を推薦して relevant/irrelevant を評価してもらった結果の Precision
- 質問1つあたり、および全体の処理時間

の観点から、バッチ版PLSA、**Fold-In**、**IPLSA**、**MAP-PLSA** との比較評価を行う。

ハイパーパラメータはトピック数が64、$\alpha=0.5$、$\beta$ は positive なフィードバックのとき0.5、negative なフィードバックのとき-0.5に設定。

結果、Perplexity と Precision はいずれも提案手法が最良。処理時間はそもそも $P(w|z)$ を更新しない **Fold-In** には劣るものの、他の手法よりは短かった。

### まとめ

PLSAを質問推薦システムに応用するときの気持ちはよく伝わった。

この論文の成果としては、

- 新しい Incremental PLSA のアルゴリズムを作ったこと
- 質問推薦システムにハイパーパラメータ $\beta$ を導入したこと

の2つがある。

しかし質問推薦を対象としていない既存の Incremental PLSA たちを引き合いに出して、『これではユーザの長期的/短期的な関心を捉えられない』『positive/negativeなフィードバックの両方を反映できない』と主張している気がして、それはどうなんだ、と思った。

定式化は「Generalized EM を元にして拡張した」とだけ書かれていて、導出がブラックボックス。しかも肝心なところでタイポなのか単に記述が紛らわしいだけなのか怪しいところがあり、アルゴリズムが本当に正しいのか正直判断が付かない。

とはいえ、$\alpha$ を導入した柔軟な $P(w|z)$ の更新は Incremental PLSA 単体の研究として見て、十分価値がある話だと思う。そして実践的にはこういった自由度が大切だったりするので、[HivemallにPLSAを実装するにあたって、僕はこの手法を採用したのでした](https://github.com/apache/incubator-hivemall/pull/71)。