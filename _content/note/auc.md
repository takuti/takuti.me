---
layout: post
title: "Area Under the ROC Curve (AUC) を実装する"
lang: ja
date: 2017-03-04
---

二値分類器の評価指標として **Area Under the ROC Curve (AUC)** がある。これは Root Mean Squared Error (RMSE) が測る『誤差』や Precision, Recall で求める『正解率』のような直感的な指標ではないので、どうもイメージしづらい。

というわけで実際に実装して「結局AUCって何？」を知る。詳しくは以下の論文を参照のこと。

- Tom Fawcett. **[An introduction to ROC analysis](http://www.sciencedirect.com/science/article/pii/S016786550500303X)**. Pattern Recognition Letters 27 (2006) 861–874.

### AUCとは結局なにを計算しているのか

サンプルに対して **0から1の範囲でスコア（確率）を与える二値分類器** の精度を評価することを考える。

このときAUCは『**予測スコアでサンプルを（降順）ソートしたときに、True Positive となるサンプルが False Positive となるサンプルより上位にきているか**』ということを測る。つまり、**ラベル `1` のサンプルに正しく高スコアを与える予測器であるか** を見ている。

[推薦などのランキング問題の評価でもAUCが登場する](https://speakerdeck.com/takuti/treasure-data-summer-internship-2016?slide=11)けど、イメージはそれとほぼ同じ。

たとえば、以下のようなソート済スコアと真のラベルのペアがあったとき、真のラベルが `1,1,1,0,0` と並ぶことが理想。しかし今は `1,1,0,1,0` となっているので、このスコアリングは最高精度とは言えない。

| 予測スコア | 真のラベル |
|:---:|:---:|
| 0.8 | 1 |
| 0.7 | 1 |
| 0.5 | 0 |
| 0.3 | 1 |
| 0.2 | 0 |

### AUCの実装 is 台形（長方形）の面積の逐次計算

この **True Positive が False Positive より上位にランキングされるか** という考えを念頭に置くとAUCの実装が理解しやすい。

具体的には、降順にソートされた予測スコア `pred` と、それらの真のラベル `label` を順に処理して、各時点での True Positive, False Positive の増分から面積を求めて加算的に計算していく。

コードにすると以下のような雰囲気。

<pre class="prettyprint lang-python">
def trapezoid(x1, x2, y1, y2):
    """与えられた長方形（台形）の面積を求める
    """
    base = abs(x1 - x2)
    height = (y1 + y2) / 2.
    return base * height


def auc(pred, label):
    """ソート済スコアとラベルのリストからAUCを求める
    """
    n = len(pred)

    a = 0.
    score_prev = float('-inf')
    fp = tp = 0
    fp_prev = tp_prev = 0

    # ソート済スコアとラベルのペアを逐次的にみていく
    for i in range(n):
        if pred[i] != score_prev:
            # True Positive (False Positive) の増分がつくる長方形の面積を加算
            a += trapezoid(fp, fp_prev, tp, tp_prev)
						
            score_prev = pred[i]
            fp_prev = fp
            tp_prev = tp

        # 現時点での True Positive, False Positive 数
        if label[i] == 1:
            tp += 1
        else:
            fp += 1

    a += trapezoid(fp, fp_prev, tp, tp_prev)
    
    # 最大面積で正規化
    return a / (tp * fp)
</pre>

やっていることを図で描くと以下のような感じ。False Positive-True Positive のグラフ上に作られる長方形の面積を足し合わせていく。

<img src="/images/auc/auc.001.png" alt="auc1" width=600 />

▲ 初期状態。そもそも ROC Curve は横軸に False Positive Rate、縦軸に False Positive Rate をとったグラフなので、AUCの計算でも False Positive, True Positive の数をそれぞれの軸にとる。

<img src="/images/auc/auc.002.png" alt="auc2" width=600 />

▲ 1サンプル目、最もスコアが高かったサンプル。`label = 1` だったので、True Positiveカウントを増やす。

<img src="/images/auc/auc.003.png" alt="auc3" width=600 />

▲ 2サンプル目。同じく `label = 1` だったので、True Positiveカウントを増やす。

<img src="/images/auc/auc.004.png" alt="auc4" width=600 />

▲ 3サンプル目。`label = 0` なので False Positive カウントを増やす。

<img src="/images/auc/auc.005.png" alt="auc5" width=600 />

▲ 4サンプル目。`label = 1` なので True Positive + 1。ここまでくると、グラフの下に長方形をみることができる。この面積は横2×縦1=2である。

<img src="/images/auc/auc.006.png" alt="auc6" width=600 />

▲ 5サンプル目は False Positive。これで最後なので、4サンプル目以降にできた大きな長方形の面積を求めると縦3×横1=3となる。つまり、ソート済みサンプルから得られた False Positive-True Positive グラフの下の面積は 2+3=5 だとわかる。

<img src="/images/auc/auc.007.png" alt="auc7" width=600 />

▲ ROC Curve は True Positive (False Positive) "Rate" を考えるので、最後に得られた面積を正規化する。今回は全部で `label = 1` のサンプルが3つ、`label = 0` のサンプルが2つあったので、最大で 縦3 × 横2 = 面積6 の長方形が得られるはず。というわけで、この場合のAUCは 5 / 6 = 0.83333 となる。

以上、これがAUCによる精度評価の内側。例えばラベルが `1,1,1,0,0` の順で来ればAUCは最高の 1.0 になって、逆に `0,0,1,1,1` の順で来れば最悪の 0.0 になる。

### まとめ

AUCによる精度評価の “気持ち” を実装しながらつかんだ。**True Positive が False Positive より上位にランキングされるか** という視点と、それを **False Positive-True Positive グラフの下の面積** に対応付けることがポイント。

ROC Analysis は[それだけでワークショップが開催できる](http://users.dsic.upv.es/~flip/ROCML2006/)くらい難しいトピックだけど、実用上はこれくらい分かっていれば十分な気がする。