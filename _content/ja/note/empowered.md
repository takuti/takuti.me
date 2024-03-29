---
categories: [読書記録, デザイン]
series: [product]
date: 2021-09-29
lang: ja
title: ソフトウェアプロダクトマネジメントのバイブル "Inspired" の続編 "Empowered"、わかりみが深い。
lastmod: '2022-09-02'
keywords: [プロダクト, リーダー, チーム, 顧客, risk, 組織, コーチング, 前作, okr, empower]
recommendations: [/ja/note/product-management-myths/, /ja/note/hooked-design/, /ja/note/product-management-and-bullshit-job/]
---

これまでに読んだソフトウェアプロダクトマネジメントに関する本の中で個人的にいちばん信頼している "[Inspired](https://amzn.to/3ENMSXv)" の続編、"[Empowered](https://amzn.to/3i8xT0G)" を読んだ。

<a href="https://www.amazon.co.jp/EMPOWERED-Ordinary-Extraordinary-Products-Silicon-ebook/dp/B08LPKRD5L?pd_rd_w=4rkIZ&pf_rd_p=367c54b8-500b-4071-9b4d-65fe16192688&pf_rd_r=DCFBTCMFQY5S923M9J5V&pd_rd_r=86aa7358-41db-4a4a-8549-c5fef6ef3158&pd_rd_wg=ABNPZ&pd_rd_i=B08LPKRD5L&psc=1&linkCode=li2&tag=takuti-22&linkId=de0520e54080f4ef8beae38cc02adb4f&language=ja_JP&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-fe.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B08LPKRD5L&Format=_SL160_&ID=AsinImage&MarketPlace=JP&ServiceVersion=20070822&WS=1&tag=takuti-22&language=ja_JP" ></a><img src="https://ir-jp.amazon-adsystem.com/e/ir?t=takuti-22&language=ja_JP&l=li2&o=9&a=B08LPKRD5L" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />

内容的には特に目新しい点もないのだが、前作同様、点と点をつなげて一冊の本という“プロダクト”を作るのが本当にうまい。聞いていて耳が痛くなるような話をフックに「なぜそれが重要なのか」を読者に訴えかけ、ロールモデルやケーススタディを交えて「じゃあどうすればいいのか」をクリアに伝えてくれる。

エンジニア、デザイナー、プロダクトマネージャーを基本とする「プロダクトチーム」[^1]。前作ではそんなプロダクトチームが顧客を *"Inspire"* するための方法論が語られていた。一方、今作は組織内で彼ら彼女らをコーチングする立場の「プロダクトリーダー」（マネージャーやテックリード等）がチームを *"Empower"* することに焦点を当てている。

### プロダクトリーダーの責任

チームの一員 (Individual Contributor; IC) であろうとリーダーであろうと、尊重すべき基本要素は普遍だ。

1. **Vision**: ビジョンドリブン*&mdash;MercenaryではなくMissionary&mdash;*であること
2. **Foundation**: 様々な書籍で学ぶことができる“当たり前”のスキルを正しく身に着け、実践すること
3. **People**: リーダーシップ・オーナーシップを持ち、コミュニケーションを通して信頼関係を構築すること

ここで注意したいのは、ICだからリーダーシップは不要だとか、マネージャーだから顧客との接点をおろそかにしてもいいとか、そういう話では決して無いということ。ただ、プロダクトリーダーの仕事にはICとしての経験を踏まえた、より大きな役割と責任が伴うのだ、という話。

究極的には、チームの失敗はリーダーによるコーチング不足の責任である。本書の中で著者が明示的にこの点を強調しているのは、例えばリモートワークによって破綻するプロダクトチームの話。

前提として、プロダクトチームの仕事は次の2つに大別される。

1. 顧客との密なコミュニケーションとプロトタイピングによって解を探索する**Discovery**フェーズ
2. 開発を進め、製品を顧客に届ける**Delivery**フェーズ

