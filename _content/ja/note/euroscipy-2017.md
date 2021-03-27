---
aliases: [/note/euroscipy-2017/]
categories: [プログラミング, イベント参加記]
date: 2017-09-02
keywords: [発表, python, euroscipy, pytorch, カンファレンス, keynote, 飲ん, 参加, 実験, パッケージ]
lang: ja
recommendations: [/ja/note/pytorch-autograd/, /ja/note/master-graduate/, /ja/note/chiir-2017/]
title: EuroSciPy 2017に参加してしゃべってきた
---

8月30, 31日にドイツのエルランゲンで開催された **[EuroSciPy 2017](https://www.euroscipy.org/2017/)** に発表者として参加してきた。カンファレンス参加を積極的にサポートしてくれる弊社に感謝感謝。

このカンファレンスは "Scientific Computing in Python" に関するあらゆる話題が対象で、numpy, scipy, matplotlib, pandas, Jupyter notebooks あたりが絡んでいればよろしい。[SciPy Conference US](https://scipy2017.scipy.org/ehome/220975/493388/) のヨーロッパ版ということになる。本会議前2日間はチュートリアル、9月1日にはSprintもあったけど、そっちは不参加。

全体で200名程度の参加があったらしい。思っていたよりもずっと賑やかな会議だったなーという印象がある。参加者のバックグラウンドは教授から学生、企業の研究者、データサイエンティスト、エンジニアまで様々。

### しゃべった

僕が発表した内容は、去年修士研究の片手間で作っていたオンライン型の推薦アルゴリズムのパッケージ [FluRS](https://github.com/takuti/flurs) について：

<script async class="speakerdeck-embed" data-id="f8e9917ab2cf46dfaba1be61b6e449cd" data-ratio="1.33333333333333" src="//speakerdeck.com/assets/embed.js"></script>

実験をして論文を書くためのexperimentalなライブラリなので、本当の意味で "Streaming" な実装とは言えないのだけど…。

Proposalで書いたトークの概要は[ここ](https://www.euroscipy.org/2017/descriptions/19827.html)にある。Real-world machine learning と向き合い始めて半年、ここらで去年までやっていたことにもう一度向き合って整理して、次に繋げるいいきっかけになれば、と思って応募した。

『行列計算の基本くらいは分かるけど、推薦アルゴリズムは何も知らない』という聴衆を想定して、古典的な推薦アルゴリズムから僕が修士研究で取り組んでいたオンライン型の推薦の話まで、理論と実装の雰囲気を15分で話した。「よかったよ！」とわざわざ声をかけてくれた人たちが何人もいて、短い説明から本質的な問題点を汲み取って鋭い質問を投げかけてくれた人たちがいて、とても優しい世界だった…うれしい…。

そして何より「行ってよかった」と思えたのは、Amazon US で Senior Applied Scientist をやっている [Federico Vaggi](https://twitter.com/F_Vaggi) 氏やSonyで推薦関連のR&Dをしている某氏をはじめとする、非常に濃い人たちとこの話題について近い距離で議論できた点。こういう時間がこの先1年間くらいの糧になる。

あと、2日目の最後にあったLT（ひとり2分！）は当日に発表者を募集していたので、勢いで [td-client-python](https://github.com/treasure-data/td-client-python) や [pandas-td](https://github.com/treasure-data/pandas-td) を絡めて（無理矢理）Hivemall や Treasure Data のことを話した。が、これは難しかった…参加者の興味も、HadoopやSparkとはかけ離れたところにある印象だった。

### エルランゲンという街

もうね、すごい。自然。森。会場だって森の中：

![venue](/images/euroscipy-2017/venue.jpg)

airbnbから会場まで40分くらい、こんな道をずーっと歩いていると、なんかもう地元で散歩している気分になる：

![road](/images/euroscipy-2017/road.jpg)

カンファレンスのソーシャルイベントでは、洞窟でビールをつくっている昔ながらのブルワリーが密集した高台のエリア（語彙力）で飲んで飲んでガイドツアーに参加して飲んで、という感じの素晴らしい時間を過ごした。水のようにビールを飲んで、でもどれ1つとして同じ味のビールは無くて、最高だったなァ：

![social](/images/euroscipy-2017/social.jpg)

お世辞にももう一度来たいと思うような街ではなかったけど、よい2日間でした。

[前回のノルウェー](/note/chiir-2017)からヨーロッパのカンファレンスが2回続いてしまったので、次はもう少し違う方角へ飛べたらいいですね。

以下ほかの発表について、メモと感想をつらつらと。

### Keynote

#### Keynote 1: [How to fix a scientific culture](https://osf.io/n4ckd/)

- 『報告されている心理学実験の結果の多くは、再現実験で有意だと示せないものばかりだ』という、論文 "[Estimating the reproducibility of psychological science](http://science.sciencemag.org/content/349/6251/aac4716)" に書いてあるような話題
- みんな "noise mining", "p-hack" をして、自分の喜ばしい、有意だと言えそうな結果を探しているだけだという悲しい現実
- この世界をどうやって変えていくか？そもそも、データを扱うワークフロー上のすべてのステップ（仮説、実験、検証、…）で、我々は意識的・無意識的に“バイアス”をかけてしまっている
- アプローチ1: Pre-registration
  - 実験の各ステップで、これまでやってきたことを peer-review する
  - アイディアを元に実験を設計したらレビューを受ける、データを集めたらまたレビューを受ける…これを繰り返して、最後のレビューまでクリアしたら成果を公開してよい
- アプローチ2: Open Science
  - [Open science framework](https://osf.io/) というプラットフォームもある
  - データや手法、解析用スクリプトなど、様々な情報を公開してフェアな世界をつくろう

Pythonに直接関係のある話では無かったけど、同じ『データの上で仕事をする人間』として耳が痛い内容だった。僕らがいかにたやすく誤った結論を導いてしまうか、それを肝に銘じておかなければならない。

#### Keynote 2: [PyTorch](https://www.euroscipy.org/2017/keynote_soumith_chintala.html)

みなさんご存知、Deep Learning界隈で広く使われているPythonライブラリ [PyTorch](https://github.com/pytorch/pytorch) について、Facebook AI research の [Soumith Chintala](https://twitter.com/soumithchintala) 氏が話してくれた。

- PyTorchは "**numpy alternative**" という位置づけで、GPU上で使える `ndarray` 相当のものを提供する
- [Auto gradient](http://pytorch.org/docs/master/autograd.html)がウリ
- [Data loader](http://pytorch.org/docs/master/data.html#torch.utils.data.DataLoader)も頑張っていて、機械学習で一番面倒な前処理フェーズを手厚くサポートする
- PyTorchの思想
  - 線形なコードフローを推奨する
    - パーツのつなぎ合わせで機械学習のアルゴリズムが実装できる
  - 可能な限り高速化
- 今後の予定
  - Distributed PyTorchを実現したい
  - より高次の自動微分を可能にする
  - JITサポート（[#2565](https://github.com/pytorch/pytorch/pull/2565)で実装が進んでいる）

これは "Introduction to PyTorch" 的な内容であまり面白くなかったかな。まぁKeynoteとは往々にしてそういうものである…。

### 他の発表にみる、"Possibilities of Python" のタテ方向への広がり

一般発表は（自分の発表も含め）いずれも、アカデミックカンファレンスほど理論理論していないし、techカンファレンスほど凝った実装の話というわけでもなく、広く浅い内容だった。発表時間もひとり15分〜30分なので、みんな詳細は削ぎ落としてしゃべる。そしてその分、コーヒーやビールを片手に発表の断片からはじまる議論が異様にヒートアップした感じ。

特に印象的だった発表は次の3つ：

- [Getting the hang of WASM](https://www.euroscipy.org/2017/descriptions/19633.html)
  - [wasmfum](https://github.com/almarklein/wasmfun) というPythonでWASMを生成するパッケージについて
  - いかにWASMベースのレンダリングが高速で安全か、という話
  - Brainfuckのデモが盛り上がった
- [Introduction into the ppci project](https://www.euroscipy.org/2017/descriptions/20514.html)
  - ppci = pure python compiler infrastructure
  - 多様な言語のコンパイラをPythonで実装している話
  - Pythonという言語のポータビリティを活かしたかった
- [Tricks for efficient multi-core computing in Python](https://www.euroscipy.org/2017/descriptions/19817.html) 
  - `multiprocessing.Pool` は古い
  - `concurrent.futures` がナウい
  - `concurrent.futures` をよりロバストにした [loky](https://github.com/tomMoral/loky) というパッケージを作った

[2年前に参加した PyConJP 2015](/note/pyconjp-2015) のテーマは "**Possibilities of Python**" だった [^1]。このときの "Possibilities" は「Webアプリから数学、機械学習、DevOpsまで、Pythonでいろんなことができるよ！」という感覚で、いわばヨコ方向に広がった可能性。

一方で近年のPythonのユースケースに目を向けると、低いレイヤでの最適化や高度なアプリケーションとそれを支える中間レイヤのパッケージ群が目につき、タテ方向にその可能性が広がっている印象をうける。

あとエンジニアリング的に面白かった発表：

- [Autoscaling distributed compute with Dask, Kubernetes and AWS](https://speakerdeck.com/jacobtomlinson/euroscipy17-distributed-compute-with-dask-kubernetes-and-aws)
  - いかにDevOpsチームがデータサイエンティストの解析作業を支えているか
  - [Dask](https://github.com/dask/dask) でタスクを並列実行できるようにしてあげる
  - Daskは与えられたクラスタの上で可能な限り並列化してくれるので、タスクに応じて最適な規模のクラスタを立てておきたい → Autoscalingしましょう

この他の発表は「つくってみた」「やってみた」的なものが多かったかな。

というわけでEuroSciPy、ほどよい規模感でとても充実したいい会議だったけど、願わくばもう少しエンジニアリング寄りの話をたくさん (聞きたかった|したかった) なーとも思っている。

そんな感じで、おつかれさまでした。

![name](/images/euroscipy-2017/name.jpg)

[^1]: そういえば今週は [PyConJP 2017](https://pycon.jp/2017/ja/) らしいですね。