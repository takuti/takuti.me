---
aliases: [/note/levenshtein-distance/]
categories: [プログラミング, 自然言語処理]
date: 2017-07-28
keywords: [編集, 距離, 文字列, 文字, 置換, levenshtein, distance, クラスタリング, title, job]
lang: ja
recommendations: [/ja/note/postgresql-fuzzy-search/, /ja/note/job-title-normalization/,
  /ja/note/algorithmic-marketing/]
title: いまさら編集距離 (Levenshtein Distance) を実装するぜ
---

ある文字列Aに対して『1文字の追加・削除・置換』を何回繰り返せば他の文字列Bになるか。このときの最小回数を、文字列A, B間の[編集距離 (Levenshtein Distance)](https://ja.wikipedia.org/wiki/%E3%83%AC%E3%83%BC%E3%83%99%E3%83%B3%E3%82%B7%E3%83%A5%E3%82%BF%E3%82%A4%E3%83%B3%E8%B7%9D%E9%9B%A2)と呼ぶ。

- **花火** から **火花** までの編集距離は各文字の置換なので 2
- **クワガタ** から **カブトムシ** までの編集距離はなんかもう全文字違うので総入れ替え＆文字『シ』の追加で 5

この編集距離、文字列の“類似度”と見ることができて、なかなか便利な子である。『[Job Titleの前処理＆クラスタリングをどうやって実現するか問題](/note/job-title-normalization)』では、人々の肩書きを編集距離を使って前処理（クラスタリング）している事例も紹介した。

さて、ここでは Levenshtein Distance を求めるアルゴリズムを実装して、備忘録として書き留めておく。ネット上にも多数の解説記事があり「今更ァ？」という話だが、正直どれを読んでもピンとこなかったのだ。

### アルゴリズム

動的計画法 (DP) です。おわり。

Wikipedia に書かれている擬似コードをそのまま実装すると次のような感じ：

```py
def levenshtein(s1, s2):
    """
    >>> levenshtein('kitten', 'sitting')
    3
    >>> levenshtein('あいうえお', 'あいうえお')
    0
    >>> levenshtein('あいうえお', 'かきくけこ')
    5
    """
    n, m = len(s1), len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i

    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,         # insertion
                           dp[i][j - 1] + 1,         # deletion
                           dp[i - 1][j - 1] + cost)  # replacement

    return dp[n][m]
```

二次元配列 `dp` の中身は、たとえば `levenshtein('kitten', 'sitting')` を実行した後だと：

```
   |  -  s  i  t  t  i  n  g
----------------------------
 - |  0  1  2  3  4  5  6  7
 k |  1  1  2  3  4  5  6  7
 i |  2  2  1  2  3  4  5  6
 t |  3  3  2  1  2  3  4  5
 t |  4  4  3  2  1  2  3  4
 e |  5  5  4  3  2  2  3  4
 n |  6  6  5  4  3  3  2  3
```

### 理解

たとえば、この `4` は、文字列 `ki` から `sitti` までの編集距離を意味する：

```
   |  -  s  i  t  t  i  n  g
----------------------------
 - |                 .
 k |                 .
 i |  .  .  .  .  .  4
 t |
 t |
 e |
 n |
```

アルゴリズムでは、まず `dp` を次のように初期化する：

```
   |  -  s  i  t  t  i  n  g
----------------------------
 - |  0  1  2  3  4  5  6  7
 k |  1
 i |  2
 t |  3
 t |  4
 e |  5
 n |  6
```

空文字列から `sitting` のx文字目までの編集距離と、`kitten`のy文字目から空文字列までの編集距離。これは自明。

そして空白をうめていく。`k`（`kitten`の一文字目）と`s`（`sitting`の一文字目）の編集距離、つまり X (= `dp[i][j]` ) の値はなにか：

```
           (j)
      |  -  s  i  t  t  i  n  g
   ----------------------------
    - |  0  1  2  3  4  5  6  7
(i) k |  1  X
    i |  2
    t |  3
    t |  4
    e |  5
    n |  6
```

最初に書いたとおり可能な操作は『1文字の追加・削除・置換』で、`dp[i][j]`に隣接する既知の編集距離から：

|| 既知の編集距離（文字列A→B） | 操作 (+1) | 得られる編集距離 ||
|:--:|:--:|:--:|:--:|:--:|
|`dp[i-1][j]` | '-'（空文字列）→ 's' | 文字列 A '-' に 'k' を**追加** ( → 's' ) | 'k' → 's' | `dp[i][j]` |
|`dp[i][j]` | 'k' → 's' | ( 'k' → ) 文字列 B 's' から 's' を**削除** | 'k' → '-' | `dp[i][j-1]` |
|`dp[i-1][j-1]` | '-' → '-' | 文字列 A の次の文字 'k' を 's' に**置換** | 'k' → 's' | `dp[i][j]` |

つまり、

- `dp[i-1][j]` と `dp[i][j]` の差は**追加**操作1回分
- `dp[i][j]` と `dp[i][j-1]` の差は**削除**操作1回分
- `dp[i-1][j-1]` と `dp[i][j]` の差は**置換**操作1回分

とわかる。

ただし、置換操作は文字列 A と B の次の文字が既に一致していれば『何もしない』。すなわち、編集距離として `dp[i-1][j-1]` と `dp[i][j]` は等しくなる。

以上が

```py
cost = 0 if s1[i - 1] == s2[j - 1] else 1
dp[i][j] = min(dp[i - 1][j] + 1,         # insertion
               dp[i][j - 1] + 1,         # deletion
               dp[i - 1][j - 1] + cost)  # replacement/noop
```

でやっていること。編集距離は最小の操作回数なので追加・削除・置換の `min` をとる。

あとは同様に、隣接する既知の編集距離から表を埋めていけば、最後（右下）に `kitten` と `sitting` の編集距離が得られる。

```
   |  -  s  i  t  t  i  n  g
----------------------------
 - |  0  1  2  3  4  5  6  7
 k |  1  1  2  3  4  5  6  7
 i |  2  2  1  2  3  4  5  6
 t |  3  3  2  1  2  3  4  5
 t |  4  4  3  2  1  2  3  4
 e |  5  5  4  3  2  2  3  4
 n |  6  6  5  4  3  3  2  3
```

めでたしめでたし。

こういう応用範囲の広いシンプルなアルゴリズムは好きです。

[Presto](https://github.com/prestodb/presto/pull/7311) や [Hive](https://issues.apache.org/jira/browse/HIVE-9556) にも近年実装されました。みなさん積極的に使いましょう。（とはいえ計算量 $\mathcal{O}(nm)$ は下手に CROSS JOIN とかすると重すぎて詰むので、過去に求めた編集距離はキャッシュしておくなど、ご利用は計画的に。）