昨今のリモートワーク環境下で特に困難なのは前者で、むしろ後者はリモートの方が上手くいく場合も少なくない。

“弱いプロダクトチーム”は、リモートコミュニケーションの難しさからウォーターフォール的な仕事の進め方に回帰してしまう。それは第三者から仕様を与えられて稼働する "Mercenary" なプロダクト開発に他ならない。加えて、心理的安全性を担保することの難しさ。面と向かって無神経な発言をする人間は多くないだろうが、メールやSlack上での文面によるコミュニケーションでは、そのような排他的・閉鎖的なやり取りが容易に発生する。

結果、プロダクトチームはDiscoveryに失敗し、必然的にDeliveryにも失敗する。これらはすべてリーダーのコーチング不足が招いた結果である、と。

裏を返せば、リーダーの仕事によってプロダクトチームの働きや顧客に与えるインパクトは何倍・何十倍にもなりうる、ということでもある。

### “当たり前”を教えるのは誰か

前作で語られたプロダクト開発における4つのリスク。プロダクトチームの役割は、これらのリスクを回避して顧客に価値ある製品を届けることである。

1. **Value risk**: 顧客がそもそもプロダクトを買ってくれるか
1. **Usability risk**: ユーザはそのプロダクトを正しく使うことができるか
2. **Feasibility risk**: エンジニアはそのプロダクトを開発することができるか
4. **Business viability risk**: 法務や財務といった視点で見たときに、そのプロダクトは現実的であるか

そのための方法論は確かに存在し、数多の書籍で同様に語られていることでもある。例えばプロダクトマネージャーに関して言えば、その第一歩として

- 何十もの顧客に会いましょう
- データからビジネスを知りましょう
- 市場・競合の理解を深めましょう
- 財務、法律、倫理、技術、営業、GTM等に関する知見を幅広く得ましょう

といった取り組みがキモであり、具体的なツールやテクニックは枚挙にいとまがない。そして往々にして、創業者が多大な影響力を持つ初期のスタートアップではこのような営みが極めて自然に行われている。

しかし組織が大きくなるにつれて、このような“当たり前“を創業者からリーダーへ、リーダーからチームメンバーひとりひとりへと継承し、全体を *"Empower"* することが必要になってくる。

- 最低でも週に1時間は顧客と直接話す機会を作る
- 我々は経営陣やステークホルダーのためにプロダクトを作っているのではない
- 顧客に「何がほしいですか」と聞かない

そのようなキホン（あるいはバッドノウハウ/アンチパターン）を伝え、プロダクトチームを“開発”することがリーダーの役割である。

また、プロダクトチームは「作るべき機能」ではなく「解決すべき問題」を与えられて行動するものであり、それを実践するためには「顧客の人生・生活が10年後にどうなっているべきか」を語るビジョン（指針；"North Star"）の存在が欠かせない。プロダクト開発組織は、何よりも先にそのビジョンの熱狂的信者でなければならない。その先にあるのが、具体的な経営目標や戦略、ロードマップといった "HOW" に関する議論だ。このようなマインドセット・土壌を形成するのもまたリーダの仕事である。

採用からオンボーディング、コーチング、昇級、時にリストラの判断を下す場に至るまで、リーダーは一貫してそのようなメッセージを発し続け、多様性を保ちながら“強いプロダクトチーム”を作り上げてゆくことになる。換言すれば、成長の過程で壁にぶつかってしまうプロダクト開発組織は、リーダーに起因する何らかの構造的な問題を抱えている。

### プロダクト組織はかくあるべし

どこまでも成長を続ける強固なプロダクト組織と、そこそこの成長を収めて頭打ちになる組織の間にある壁。前述の通り、それはリーダーの仕事に依るところが大きい。では、“良きプロダクトリーダー”の働きとはどのようなものか。

本書で紹介されている具体的な手段は次の通り。

