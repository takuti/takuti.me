---
aliases: [/note/data-science-project-structure/]
categories: [機械学習, データサイエンス]
date: 2017-12-16
lang: ja
title: データサイエンスプロジェクトのディレクトリ構成どうするか問題
lastmod: '2022-01-18'
keywords: [practices, ディレクトリ, scientific, バージョン, computing, データサイエンス, プロジェクト, ソースコード,
  ソフトウェア開発, スクリプト]
recommendations: [/ja/note/euroscipy-2017/, /ja/note/acroquest-javabook/, /ja/note/why-spark/]
---

あるいは、論文 "**[Best Practices for Scientific Computing](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745)**" および "**[Good Enough Practices in Scientific Computing](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)**" について。

### TL;DR

- 標題の件について、未だに答えは見えていないのだけど、自分の現状と他の人の例を文字で残しておく。
- こういう話で「あーその手があったかー！」と知ったときの興奮はすごいので、みなさんもっとオープンにいきましょう。
- 大切なのは、ソフトウェア開発と同じ要領でデータサイエンスのプロジェクトを捉えて、分析と言う名の“開発”を行うつもりでディレクトリを掘ること。

### 必要なものリスト

ナウいデータサイエンス/機械学習プロジェクトの中には（経験上、ぱっと思い浮かぶだけでも）次のようなファイル群があって、僕たちはそれらを良い感じに管理したい。

#### ソースコード

役割がいろいろある：

- 前処理（これが一番ヤバい）
- 実験
- 学習
- 予測
- テスト

どの程度モジュール化するかという点は難しくて、Jupyter Notebookの中から特定のクラスを `import` して使いたいこともある。

#### タスクランナー

`make` でも `rake` でもいいし、エントリポイント的なCLIツールを1つ作ってもいい。

いずれにせよ、コードが1つのパッケージとしてキレイにまとまっているわけではないので、各スクリプトの実行手続きが単純かつ明確でなければならない。

#### 設定ファイル

ハイパーパラメータやイテレーション回数、データのパスなどは頻繁に変わる（切り替える）ので、ハードコードしないで外部から読み込みたい。

#### Notebooks

ソースコードとは別。探索的な解析や可視化で使う。ごちゃごちゃしがち。

#### データ

生データと前処理済みデータがある。でかい。

後者をしっかり保存しておくと、2回目以降が楽ちん。

#### 結果

`.pkl` などで出力されたモデル。ファイル名などによるバージョニングが重要で、いつでも過去の結果に戻れるようにしておきたい。各バージョンに対応する精度がどこかで参照できるとさらによい。

あと、可視化したグラフなども重要な結果のひとつ。

#### バージョン

モデルのバージョンに限らず、ディレクトリ全体として「これはいつの状態か」が分かることが大切。

#### 依存

DBやライブラリをインストールする必要があるときはそれをREADMEに明記しておく。インストール用のスクリプトがあればなお丁寧。

Pythonなら `requirements.txt` をきちんと置いておく。

### わたしの場合

