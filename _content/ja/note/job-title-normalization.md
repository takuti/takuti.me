---
aliases: [/note/job-title-normalization/]
categories: [プログラミング, 自然言語処理]
date: 2017-07-09
lang: ja
recommendations: [/ja/note/levenshtein-distance/, /ja/note/fastcat/, /ja/note/leakage/]
title: Job Titleの前処理＆クラスタリングをどうやって実現するか問題
---

LinkedIn など、**Job Title**（職場での肩書き）をユーザに入力させるサービスは世の中にたくさんある。機械学習、データマイニングの文脈で、このデータをいかに扱うかという話。

### 問題

手入力の雑多なJob Titleデータがある：

|user id | title |
|:---:|:---|
|1|VP of Marketing|
|2|Eng. Mng.|
|3|Marketing Manager|
|4|Software Engineer and Entrepreneur|
|5|Founder and CTO|
|6|Chief Technology Officer|
|... | ... |

このデータを各ユーザの demographics を表す特徴量（カテゴリ変数）として使いたい。

大まかな流れは、

1. 前処理
2. クラスタリング（i.e., 次元削減
3. 未知のJob Titleが属するクラスタの予測

こんな雰囲気。

### 前処理

Job Titleはユーザが好き勝手に入力したデータなので、表記揺れが激しく前処理が必須。

"[Mining LinkedIn: Faceting Job Titles, Clustering Colleagues, and More](http://chimera.labs.oreilly.com/books/1234000001583/ch03.html)" では、実際にLinkedInのデータを取得して前処理、可視化、クラスタリングする際の流れがPythonコードと共に紹介されている。Job Titleに対して行う前処理は、"President/CEO" といったスラッシュ区切りのTitleを分割して、略語をルールベースで展開するというもの：

```py
transforms = [
    ('Sr.', 'Senior'),
    ('Sr', 'Senior'),
    ('Jr.', 'Junior'),
    ('Jr', 'Junior'),
    ('CEO', 'Chief Executive Officer'),
    ('COO', 'Chief Operating Officer'),
    ('CTO', 'Chief Technology Officer'),
    ('CFO', 'Chief Finance Officer'),
    ('VP', 'Vice President'),
    ]

csvReader = csv.DictReader(open(CSV_FILE), delimiter=',', quotechar='"')
contacts = [row for row in csvReader]

# Read in a list of titles and split apart
# any combined titles like "President/CEO"
# Other variations could be handled as well such
# as "President & CEO", "President and CEO", etc.

titles = []
for contact in contacts:
    titles.extend([t.strip() for t in contact['Job Title'].split('/')
                  if contact['Job Title'].strip() != ''])

# Replace common/known abbreviations

for i, _ in enumerate(titles):
    for transform in transforms:
        titles[i] = titles[i].replace(*transform)
```

そして前処理を終えたJob Titleを『Titleごと』および『単語ごと』にカウントして、“重要な特徴量”を探っている：

```
+-------------------------------------+------+
| Title                               | Freq |
+-------------------------------------+------+
| Chief Executive Officer             | 19   |
| Senior Software Engineer            | 17   |
| President                           | 12   |
| Founder                             | 9    |
| ...                                 | ...  |
+-------------------------------------+------+

+---------------+------+
| Token         | Freq |
+---------------+------+
| Engineer      | 43   |
| Chief         | 43   |
| Senior        | 42   |
| Officer       | 37   |
| ...           | ...  |
+---------------+------+
```

この他には

- ストップワード (of, and, ...) や記号の除去
- 大文字・小文字の統一
- ステミング

