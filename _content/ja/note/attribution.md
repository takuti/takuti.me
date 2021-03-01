---
categories: [データサイエンス, プログラミング]
date: 2020-10-18
keywords: [winters, holt, instagram, value, facebook, 手法, マーケティング, twitter, チャネル,
  基づく]
lang: ja
recommendations: [/ja/note/holt-winters/, /ja/note/customer-centric-marketing/, /ja/note/yahoo-egads/]
title: マーケティング最適化のためのアトリビューション：単一タッチポイント全振りパターンからShapley Valueモデルまで
---

> ※『**[異常検知のための未来予測：オウム返し的手法からHolt-Winters Methodまで](/ja/note/holt-winters)**』のリミックスです。

Facebook, Twitter, Instagram, ...企業のマーケティング部門は様々なチャネルでキャンペーンを打つ。そして僕ら顧客はモバイルアプリやWeb上の様々な接点（タッチポイント）で似たような広告を目にすることになる。

さて、めでたく顧客がコンバージョン（購買、クリック、問い合わせフォームの送信、など）に至ったとして、一体どのマーケティング施策が効いたのだろうか？

「各チャネルでの接点が最終的なコンバージョンにどれだけ寄与しているか」これを数値化できれば、マーケティング担当者はそれを施策の最適化に役立てることができる。与えられた宣伝予算をFacebook, Twitter, Instagramのそれぞれにどのように配分するのがベストか、といった議論が可能になるのだ。

このように、コンバージョン履歴に基づいて各マーケティングチャネルの価値（＝KPIに対する貢献度合い）を定量的に評価するための手法が**アトリビューション**。

では具体的にどのような手法が世の中にあるのか見ていこう。

### 定番ヒューリスティクス5選

まずは、ヒューリスティクスに基づく基本的な5つの手法。

以後、次のようなコンバージョンパス `path` とその観測回数 `value` のペアが与えられるものとする：

| `path` | `value` |
|:---:|:---:|
| Twitter > Instagram | 2 |
| Facebook | 5 |
| Instagram > Facebook > Twitter | 1 |
| ... | ... |

Pythonではこんなリストをイメージしよう：

```py
conversions = [
    (('Twitter', 'Instagram',), 2),
    (('Facebook',), 5),
    (('Instagram', 'Facebook', 'Twitter', ), 1),
    ...
]
```

アウトプット（アトリビューション分析結果）として、チャネルごとに貢献度を示す何らかの値が得られるものとする：

```py
attribution = {
    'Twitter': 0,
    'Instagram': 0,
    'Facebook': 0
}
```

