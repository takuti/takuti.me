---
aliases: [/note/auc-parallel/]
categories: [機械学習]
date: 2017-03-10
lang: ja
title: Area Under the ROC Curve (AUC) を並列で計算するときに気をつけること
lastmod: '2022-01-18'
keywords: [マージ, auc, 面積, 'true', 並列, プロセス, positive, 結果, サンプル, ソート]
recommendations: [/ja/note/auc/, /ja/note/adjusting-for-oversampling-and-undersampling/,
  /ja/note/td-intern-2016/]
---

### 追記 (2017/03/10)

現在の内容は過度な簡略化と不完全な説明を含むので、それを踏まえて読んでいただけると幸いです。（後日更新予定）

https://twitter.com/myui/status/840089982991708160

---

ひとつ前の記事で二値分類器の性能評価に用いられる **Area Under the ROC Curve (AUC)** の実装について書いた: [Area Under the ROC Curve (AUC) を実装する](/note/auc/)

簡単にまとめると、

- AUCは『予測器がラベル `1` (True) のテストサンプルに正しく高スコアを与えるか』をみる。
- それは予測スコアでサンプルをソートしたときに True Positive が False Positive より上位にランキングされるか、ということ。
- 実装する際はソート済みサンプル列を逐次的に見ていって、False Positive-True Positive グラフの下の面積を求める。

という話だった。

<img src="/images/auc/auc.007.png" alt="auc7" width=600 />

### AUC in Hivemall

そして先日、Hive/Spark/Pig用の並列機械学習ライブラリ[Hivemall](https://hivemall.incubator.apache.org/)にAUCを計算する関数を実装した。

https://twitter.com/ApacheHivemall/status/836526293927657472

実装にあたりAUCをMap-Reduceの枠組みの中で並列に計算する必要があった。

たとえば2並列の場合を考えると、プロセス1と2でソート済みサンプルを分担することになる。

|プロセス| 予測スコア | 真のラベル |
|:---:|:---:|:---:|
|1| 0.8 | 1 |
|1| 0.7 | 1 |
|1| 0.5 | 0 |
|2| 0.3 | 1 |
|2| 0.2 | 0 |

しかし先述の通りAUCの実装はソート済みサンプルを**逐次的に**見ていく（つまり1つ前の結果に依存する）ので、気をつけて実装しないと誤った結果になってしまう。

### マージするときに長方形を底上げする

図で考えよう。先の例で各プロセスがTrue Positive, False Positiveカウントを独立して計算すると次のようになる。

<img src="/images/auc/auc-partials.png" alt="auc-partials" width=400 />

この2つの結果をマージしたいとき、単に両者の面積を足して 2+1=3 とはなりませんよ、というのが問題。正しいマージ後の面積は冒頭の図にある通り 5 になる。

より具体的に、プロセス1の結果（マージ元）をプロセス2の結果（マージ先）にマージする場合を考える。このとき、補足情報としてマージ元のTrue Positiveのカウントをマージ先に教えてあげる。これがポイント。

すると、マージ先ではマージ元の長方形の分だけ面積を底上げをすることができて、正しい面積が得られる。

<img src="/images/auc/auc-merge.png" alt="auc-merge" width=300 />

▲ こんな感じ。あとは『マージ元の面積』と『マージ先の底上げした面積』の和を求めて正規化すれば、それが正しいAUCとなる。

ちなみに実際のHivemallのマージ部分の実装は[ここにある](https://github.com/apache/incubator-hivemall/blob/master/core/src/main/java/hivemall/evaluation/AUCUDAF.java#L251-L282)。マージ元とマージ先が逆の場合にも対応できるように他の補足情報も渡しているけど、基本的な考え方は上記のものと変わらない。

### まとめ

計算の前後に依存関係がある処理の並列化は往々にして困難だけど、AUC計算は長方形の面積の足し合わせという単純な処理なので少し補足情報を渡してあげるだけで並列実装も可能。

ただし、マージ元とマージ先が隣接していないとダメな点に注意。たとえば以下のように3並列で計算した場合、プロセス1と3の結果を先にマージする、ということはできない。

|プロセス| 予測スコア | 真のラベル |
|:---:|:---:|:---:|
|1| 0.8 | 1 |
|1| 0.7 | 1 |
|2| 0.5 | 0 |
|2| 0.3 | 1 |
|3| 0.2 | 0 |

すなわち、

- 1と2の結果をマージ → それと3の結果をマージ
- 2と3の結果をマージ → それと1の結果をマージ

このいずれかの順序でマージされる必要がある。むずかしい。