などが考えられる。[NLTK](http://www.nltk.org/index.html)をバシバシ活用しましょう。

### クラスタリング

前処理を行ったJob Titleをクラスタリングすることでカテゴリ変数に落とし込んでいく。

このとき、Job Titleはユーザの立場 (VP, Manager, Chief XXX, ...) と職務 (Marketing, Engineer, Chief "Technology" Officer, ...) の2つの情報を表現しうるので、それらを別々に扱いたい。

すなわち、各ユーザのJob Titleデータを立場 (role) と職務 (function) の **Category** として再定義することがゴール：

|user id | category: role | category: function |
|:---:|:---|:---|
|1| executive | marketing |
|2| manager | engineering |
|3| manager | marketing |
|4| entrepreneur | engineering |
|5| executive | engineering |
|6| executive | engineering |
|...| ... | ... |

この点は "[Normalizing Job Titles vs. eliminating them](https://nation.marketo.com/thread/38762-normalizing-job-titles-vs-eliminating-them)" でもマーケティング畑の人たちが議論していて、人の立場を表す *hierarchy level* と職務を表す *functional role* を分けて考えよう、という話をしている。

クラスタリング済みのJob Titleデータを提供している "[400 Categorized Job Titles for Data Scientists](http://www.datasciencecentral.com/profiles/blogs/400-categorized-job-titles-for-data-scientists)" では、データ作成時に実際に行った処理の様子が示されている。

ここでもやはり、立場を表す *job level* と職務を表す *job category* を区別している。クラスタリングは完全にルールベースで、前処理済みのJob Title `$job` が、ある特定の単語を含んでいるか否かでクラスタを決める：

```pl
#---- Step 1: creating job level
$level="Other";
if ($job =~ "vice president") { $level="Executive"; }
if ($job =~ "vp ") { $level="Executive"; }
if ($job =~ "ceo") { $level="Executive"; }
if ($job =~ "executive") { $level="Executive"; }
if ($job =~ "officer") { $level="Executive"; }
if ($job =~ "chief") { $level="Executive"; }
if ($job =~ "partner") { $level="Executive"; }
if ($job =~ "president") { $level="Executive"; }
if ($job =~ "director") { $level="Manager"; }
if ($job =~ "manager") { $level="Manager"; }
if ($job =~ "lead") { $level="Manager"; }
if ($job =~ "consultant") { $level="Consultant"; }
if ($job =~ "principal") { $level="Consultant"; }
if ($job =~ "professor") { $level="Professor"; }
if ($job =~ "analyst") { $level="Analyst"; }
if ($job =~ "student") { $category="Student"; }
if ($job =~ "analyst") { $category="Analyst"; }
$ljob_level{$job}=$level;

#---- Step 2: creating category
$category="Other";
if ($job =~ "recruit") { $category="Recruiter"; }
if ($job =~ "talent") { $category="Recruiter"; }
if ($job =~ "engineer") { $category="Engineering"; }
if ($job =~ "software") { $category="Developer"; }
if ($job =~ "develop") { $category="Developer"; }
if ($job =~ "architect") { $category="Data Plumbing"; }
if ($job =~ "scientist") { $category="Data Science"; }
if ($job =~ "science") { $category="Data Science"; }
if ($job =~ "stat") { $category="Statistician"; }
if ($job =~ "research") { $category="Research"; }
if ($job =~ "marketing") { $category="Business Analytics"; }
if ($job =~ "analytics") { $category="Business Analytics"; }
if ($job =~ "business") { $category="Business Analytics"; }
if ($job =~ "operations") { $category="Business Analytics"; }
if ($job =~ "consultant") { $category="Consultant"; }
if ($job =~ "training") { $category="Trainer"; }
if ($job =~ "lecturer") { $category="Trainer"; }
if ($job =~ "professor") { $category="Trainer"; }
if ($job =~ "student") { $category="Student"; }
$ljob_category{$job}=$category;
```

もう少し機械学習っぽい方向性はどうだろう。さすがに「Titleの bag-of-words 表現を k-means に放り込んで、ユークリッド距離の意味でクラスタリング」というのは乱暴な気がする。ベクトルの表現や類似度を工夫して、近傍法ベースの（教師あり）分類アルゴリズムの適用も視野にいれたいものである[^1]。

調べてみると、[word2vecをJob Title分類に応用した話](https://arxiv.org/abs/1609.06268)が見つかる。ナウい。

Title間の類似度としては、[前処理のときにも紹介した記事](http://chimera.labs.oreilly.com/books/1234000001583/ch03.html#measuring-similarity)で、

- 編集距離 (Levenshtein distance)
- n-gram similarity
- Jaccard distance

を検討している。

いずれにせよ、立場 (role) と職務 (function) を分けて考える場合は、より丁寧に前処理を行って、モデルを2つ作るという話になりそう。または role はルールベースで分類して、function は機械学習、といったハイブリッドな方法も考えられる。このあたりはどれだけ正確にクラスタリングしたいか、という要求次第ですね。

### 未知のJob Titleが属するクラスタの予測

一度クラスタ（カテゴリ）が得られれば、次のような**マッピングテーブル**が作れる：

|user id | raw title |category: role | category: function |
|:---:|:---|:---|:---|
|1|VP of Marketing| executive | marketing |
|2|Eng. Mng.|manager | engineering |
|3|Marketing Manager|manager | marketing |
|4|Software Engineer and Entrepreneur| entrepreneur | engineering |
|5|Founder and CTO|executive | engineering |
|6|Chief Technology Officer|executive | engineering |
|... | ... |... | ... |

あとはマッピングテーブルの "raw title" との比較で、未知のJob Titleに対してもクラスタが割り当てられる。ここでいう“比較”とは、ルールベースな場合もあれば、（ベクトル化→）何らかの類似度に基づく場合もある。要は、似ているものが見つかればそれでよろしい。

### まとめ

手入力によるユーザの肩書きデータを前処理＆クラスタリングして、カテゴリ変数にするための方法を探ってみた。

更に調べると、次の2つの文献はRNNを利用していて、すごく頑張っている：

- [Job Classification Based on LinkedIn Summaries](https://cs224d.stanford.edu/reports/BoucherEric.pdf)
- [Learning Text Similarity with Siamese Recurrent Networks](http://www.aclweb.org/anthology/W/W16/W16-1617.pdf)

特に後者は、ペアワイズの“似たJob Titleか否か”の学習を文字レベルで行っていて面白い。

しかしまぁ結局は前処理が最も重要なステップであり、Job Titleという限定されたドメインの中での話なので、クラスタリングも単純なルールベースで案外十分だったりする。こういうとき、手法の取捨選択をもっと素早くできるとイイなぁと思う。精進します。

[^1]: たとえば代表的なJob Titleに予めクラスタを（人力で）割り当てておき、その他のTitleは代表タイトルとの類似度を元に、“一番近いクラスタ”に割り当てる。