※参考：『[アトリビューションとは：5分でわかる意味と5つの基本モデル](https://anagrams.jp/blog/basic-of-attribution/)』

#### ラストタッチ (Last-Touch)

![last-touch](/images/attribution/last-touch.png)

最も単純なアトリビューションモデルのひとつ、コンバージョン直前のタッチポイント全振りパターン。購買直前に見たのがTwitter広告なら、そのコンバージョンは「Twitter広告のおかげ」ということになる。それまでにどんなタイミングでどんな接点を持っていようが関係ない。

```py
# Last-Touch
for path, value in conversions:
    attribution[path[-1]] += value
```

#### ファーストタッチ (First-Touch)

![first-touch](/images/attribution/first-touch.png)

ラストタッチの逆で、最初のタッチポイントに全振り。つまり第一印象ですべてが決まるという考え方。コンバージョンした人とのファーストコンタクトがInstagram上だったのなら、その後コンバージョンに至るまでにどんな広告を何回見ていようが関係なく「Instagramのおかげ」ということになる。

```py
# First-Touch
for path, value in conversions:
    attribution[path[0]] += value
```

#### 線形 (Linear)

![linear](/images/attribution/linear.png)

先の2つはさすがに過剰では・・・という見方もある。これまでの対話の積み重ねで僕らは最終的にコンバージョンに至るのだ、と。では、過去の全接点を等しく評価してあげればよいではないか。

```py
# Linear
for path, value in conversions:
    n = len(path)
    for c in path:
        attribution[c] += value / n
```

#### U字型 (U-Shape)

![u-shape](/images/attribution/u-shape.png)

とはいえ、ファーストタッチ・ラストタッチの「第一印象とコンバージョン直前の接点が特に重要だ」という仮定のほうが現実に即している感じがする。そこで、両端には特別に高い重み付けを行ってみる。

```py
# U-Shape
for path, value in conversions:
    # 接点が2回以下ならLinearと同じ
    edge_weight = 0.4 if len(path) > 2 else 0.5

    attribution[path[0]] += value * edge_weight
    attribution[path[-1]] += value * edge_weight
    
    n_intermediate = len(path) - 2
    for i in range(1, len(path) - 1):
        # 残り20%を中間接点に等しく配分
        attribution[path[i]] += value * 0.2 / n_intermediate
```

#### 時間減衰 (Time Decay)

![time-decay](/images/attribution/time-decay.png)

いやいや、第一印象なんて時間の経過とともに忘れ去られてしまうもので、重み付けを行うなら直近の印象のほうが大切に違いない！

```py
# Time Decay
for path, value in conversions:
    ordered_unique_exposure = dict.fromkeys(path)

    base = 1 / sum(range(1, len(ordered_unique_exposure) + 1))
    for i, c in enumerate(ordered_unique_exposure, 1):
        attribution[c] += i * base * value
```

タッチポイントが5回あったのなら $\sum_{i=1}^{5} i = 15$ でその重み付けは過去から順に $\frac{1}{15}, \frac{2}{15}, \frac{3}{15}, \frac{4}{15}, \frac{5}{15}$ となる。

### データに基づくアトリビューションとShapley Value

以上が最も単純なルールベースのアトリビューションモデルたち。しかし全て何らかの“極端な仮定”に依存しており、実際のコンバージョンに至るまでの振る舞いはそんなに簡単には抽象化できない、という意見もある。

そこで、現場の興味はデータ分析や機械学習、より複雑な数式を用いたモデリングに向く。

たとえばGoogle Analyticsのドキュメント "[Multi-Channel Funnels Data-Driven Attribution](https://support.google.com/analytics/answer/3191594)" で紹介されているのは、ゲーム理論における **[Shapley Value](https://en.wikipedia.org/wiki/Shapley_value)**（[シャープレイ値](https://ja.wikipedia.org/wiki/%E3%82%B7%E3%83%A3%E3%83%BC%E3%83%97%E3%83%AC%E3%82%A4%E5%80%A4)）を応用したアトリビューションモデル。噛み砕いた分かりやすい解説は『[Google 広告のデータドリブン アトリビューション(DDA)について理解してみる](https://anagrams.jp/blog/understand-data-driven-attribution-in-google-adwords/)』に譲るとして、その数式からモデルの気持ちを感じ取ってみよう。

総数 $n$ のマーケティングチャネルの集合 $N$ とその部分集合からなる取りうるチャネルの組み合わせ $S$ があるとき、あるチャネル $i$ のShapley value $\varphi_{i}$ は、与えられたチャネルの組み合わせに応じてその“価値”を数値化する関数 $v$ を用いて次のように定式化される：

$$
\varphi_{i}(v) = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|! \ \left(n-|S|-1\right)!}{n!}\left(v\left(S \cup \{i\}\right)-v\left(S\right)\right)
$$

試しにこれまで見てきた例に沿って $N = \\{ \mathrm{Facebook, Twitter, Instagram} \\}$ ($n=3$) を考えると、$N \setminus \\{i\\}$ の下で $S$ は次のようなチャネル集合となる：

- $i = \mathrm{Facebook}$ のとき $\\{\mathrm{Twitter}\\}, \\{\mathrm{Instagram}\\}, \\{\mathrm{Twitter, Instagram}\\}$
- $i = \mathrm{Twitter}$ のとき $\\{\mathrm{Facebook}\\}, \\{\mathrm{Instagram}\\}, \\{\mathrm{Facebook, Instagram}\\}$ 
- $i = \mathrm{Instagram}$ のとき $\\{\mathrm{Facebook}\\}, \\{\mathrm{Twitter}\\}, \\{\mathrm{Facebook, Twitter}\\}$

ここで、例として $v(S)$ を「チャネル集合 $S$ に対してそのコンバージョン回数の総数を返す関数」とすると、$i = \mathrm{Facebook}$ でコンバージョン履歴に `(('Twitter', 'Instagram',), 2)`, `(('Instagram', 'Twitter',), 3)`, `(('Instagram',), 1)` を含む場合：

- $v\left(\\{\mathrm{Twitter, Instagram}\\}\right) = 2 + 3 = 5$
- $v\left(\\{\mathrm{Twitter}\\}\right) = 0$
- $v\left(\\{\mathrm{Instagram}\\}\right) = 1$

となる。このとき $S$ は「チャネルの集合」を表すため、単一コンバージョンパス内での接点は順不同であることに注意。すなわち、Twitter > Instagram と Instagram > Twitter は同一視され、$v\left(\\{\mathrm{Twitter, Instagram}\\}\right)$ では両パスの“価値”が合算される。

以上を踏まえると、式の中の $v\left(S \cup \\{i\\}\right)-v\left(S\right)$ （＝チャネル $i$ を**含むとき**と**含まないとき**の $v$ の差分）は「コンバージョンパスの“価値”（先の例では“コンバージョン総数”）に対するチャネル $i$ の寄与度」を意味しているものと読むことができる。したがって、これをすべての $S$ について足し合わせれば $\sum_{S \subseteq N \setminus \\{i\\}} \left(v\left(S \cup \\{i\\}\right)-v\left(S\right)\right)$、チャネル $i$ の“価値”を数値化できそうだ。

では元の式に含まれる $\frac{|S|! \\ \left(n-|S|-1\right)!}{n!}$ は何かというと、これは平均化のための重み。コンバージョンパス内のチャネル数 $|S|$ ごとに寄与度の平均をとっている。具体的には $|S|=1$ なら、考えるのは：

- $i = \mathrm{Facebook}$ のとき $\\{\mathrm{Twitter}\\}, \\{\mathrm{Instagram}\\}$
- $i = \mathrm{Twitter}$ のとき $\\{\mathrm{Facebook}\\}, \\{\mathrm{Instagram}\\}$
- $i = \mathrm{Instagram}$ のとき $\\{\mathrm{Facebook}\\}, \\{\mathrm{Twitter}\\}$ 

以上の全3チャネル×各チャネル2通りずつで計6通りだから、先の例で $i = \mathrm{Facebook}$ の場合をみると：

$$
\frac{\left(v\left(\{\mathrm{Twitter}\} \cup \{i\}\right)-v\left(\{\mathrm{Twitter}\}\right)\right) + \left(v\left(\{\mathrm{Instagram}\} \cup \{i\}\right)-v\left(\{\mathrm{Instagram}\}\right)\right)}{3 \cdot 2}
$$

一般化すると $S \subseteq N \setminus \\{i\\}$ だから、$n-1$ チャネルから $|S|$ チャネルを取ったときの組み合わせ ${}\_{(n-1)} \mathrm{C}_{|S|} = \frac{(n-1)!}{|S|!(n-1-|S|)!}$ を全 $n$ チャネルについて考えればよくて、

$$
\begin{aligned}
\sum_{S \subseteq N \setminus \{i\}} \frac{1}{n \cdot {}_{(n-1)} \mathrm{C}_{|S|}}\left(v\left(S \cup \{i\}\right)-v\left(S\right)\right) &= \sum_{S \subseteq N \setminus \{i\}} \frac{|S|! \ (n-|S|-1)!}{n(n-1)!}\left(v\left(S \cup \{i\}\right)-v\left(S\right)\right)\\\\
&= \sum_{S \subseteq N \setminus \{i\}} \frac{|S|! \ \left(n-|S|-1\right)!}{n!}\left(v\left(S \cup \{i\}\right)-v\left(S\right)\right)\\\\
&= \varphi_{i}(v)
\end{aligned}
$$

これで冒頭のShapley Valueの計算式に帰ってきた。ここまでの直感的な理解をまとめると、Shapley Valueによるアトリビューションモデリングは「各マーケティングチャネルについて、コンバージョンパス中で他のチャネルとどの程度共起していたか」を数値化しているもの、といったイメージだろうか。

### 例

それでは実際に、5つのルールベースモデルとShapley Valueモデルがどのようなアトリビューション結果を返すのか、サンプルデータを使って見てみよう。

データはRのアトリビューションモデル実装 [ChannelAttribution](https://www.channelattribution.net/) の中で提供されているもので、全12種類のダミーチャネルからなるコンバージョンパス `path` と観測回数 `total_conversions` を含む：

```
path,total_conversions,total_conversion_value,total_null
eta > iota > alpha > eta,1,0.244,3
iota > iota > iota > iota,2,3.195,6
alpha > iota > alpha > alpha > alpha > iota > alpha > alpha > alpha > alpha > alpha,2,6.754,6
beta > eta,1,2.4019999999999997,3
iota > eta > theta > lambda > lambda > theta > lambda,0,0.0,2
...
```

各チャネルの全コンバージョンパス中の出現頻度は次の通り。

![frequency](/images/attribution/freq.png)

実験結果は [**attribution.ipynb** @ Google Colaboratory](https://colab.research.google.com/drive/1E1kd63YSiuO_8Zy0jo7uNWTMuoa3C9zf?usp=sharing) より。ここまでに紹介したアトリビューションモデルの実装は [**takuti/mtapy**](https://github.com/takuti/mtapy) にまとめた。

1ノルムで正規化したすべてのアトリビューション結果を並べたものがこちら：

![attribution](/images/attribution/attribution.png)

「なんかあんまり変わらんな・・・」というのが正直な感想なのだけど、どうだろうか。とはいえ実際のマーケティング予算最適化に適用した場合、0.01の差異でも金額としては大きな違いになるはずであり、こんなものなのだろうか。

ここから「ヒューリスティクスでも案外使い物になる」と結論づけることもできるだろうが、そのためにはより大規模なデータでの実験は不可欠だろう。

### まとめ

単一タッチポイント全振りパターンから出発して、データに基づくShapley Valueモデルまで、シンプルなアトリビューションモデルの気持ちを感じた。

データに基づく手法は沼であり、容易に複雑な方向へと拡張していくことができる。たとえば論文 "[Causally Driven Incremental Multi Touch Attribution Using a Recurrent Neural Network
](https://arxiv.org/abs/1902.00215)" ではLSTMと改良版Shapley Valueモデルの組み合わせによって時間的要素を考慮したより効果的なモデリングを試みている[^1]。

一方で『**[異常検知のための未来予測：オウム返し的手法からHolt-Winters Methodまで](/ja/note/holt-winters)**』でも書いたとおり、「このユースケースでそれって本当に必要ですか？」という議論がやっぱり大切なんだと思います。アトリビューションも、案外ここに書いてあることだけで十分かもね。

[^1]: 手前味噌ですが、最近お仕事の一環で社内リサーチチームの協力の下この論文のモデルを[実装・公開](https://github.com/treasure-data/treasure-boxes/tree/master/machine-learning-box/multi-touch-attribution)するなどしました。