---
categories: [情報推薦]
date: 2021-12-05
images: []
lang: ja
title: 後処理による人気アイテムの“格下げ”で確保する推薦多様性
keywords: [tail, 推薦, アイテム, long, head, short, 多様性, 論文, 指標, 後処理]
recommendations: [/ja/note/recsys-2021-ab-ndcg/, /ja/note/two-decades-of-amazon-recommender/,
  /ja/note/data-skeptic-recommender-systems/]
---

『[もしも推薦システムの精度と多様性が単一の指標で測れたら](/ja/note/recsys-2021-ab-ndcg/)』で、直近のRecSys 2021で発表された新しい推薦システムの評価指標 <!--email_off-->$\alpha\beta$-$\mathrm{nDCG@}k$<!--/email_off--> を見た。以降、引き続き推薦多様性についてサーベイしているのだけれど、どうやら僕はいきなりエクストリームな論文を読んでしまっていたらしい。

今回はもっとシンプル（だけど実用的そう）な論文 "[Managing Popularity Bias in Recommender Systems with Personalized Re-ranking](https://arxiv.org/abs/1901.07555)" @ FLAIRS 2019 について。

前提として、世の中のアイテムは「**Short-head**&mdash;常に推薦されるような超人気アイテム」「**Long-tail**&mdash;見落とされがちだけど候補として有望なアイテムたち」「**Distant-tail**&mdash;その他、有象無象と言われても仕方のないようなアイテムたち」の3種類に分類できる。

- Short-head: フィードバック（評価、クリック、購入、...）の絶対数が多いので、推薦結果にバイアスを与える。
- Long-tail: 推薦候補として至って普通のアイテムなのに、Short-headの存在によってその機会が奪われている。
- Distant-tail: 単純にフィードバックが足りていない、超不人気か新製品の類。Cold-start問題に直結する。本研究では扱わない。

“多数派”の行動を直に反映したShort-headなアイテムたちがもたらすバイアス **Popularity Bias** は、推薦結果の多様性を考える上で極めて重要な問題だ。「新しいアイテムを発見する機会がなくなる（セレンディピティの損失）」「ニッチな嗜好が推薦結果に反映されない」といった一般的なデメリットもさることながら、例えば日用品推薦の文脈で、ユーザが人種的マイノリティであったり特殊な健康状態（食事制限、アレルギーなど）にある場合はどうなるだろうか。あるいはニュース・動画などのコンテンツ推薦においては、[フィルターバブルやエコーチェンバー現象](/note/recsys-2021-echo-chambers-and-filter-bubbles/)を助長する恐れもある。

そこで本論文では、既にある推薦結果の後処理 (Post-processing) によって**アイテムの再ランキング**を行い、**精度指標を大きく損ねることなくLong-tailなアイテムを格上げする**ことを目指す。

### 問題

ある推薦アルゴリズムがユーザ $u \in U$ に対して、ランク付けされたアイテムからなる推薦リスト $R$ を生成したとする。このとき、$R$ に対して後処理を施してShort-headなアイテムを格下げすることによって、Popularity Biasを緩和した新たな推薦リスト $S$ を生成する。

ここでいう「後処理」とは、

1. 各アイテムがShort-head/Long-tailのどちらに属するかに基づいてスコアを計算し、
2. 最も「ちょうどいい」アイテムを $R$ から選んで逐次的に $S$ に加えていく

というもの。ナイーブにPythonで書き下すと次のような流れになる。

```py
def rerank(user, R, S_size):
    S = []
    for _ in range(S_size):
        candidates = [
            (score(user, item, S), idx)
            for idx, item in enumerate(R)
            if item not in S
        ]
        _, idx = max(candidates,
                     key=lambda t: (t[0], -t[1]))  # スコアが同じならオリジナルのランキングに従う
        S.append(R[idx])
    return S
```

というわけで我々の仕事は、ユーザ $u$ (`user`) とその時点までの暫定的な `S` が与えられたときに、次に「ちょうどいい」アイテムを $R \setminus S$ の中から選択するためのスコアリング関数 `score(user, item, S)` を定義することにある。