- コーチングツールとしての[1-on-1](https://svpg.com/coaching-tools-the-one-on-one/)
- コミュニケーションツールとしての[Written Narrative](https://svpg.com/coaching-tools-the-narrative/)
- 目標設定ツールとしての[OKR](https://svpg.com/team-objectives-overview/)

「なんだ、結局そういう話か」と思うだろうか。しかしどうだろう、それを組織規模で“正しく”実践できている例が、果たして世の中にどれだけあるだろう。

- 雑談と現状確認で終了し、フィードバックの一つももらえない1-on-1（そして年に一度の人事評価で突然重大な勧告を受ける）
- 自分の主張を押し通すための一方向かつ無責任なコミュニュケーションツールとして利用され、顧客の生の声・ストーリーやステークホルダーに向けたFAQの存在しないWritten Narrative（もはや「ナラティブ」とは呼べない）
- ビジョンやプロダクト戦略に紐付いておらず、設定した瞬間に8割方終了している無意味なOKRや、マイクロマネジメントの道具として悪用されるOKR[^2]

キャリアの中で、このような間違いを冒さないリーダー（＝コーチ）と一度でも働く機会が得られたのなら、それはどれだけ幸運なことであろうか。

ゆえに、あなたはそのようなリーダーの存在を積極的に求め、経験的に語れることの量と質を増やし、自分がリーダーになるときにはチームを *"Empower"* することの価値と喜びを大いに感じ取ってほしい&mdash;そのようなメッセージを、僕は本書から受け取った。

あくまで「何が良くて、何が危険か」を事例ベースで伝えることが中心であり、「キャリアゴールとしてリーダーを目指しなさい」とか、そういった押し付けがましいメッセージが無いのは前作と合わせて好印象。だからこそ、プロダクトの倫理的側面とキャリアについてかなり踏み込んだ記述があったのは興味深い。

> 「そもそも我々はこのプロダクトを作るべきなのか？」「社会・環境・コミュニティに及ぼしうる影響は？」このようなプロダクトの倫理に関する議論は、Business viability riskの一部として法律やプライバシーと同等に扱われるべき新たな課題であり、その重要性から第5のリスク&mdash;***Ethics risk***&mdash;として独立して議論しても良いほどである。そして、私がアドバイスとして「退職」という選択を勧めることは極めて稀だが、もしあなたの組織が倫理的な配慮を欠いていると思うのであれば、それはおそらく辞めて他の仕事を探すべきタイミングだ。<br/><br/>*※超意訳かつ要約済。原文は [Coaching - Ethics | Silicon Valley Product Group](https://svpg.com/coaching-ethics/) にほぼ同じ。*

当ブログでも繰り返し触れているように、この種の問題はいま個人的に最大の関心事なので大変強く響いた。

- [僕らはなぜ、誰のためにプロダクトを作るのか─行動変容デザインとその倫理的側面](/ja/note/hooked-design/)
- [Reviewing Ethical Challenges in Recommender Systems](/note/ethical-challenges-in-recommender-systems/)
- [Understanding Big Tech's Sustainable Commitment with Word Cloud](/note/sustainability-at-big-tech/)

“簡単“に実装可能なセグメンテーション、A/Bテスト、パーソナライゼーションを無邪気に応用する前に、一歩立ち止まってそのプロダクトの外部性を問いただすこと。そのような客観性と冷静さもまた、昨今のプロダクトチーム・リーダーに求められる重要なスキルと言えるだろう。

[^1]: 製品・組織に応じてデータサイエンティストやユーザリサーチャーなど他の役割も加わることは補足しつつも、書籍内では一貫して軸となる三者に焦点を絞っている。とはいえ、書かれているリーダー論は役割問わず応用可能なものである。
[^2]: 本書では「OKRはプロダクト戦略を着実に実現するためのツールであり、プロダクトチーム単位に設定するもの。個人単位で設定するものではない」と語られている。
