---
aliases: [/note/trends-in-real-world-recommender-systems-2017/]
categories: [カンファレンス, 情報推薦]
date: 2017-11-23
lang: ja
recommendations: [/ja/note/data-skeptic-recommender-systems/, /ja/note/recommender-libraries/,
  /ja/note/coursera-recommender-systems/]
title: 筋トレ、登山、昨今の推薦システムのトレンドなどについて話しました
---

元インターン先である[シルバーエッグ・テクノロジー](http://www.silveregg.co.jp/)とのご縁があり、『[ビッグデータ解析のためのAI技術の最新事情とビジネスへの応用](http://peatix.com/event/307962)』という~~名前だけ聞くと心配になる~~セミナーで講演の機会をいただき、昨今の推薦システムのトレンドについてお話してきました：

<script async class="speakerdeck-embed" data-id="dbe350bda78f411d88e35218dceff98a" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>

1. ※ 修士研究までの僕個人の経験に基づいた内容であり、これが世の中の全てではありません。
2. ※ 論文などですでに公開されている情報しか含んでいません。
3. ※ 内容は、過去および現在のいかなる所属の立場を代表するものでもありません。

はむかず先生が「趣味は筋トレです」と自己紹介していたので便乗したけど、ちゃんとジムに通っている先生に対して、僕は家でプッシュアップ、腹筋ローラー、チューブエクササイズ各3セットを週2〜3回やっているだけで、あとはそこにランニング（6-10km）またはプール（1時間弱）を加えている程度なので本気度が違う。

セミナー後には、公営のジムは（ユーザ層的な意味で）安心できる、ゴールドジムなどはガチ勢ばかりで怖いという話で盛り上がった気がする。願わくばもっとたくさん筋トレトークを聞きたかった。

なお、はむかず先生は糖質制限などはそんなに意識していないとのこと。僕も外ではそれほど気にせず好きなものを飲み食いしているけど、一方で、家ではお米や麺は控えて、プロテイン、ヨーグルト、納豆、豆腐、ささみ、チーズ、茹でて小分けにして冷凍した野菜各種のローテーションになっている。

まぁ筋トレよりも登山のほうが最近は大事で、そうなると炭水化物が命なので糖質制限とか知るかという気分になる。

今回のセミナー会場は大阪だったので、有給を取って前々日入りして伊吹山に登るなどした：

![ibuki1](/images/201711/ibuki1.jpg)

![ibuki2](/images/201711/ibuki2.jpg)

ちょうど登った日が初冠雪だったらしく、4合目くらいまでは鮮やかな紅葉と琵琶湖を、それ以降は今シーズン初の雪の感触を楽しんだ。平日に登る混雑していない山の素晴らしさたるや…！

そしてセミナー当日は早朝に京都の大文字山に登ってから大阪へ移動した：

![daimonji](/images/201711/daimonji.jpg)

![ginkaku](/images/201711/ginkaku.jpg)

紅葉シーズンの京都を独り占めできて最高だった。八坂神社のほうから入って銀閣寺側に抜けるコースで、散歩感覚で行ったら思った以上にちゃんとした登山で笑った。下山後はタイミングよく銀閣寺開店(?)凸ができてすごく良い。

日曜昼過ぎの開催だったセミナーには、エンジニアを中心に多くの方々の参加があった。ありがとうございました。（正直、大阪開催のミニセミナーでこんなに人が集まるとは思わなかった…。）

僕の話の内容は、修士研究までの経験談を土台として「推薦システムのトレンドはどこにあるのか？」という問いに答えを求めるもの。

### 協調フィルタリング、Matrix Factorization、レーティング予測の先にあるもの

昨今の推薦システムの理論と実践のトレンドを一言で表すと "**Beyond collaborative filtering on rating**" だろう。

『**[Understanding Research Trends in Recommender Systems from Word Cloud](/note/recsys-wordcloud)**』で推薦システムのトップカンファレンス RecSys の直近4年分の採択論文の概要からワードクラウドを作ったが、この分野の代名詞と言っても過言でない "Collaborative Filtering" や "Matrix Factorization" という手法、そしてこれまで広く議論されてきた "rating" という種のデータの存在感が明らかに薄くなっていた。

一方で、近年目立つようになったのは "product" や "review," "social" のような実アプリケーション寄りのデータを表す単語や "online," "group" のような現実的な問題設定を示唆する単語だ [^1]。

アカデミアで議論されてきた手法のアプリケーション応用が進むにつれて、理論 (Theory) と実践 (Practice) のギャップというものが明るみになった。その結果が、ワードクラウドにも現れた『協調フィルタリングのその先を考える』というトレンドなのだと思う。これは『**[推薦システムのトップ会議RecSys2016に参加した](/note/recsys-2016/)**』のときに僕自身が肌で感じたことでもある。

Netflixが自分たちの推薦アルゴリズムの精度向上に対して多額の賞金を出した [Netflix Prize](https://www.netflixprize.com/) から8年、推薦システムを取り巻く環境は大きく変わった。

彼ら自身、サービス形態そのものがアメリカ国内のDVDレンタルから世界規模の動画ストリーミングへと変化していく中で、システムのスケーラビリティという問題に直面した。その結果、[今では Netflix Prize を勝ち取った手法それ自体はサービスでは使っていない](https://www.techdirt.com/articles/20120409/03412518422/why-netflix-never-implemented-algorithm-that-won-netflix-1-million-challenge.shtml)という。

実運用に耐えうるスケーラビリティとは、往々にして単一の手段では達成されない。Real-world recommender systems とは、ヒューリスティクスから深層学習まで、様々な手法を必要に応じて組み合わせて実装したハイブリッドなものなのだ。

ちなみに僕の場合、卒業論文（2014年）と修士論文（2016年）はいずれも情報推薦をテーマに執筆したが、前者がバッチ型のアルゴリズムであったのに対して、後者ではスケーラビリティ的な問題意識からオンライン型の推薦アルゴリズムに焦点を当てたという変化があった。

### 推薦システム≠機械学習であり、ヒューリスティクスも恥ではないし役に立つ

『**[修士課程で機械学習が専門ではない指導教員の下で機械学習を学ぶために](/note/master-graduate/)**』で書いたような、手探りでこの分野を掘り下げてきたひよっこだからこそ話せる内容もあるのではないかと思い、経験から伝えたい3つのメッセージを用意して講演に臨んだ。

1つ目は「**推薦システム=機械学習ではないのだ**」ということ。

より“良い”推薦システムを作るために、機械学習の存在は必須ではない。UIで解決できる問題かもしれないし、ヒューリスティクスや non-personalized な推薦手法で十分な場合だってあるかもしれない。くれぐれも、この分野のアルゴリズム的側面だけにとらわれないことだ。そんな話は『**[Podcast "Data Skeptic" の推薦システム回が良すぎて3回聞いた](/note/data-skeptic-recommender-systems)**』でも言及した。

仮に機械学習を応用するとしても、あくまで1つのツールとして考えるべきだと思う。そのような姿勢が見て取れる[楽天のゴルフパッケージ推薦のアルゴリズム](https://dl.acm.org/citation.cfm?id=2806416.2806608)は気持ちがいい。

このアルゴリズムは、推薦対象ユーザに対してゴルフパッケージの『コース』『値段』『オプション（キャディ/ランチの有無など）』の3要素を個別にスコアリングして、その重み付き和を「ユーザがこのパッケージをどの程度好むか」の予測値とする。そして、予測値上位N件を推薦する。

論文では実データの傾向をみて、解決すべき問題を定めて、可能な限りシンプルかつ解釈性の高い推薦アルゴリズムを提案している。

対照的に、何も考えずアルゴリズム的に魅力的な道を選択すると悲惨な結果が訪れる。

僕の場合、流行りの Factorization Machines という手法を思いつきで応用した結果、精度は出ないし、ハイパーパラメータが多すぎて困るし、意外と計算コスト重いし、モデルの解釈が難しいし、まぁ大変だった[^2]。そもそも手法ありきで話を始めたので、「論文を書くために精度を出す」というゴールしか設定できず、立ち止まって他の方法を考えることすら忘れていた。よくない。

手法ありきではじめるからこうなる。理屈だけ聞くとステキな、より複雑な手法に執着するからこうなる。

だからこそ、2つ目の「**できるだけシンプルなシステムを、データドリブンで作るべき**」というメッセージがある。

シンプルさの加減は難しいが、何も見えなければ一度トレンドは無視して、協調フィルタリングやロジスティック回帰のような枯れかけている手法から始めるのがよいだろう。そして non-personalized な推薦手法と比較してみるといい。

Amazonの "Do the math" というメッセージを『**[The Amazon Way on IoT - Amazonのビジネスから学ぶ、10の原則](/note/the-amazon-way-on-iot)**』で紹介したが、僕は "Do the **minimum** math" といったほうが適切であるように思う。

精度だけで議論すると、データによっては「Matrix Factorization よりも "Most Popular" （思考停止で、最も人気なアイテムをひたすら推薦する手法）のほうが高精度」という結論になりかねない。そんな悲しい結果に終わらぬよう、現場ではデータからはじまる仮説・検証のサイクルを大事にしようという話だ。

なお、ここで言う“現場”のデータは、自室や研究室のデスクの上、論文やGitHubで公開されている情報の中には存在しない。

以前、[修士研究の振り返り](/note/master-graduate)で「**機械学習の応用研究は企業(で|と)やるべきだと強く思う**」と書いた。これがそのまま3つ目のメッセージ。実データ、実サービスから生じた問題意識こそ本物で、深掘りする価値があるのだと思う。

### これからの推薦システム

Netflixは、画面に表示されるあらゆる情報がパーソナライズされているこの時代を "[Everything is recommendation](https://www.slideshare.net/justinbasilico/past-present-future-of-recommender-systems-an-industry-perspective)" だと言っている。

"**Beyond collaborative filtering on rating**" というトレンドが示唆する通り、これからも推薦技術は様々なシーンに応用され、ますます "Everything is recommendation"化は進行するだろう。たとえば、業界の重鎮であるミネソタ大学のJohn Konstan先生は、[教育への応用や音声インタフェースとの統合を考えている](/note/data-skeptic-recommender-systems)。

そんな時代の流れに乗るためには、まず古典的な推薦手法を学び、手元で試してみよう：

- **[Courseraの推薦システムのコースを修了した](/note/coursera-recommender-systems)**
- **[推薦システムのためのOSSたち](/note/recommender-libraries)**

実データに応用するのなら、ここから学べる枯れた内容・手法が最良。それが僕らの目指す“シンプルさ”の目安にもなる。

『ビッグデータ解析のためのAI技術の最新事情とビジネスへの応用』というセミナーで枯れたシンプルな手法を薦めるというのは何か矛盾しているような気もするが、リアルはそういう泥臭い取り組みの上に成り立っている―『**[ルールベースは『人工知能』か](/note/rule-based-ai)**』でも書いたことですが、そんなことを僕は強く思うのであります。

全体を通してマインドセット的なお話に徹してしまい、「結局どうやって推薦システムを作っていけば良いのか」という問いへの具体的な回答は聴衆に委ねる形になってしまった。そこは反省。特に、聴衆の多くが現場のエンジニアだったことを考えると、もう少し実践的なTipsを並べるべきだった気もする。

しかしまぁ、個人的には大変貴重な、楽しい楽しい機会でありました。ありがとうございました。

[^1]: "Group Recommendation" という新しい問題設定があって、[RecSys2016ではそれ専門のチュートリアルセッションがあった](https://www.youtube.com/watch?v=eHDzdz_lIYM)。
[^2]: もちろん自分の実装力不足という問題もあった。