なお、論文中では $|S| < |R|$（つまり $S \subset R$ であって $S \subseteq R$ ではない）と言っているが、並び順を変えただけの $|S| = |R|$ な結果だって考えても良いハズなので、これはミスリーディングであるように思う。

### アイテムをスコアリングする

結論からいこう。先の通り、あるアイテム $v \in R$ に対する再ランキング用スコアは、その時点までに選ばれたアイテム $S$ たちに基づいて計算される。そしてこれは、Long-tail, Short-headカテゴリそれぞれに属するアイテムの集合を $\Gamma$, $\Gamma'$ としたとき、どれだけ多様性を取り入れたいかを示すパラメータ $0 \leq \lambda \leq 1$ を用いて次のように記される：

$$
\begin{array}{ccl}
\mathrm{score} &=& (1-\lambda) P(v \mid u) + \lambda \sum_{C \in \{\Gamma, \Gamma'\}} P(C \mid u) \times P(v \mid C) \times \left[\textrm{現時点で } S\textrm{ にはどの程度 }C\textrm{ が不足しているか} \right] \\
&=& (1-\lambda) P(v \mid u) + \lambda \sum_{C \in \{\Gamma, \Gamma'\}} P(C \mid u) \times P(v \mid C) \times \prod_{i \in S} \left(1 - P(i \mid C, S)\right)
\end{array}
$$

*※ 原文中では $c \in \\{\Gamma, \Gamma'\\}$ だが、アイテムの「集合」であることを明確にするため大文字 $C$ とした。*

ここで、前半の3つのパーツは次のように比較的容易に得られる：

- $P(v \mid u) = $ もともとの推薦アルゴリズムが与えたスコア（例：協調フィルタリングなら類似度に基づく予測値）。オリジナルの $R$ はこの値によってランク付けされている。
- $P(C \mid u) = $ ユーザの過去のフィードバックのうち、Long-tail/Short-headなアイテムの占める割合。ユーザの行動がアイテムの人気に素直に従っているか、それとも幅広くイロイロ触れるタイプか、を表す。
- $v \in C$ ならば $P(v \mid C) = 1$、そうでなければ $0$。

最後の「現時点での $S$ における $C$（Long-tail/Short-headカテゴリのいずれか）の**不足度**」は「現時点での $S$ における $C$ に対する**満足度** $\prod_{i \in S} P(i \mid C, S)$ 」の反対の値をとっている。そして $i \in S$ 単体がもたらす「満足感」は次の二通りで計算される：

$$
P(i \mid C, S) = \left\{ 
    \begin{array}{ll}
        \mathbb{1}_{[i \in C]} & \mathrm{(Binary)} \\
        & \\
        S\textrm{ の中で }C\textrm{ に属するアイテムの割合} & \mathrm{(Smooth)}
    \end{array} \right.
$$

### Popularity Bias からの脱却度を評価する

以上のアルゴリズムとスコアリングが提案手法。これを著者らは[MovieLens](https://movielens.org/)（映画のレーティング）と[Epinions](https://snap.stanford.edu/data/soc-Epinions1.html)（商品レビュー）の2種類のデータに対して適用し、多様性と精度 (nDCG) のトレードオフをみている。

スコア計算に際して非自明な要素は、いかにアイテムを $\Gamma$ と $\Gamma'$ に分類するかということ。今回の実験では、全レーティング・レビュー数の上位80%を占めているアイテムをShort-head $\Gamma'$、それ以外をLong-tail $\Gamma$ としている。

5分割交差検証を行い、テストユーザ集合は $U_t$ とする。再ランキング前の推薦リストは[LibRecのRankALS](https://github.com/guoguibing/librec/blob/3.0.0/core/src/main/java/net/librec/recommender/cf/ranking/RankALSRecommender.java)で生成、多様化における対抗手法は "[Controlling Popularity Bias in Learning-to-Rank Recommendation](https://dl.acm.org/doi/10.1145/3109859.3109912)"。

具体的には、あるユーザ $u \in U_t$ に対して最終的に生成された推薦リスト $L_u$ が与えられたとき、この推薦の多様性を次の3つの指標で測定する。

**Average Recommendation Popularity** (ARP):

$$
ARP = \frac{1}{|U_t|} \sum_{u \in U_t} \frac{\sum_{i \in L_u} \left[ i\textrm{ が教師データ内で評価・レビューされた回数} \right]}{|L_u|}
$$

推薦されたアイテムの平均的な「人気度」を示している。値が大きいほど強いPopularity Bias（＝悪い結果）を示唆する。

**Average Percentage of Long-Tail Items** (APLT):

$$
APLT = \frac{1}{|U_t|} \sum_{u \in U_t} \frac{|\{i \mid i \in (L_u \cap \Gamma)\}|}{|L_u|}
$$

推薦されたアイテムのうち、Long-tail $\Gamma$ に属するモノの割合。値が大きいほど多様な推薦結果が得られた（＝良い）と言える。

**Average Coverage of Long-Tail Items** (ACLT):

$$
ACLT = \frac{1}{|U_t|} \sum_{u \in U_t} \sum_{i \in L_u} \mathbb{1}_{[i \in \Gamma]}
$$

$\mathbb{1}\_{[i \in \Gamma]}$ は $i \in \Gamma$ で $1$、それ以外で $0$ をとる。

正直、この指標で著者の言いたいことがイマイチ分からない。

> *We introduce another metric to evaluate how much exposure long-tail items get in the entire recommendation. **One problem with APLT is that it could be high even if all users get the same set of long tail items**.*（原論文3ページ目）

「全ユーザの推薦リストに含まれるLong-tailアイテムが全く同じでも（その $L\_u$ に占める割合さえ十分に大きければ）APLTは良い値を示す」という主張はその通りなのだが、では上記のACLTの定式化でなぜこの問題が回避できるのかが謎。

$\sum\_{i \in L\_u} \mathbb{1}\_{[i \in \Gamma]} = |\\{i \mid i \in (L\_u \cap \Gamma)\\}|$ と読めて、結局「$L\_u$ にいくつLong-tailなアイテムが入っているか」を見ているだけなのだから解決していない気がするのだけれど・・・。評価結果のグラフ（原論文 Fig. 2 右上）を見るとACLTは小数値をとっており、一層分からない。要確認。

いずれにせよ、$\lambda$の値を動かしながら評価したところ、「精度を保ちつつ高い多様性を獲得する（高nDCG, 低ARP, 高APLT, 高ACLT）」という観点において提案手法が最良となった。また、$P(i \mid C, S)$ の計算における2つのオプションBinary, Smoothの間の比較では後者のほうが優秀だった。

### 雑感

パラメータが少なく実装も容易なので、スコア再計算にかかるコストさえ許容できればなかなか有用なアプローチであるように思う。カテゴリの定義 $C \in \\{\Gamma, \Gamma'\\}$ やユーザの行動傾向 $P(C \mid u)$ の計算はカスタマイズしやすそうだし、何より単なる「後処理」なので、既存のモデルをいじらずにワークフローに1ステップ足すだけというのが現場的には嬉しいポイントだろう。

『[もしも推薦システムの精度と多様性が単一の指標で測れたら](/ja/note/recsys-2021-ab-ndcg/)』で見た <!--email_off-->$\alpha\beta$-$\mathrm{nDCG@}k$<!--/email_off--> の研究との類似点として、この論文も情報検索における検索結果多様化の先行研究（*xQuAD;* "[Exploiting query reformulations for web search result diversification](https://dl.acm.org/doi/10.1145/1772690.1772780)"）を土台としている点が挙げられる。また、定式化に際して「現時点で満足できている（いない）アイテムカテゴリ」を重視するという点においても、核となるアイディアが共通していることは明らかだ。

他の論文をいくつか眺めた感覚としても、この「情報検索→推薦への応用」という潮流（と、継承されてしまった独特な数式の Notation）が推薦システムにおける多様性を考える上で主要な役割を担っていることは間違いなさそうだ。