以上を踏まえて、自分の現状はどうかというと、だいたいいつも[修論のときのリポジトリ](https://github.com/takuti/stream-recommender)のような構成になる[^2]：

```
.
├── README.md
├── config
│   ├── LastFM
│   ├── ML100k
│   ├── ML1M
│   ├── click
│   └── example.ini
├── converter
│   ├── LastFM.py
│   ├── MovieLens100k.py
│   ├── MovieLens1M.py
│   ├── SyntheticClick.py
│   ├── __init__.py
│   └── converter.py
├── data
├── experiment.py
├── notebook
│   ├── LastFM.ipynb
│   ├── claim-iMF.ipynb
│   ├── paper-iFMs.ipynb
│   └── paper-sketch.ipynb
├── requirements.txt
├── results
└── tool
    ├── clickgenerator.jl
    └── parse_result.py
```

先の要件に沿ってこのディレクトリ構成を振り返ってみる。

- ソースコード
  - 👍
      - アルゴリズム本体とその他の処理（前処理、実験など）を切り分けた
          - 修論では途中から、アルゴリズム本体を別ライブラリ化した[^1]：**[takuti/flurs](https://github.com/takuti/flurs)**
          - 本質的な部分について、それ単体でテストしたりCIが回せるので安心感がある
      - Data Converterを `converter/` 以下に作って、データセット間のフォーマット差異を前処理段階で吸収した
  - 👎
      - 実験用コードのテストが無い
          - データを 8:2 に分けたり、精度を計算したりする部分はモジュール化して要テスト
      - CI回してない
          - テストコードがなくても、最低限、各スクリプトの runability チェックは継続的にするべき
          - 秘密のリポジトリなら Circle CI がべんり
- タスクランナー
  - 👍
      - ルートに1つ `experiment.py` というエントリポイントになるCLIツールを作った
          - Pythonの `import` パスの闇からある程度開放されて精神衛生上よい
          - コマンドライン引数のパースは `optparse` でも良いけど、多くなってきたら [click](http://click.pocoo.org/5/) も便利
  - 👎
      - オレオレCLIツールは少し時間が経つと「どうやって使ったっけ？」となる
          - `Makefile` のような標準的な形でタスクを定義できたほうが長い目で見ると良さそう
- 設定ファイル
  - 👍
      - データごと、手法ごとに `.ini` ファイルを作った
          - `experiment.py` の引数に設定ファイルのパスを渡して、所望のデータ・手法の組み合わせで実験を行う
          - バージョン管理と組み合わせると『この実験結果が出たときのハイパーパラメータ』が残せてよい
  - 👎
      - より良い設定ファイルの設計があった気がする
          - たとえば
              - データセットは名前ではなくパスで設定
              - テストデータ/学習データの割合を 8:2 固定ではなく、設定可能にする
              - 実験そのものの設定と手法のハイパーパラメータを異なるファイルで定義する
- Notebooks
  - 👍
      - 1つの論文（サブプロジェクト）につき 1 notebook、という分け方をした
          - 雑多なNotebookはあえて残さないで、できるだけ早くコード (Data Converterなど) に落とし込む
  - 👎
      - バージョン管理がうまくできない
          - Notebook内の1セルが変わっただけでもgitにはaddを要求されるが、そこまで付き合いきれない
          - 結果として、テキトーなタイミングで最近の変更をガッとまとめて "Update notebook" みたいなコミットで片付けることが多くて、いざというときに戻りづらかった
- データ
  - 👍
      - 生データは大きすぎるので `.gitignore`
          - まぁ当然ですね
  - 👎
      - データのごく一部を同じフォーマットで切り出しておいて（またはダミーデータを作っておいて）、最低限それはGitの管理下におけばよかった
          - 「これってどんなフォーマットのデータだっけ？」というときにすぐ参照できる
          - CIでも使える
          - 別リポジトリ **[takuti/twitter-bot](https://github.com/takuti/twitter-bot)** では似たようなことをしている
      - [scikit-learn のようなダウンロードスクリプト](http://scikit-learn.org/stable/datasets/index.html)があれば再現性の点でより良かった
      - 前処理済みデータを保存しておらず、実験実行のたびに Data Converter が生データを変換していて無駄
- 結果
  - 👍
      - `experiment.py` の出力を `tool/parse_result.py` でパース→Notebook上でそれを可視化、という流れができていた
  - 👎
      - オンラインなアルゴリズムを扱っていたのでモデルの保存は諦めた
          - もう少し何とかならなかったかな…。
- バージョン
  - 👍
      - 当然Git使うよね、というだけの話
      - 論文やレポートを提出したタイミングなど、プロジェクトの区切りでタグを付けておくと便利
  - 👎
      - 実験結果はあまりちゃんと残していなくて、昔の結果が欲しいのにもう消していた、ということが多々あった
- 依存
  - 👍
      - （このリポジトリだと環境依存はあまりないのでアレだけど）READMEはちゃんと書く
      - `requirements.txt` を置いておく
  - 👎
      - （ディレクトリ構成とは直接関係ないけど）もっとミドルウェアを効果的に使えなかったものか
          - 例：Redisを使った [fastcat](https://github.com/takuti/fastcat) など

プロジェクトが異なれば、それはそれでまた違った 👍 と 👎 が出てきたりして、まぁ難しい。

### みんなはどうしているのか

そもそもこんな話を書き留めておこうと思ったのは、データサイエンスプロジェクトにおける `rails new` 的な立ち位置を目指している子 "**[Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science)**" を見かけたから。

READMEから Cookiecutter 標準のディレクトリ構成を引用すると次のような雰囲気：

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
```

個人的なポイント：

- `LICENSE` 重要
- 最初に挙げた要件の通り、データはimmutableな生データと前処理済みデータに分かれている
- READMEとは別でドキュメント `docs/` がきちんとある
- `references/` はプロジェクトを通して何度も参照することになるので意外と重要
- ソースコードは `src/` 以下で一元管理
  - 役割ごとにディレクトリにまとめて、ファイル名は `動詞_xxx` に統一することで何をするスクリプトかわかりやすくなっている
- テストには `tox`（テストコードは `src/` 以下に適宜置くのかな）
  - このあたりは好みの問題もあるけど、toxだと異なるバージョン間のテストが楽だった気がする[^3]

このような構成について、詳しくは "[Structure and automated workflow for a machine learning project — part 1](https://towardsdatascience.com/structure-and-automated-workflow-for-a-machine-learning-project-2fa30d661c1e)" なども参照されたい。ここまで考え抜かないとディレクトリ構成のテンプレ化は困難か…。

関連して、[Kaggleのディスカッションフォーラムでも似たような議論がなされていた](https://www.kaggle.com/general/4815)。回答の一部を並べてみよう：

```
├── code
├── data
│   ├── input
│   ├── working
│   └── output
├── demos
└── tests
```

▲ `data/` 内で『どんなデータか』をディレクトリごと分けて保存している。

```
├── analysis
├── data
├── download
├── features
├── src (or <method>)
├── logs
└── submissions
```

▲ `download/` は生データ、`data/` は何らかの処理を施したデータ、さらに特徴量を作ったらそれは `features/` に保存。そして `logs/`！これ確かに一番大切だ…。

```
├── data
├── util
├── history (= submissions)
└── <method>
```

▲ `data/` には生データだけでなく、train/test用に分割されたデータなど、いろいろ入る。データの前処理用スクリプトなどは `util/` に入る。メインのコードは手法や使用言語ごとにディレクトリを完全に分けているというのが面白い (e.g., `knn_R/` など)。

```
├── documentation
├── data
├── code
├── submissions
└── figures
```

▲ ドキュメントと図の管理が重要。

人によって細かな配慮の差はあれど、大枠は共通していて、

- 元データ
- 前処理済みデータ
- 実験結果の履歴 (＝ Kaggle の submissions 履歴)
- 分析の足跡（ログ、あるいはソースコードそれ自体）

これらをきちんと残すことが重要なんだと思う。

ちなみに、このフォーラムで挙げられていた文献：

- **[Best Practices for Scientific Computing](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745)**

が良くて、著者たちは科学技術計算におけるソフトウェア開発のベストプラクティスとして次の8つを挙げている：

1. Write programs for people, not computers.
  - リーダブルコードを読んで実践しましょう
2. Let the computer do the work.
  - 補助的なスクリプトと `make` などを利用して複雑な処理を単純化しましょう
3. Make incremental changes.
  - 可能な限りすべての中間成果物をバージョン管理して、再現可能な状態を保ちつつアジャイル的にプロジェクトを進めましょう
4. Don’t repeat yourself (or others).
  - DRYです
5. Plan for mistakes.
  - 十分な `assert` とテストコードで保守的に実装を進めつつ、バグを踏んだらそれは即テストケースに追加しましょう
6. Optimize software only after it works correctly.
  - プロファイラを使ったボトルネックの発見、C言語などのより低級な言語による実装といった最適化作業は、正しく動くものができた後で考えましょう
7. Document design and purpose, not mechanics.
  - インタフェースの詳細やそのような実装になった背景など、非自明な点をしっかりドキュメント（コメント）に残しつつ、適宜リファクタリングを行って自己説明的なコードにしていきましょう
8. Collaborate.
  - コードレビュー、ペアプロ、issue trackingなどを行いましょう

何を当たり前のことを！という感じなんですが、こんな当たり前のことさえ実践できなくなってしまう恐ろしさをデータサイエンスのプロジェクトは孕んでいるのだと思います。様々なツールとデータに翻弄され、コードの質以前に前処理や泥臭いトライ＆エラーの壁が分厚くて、頭の使い所が普段と全く違う。結果として、ゴミ屋敷のようなディレクトリが大量生成される。

だからこそ視点を変えて、データ分析を1つのソフトウェア開発として捉える必要があって、`Makefile` を作ることや、データ/コード/結果のバージョン管理、テスト、CIを行うことが大切。

なお、"Best Practices for Scientific Computing" から4年後の今年、より実践的かつ最小限のポイントを伝える "Good Enough Practices for Scientific Computing" という論文が発表された：

- **[Good Enough Practices in Scientific Computing](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)**

この詳細はリンク先に譲るが、個人的に注目したいのは以下の点で、先に挙げた複数のディレクトリ構成の実例と考えていることが合致する：

- データ管理
  - 生データはそのままの状態で保存して、同時に複数の場所でバックアップをとっておくこと
  - データの各処理過程で、その状態をしっかりと記録すること
- プロジェクト管理
  - Todoリストを作っておくこと
  - ライセンスを明確にすること
  - プロジェクトを他の人が引用しやすい状態にしておくこと（`LICENSE`と同じ要領で、`CITATION`みたいなファイルを作っておく）
- ディレクトリ構成
  - `docs/` ディレクトリにドキュメントを残すこと
    - そこに `CHANGELOG.txt` も作成して、変更をトラッキングすること
  - 各ステップで得られたデータやファイルは `data/` や `results/` といったディレクトリにしっかり保管すること
  - ソースコードは `src/` にまとめること
  - 補助的なスクリプトやコンパイル結果は `bin/` にまとめること
  - すべてに説明的なファイル名をつけること

より具体的に、論文中で挙げられているディレクトリ構成の例は次のような感じ：

```
.
|--CITATION
|--README
|--LICENSE
|--requirements.txt
|--data
|  |--birds_count_table.csv
|--doc
|  |--notebook.md
|  |--manuscript.md
|  |--changelog.txt
|--results
|  |--summarized_results.csv
|--src
|  |--sightings_analysis.py
|  |--runall.py
...
```

さらに、大きな変更を行う際は、以下のようにプロジェクトの全ファイルをどこかにコピーする、ということを提案している：

```
.
|--project_name
|  |--current
|  |  |--...projectcontentasdescribedearlier...
|  |--2016-03-01
|  |  |--...contentof'current'onMar1,2016
|  |--2016-02-19
|  |  |--...contentof'current'onFeb19,2016
```

これはKaggleのフォーラムで挙がっていた『メインのコードは `knn_R/` のように、手法や使用言語ごとにディレクトリを完全に分ける』という話に通じる。こうやって割り切ってバックアップをとっておくと安心感が違うよね。

### まとめ

ここまで見てきて、『なにが正解』という話ではなくて、みんな同じように悩んで試行錯誤してるんだなぁということが分かった。

そして他人の例と "**[Best Practices for Scientific Computing](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745)**", "**[Good Enough Practices in Scientific Computing](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)**" から、ソフトウェア開発、つまり普段のコーディングと同様にデータサイエンスプロジェクトを扱うことの大切さに改めて気付かされた。

目の前のデータにばかり囚われてゴミを量産しないように生きてゆきましょう。

[^1]: 公開したのは論文採択後。
[^2]: もちろん研究で行う『実験』と業務で行う『分析』は規模、秘匿性、環境、関わる人数などの点で大きく異なるけど、それでもディレクトリ構成の大枠は変わらないという認識。
[^3]: データサイエンスのプロジェクトで複数のPythonのバージョンをサポートする必要があるのか、という説もあるけど。