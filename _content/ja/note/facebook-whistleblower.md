---
categories: [エッセイ]
date: 2021-10-09
keywords: [プロダクト, facebook, ソフトウェア, 開発, sns, アルゴリズム, テック, 倫理, 専門家, 利益]
lang: ja
recommendations: [/ja/note/empowered/, /ja/note/hooked-design/, /ja/note/product-management-myths/]
title: Facebook内部告発の件、他人事ではない。
---

テック系メディアの枠を超えた幅広い媒体での連日の報道を見て、何やらとんでもなく歴史的な瞬間に立ち会っているような気分になってきた。興奮さめやらぬうちに、個人的に思ったことを書き留めておく。

今週、アメリカ上院の公聴会の場で行われたFacebook元従業員による証言。それは、同社が「Facebook, Instagram上の一部デジタルコンテンツは子供に対して有害である」という事実を十分に理解しながらも、莫大な利益を優先して配慮を欠いたランキング（コンテンツ推薦）アルゴリズムを採用し続けている、というもの。結果として、10代の若者を中心にSNSが原因による深刻なメンタルヘルスの問題が起きている、と。そして、奇しくもこの証言と前後する形で同社サービスが長時間ダウンした。

- [フェイスブックは「子供に害を及ぼし、民主主義を弱める」　元従業員が米議会で証言](https://www.bbc.com/japanese/58811928)
- [Facebook内部告発者「安全より利益優先」　米公聴会](https://www.nikkei.com/article/DGXZQOGN050IP0V01C21A0000000/)
- [FacebookのInstagramを含むすべてのサービスに障害　社内でのBGP更新が原因と専門家【復旧済み】](https://www.itmedia.co.jp/news/articles/2110/05/news074.html)

何らかの形でソフトウェアプロダクトの開発に携わっている者として、これは「自分はリテラシーがあるし、そもそもSNSなんてもうほとんど使っていないから大丈夫」では済まされない話であると感じた。

SNSが社会に与えうる悪影響に関する議論は近年、陰謀論やヘイトスピーチの文脈でも繰り返し行われてきた。ただ、それらはいずれも一部の“専門家”による大衆に響かない警笛の域を出ていない。一方で、ここ一週間の出来事は今までにないほど世間の注目を集めており、これから事態が大きく動く可能性を示唆している。

個人的に、一連のニュースのポイントは次の3つ。

1. タイミングよく発生した大規模なシステム障害によって、多くの人が一時的に「FacebookやInstagramの無い世界」を経験し、証言がメッセージ性を強めたこと
2. 結果、テック企業が倫理よりも利益を追求することの弊害と、そこに対して『アルゴリズム』というモノの果たす役割が一般に周知されたこと
3. 告発者・[Frances Haugen氏](https://en.wikipedia.org/wiki/Frances_Haugen)は元Facebookのプロダクトマネージャーであり、キャリアを通してGoogle, Yelp, Pinterest等の企業でソフトウェアプロダクト開発の現場に立ってきた方であるということ

エンジニアであればこの規模のシステム障害は「明日は我が身」な話で全く笑えないわけだが、「他人事で済まされない」というのはそういう意味ではない。

利潤追求のためだけに有害なプロダクトを開発し続けるテック企業を揶揄して、公聴会の場では "Big Tobacco" とまで言われてしまう有り様。テクノロジーに魅せられ、その可能性を信じて業界で働いている者として、このような認識が広まってしまうことは素直に悲しい。

たとえ明確な中毒症状が出ていなくても、ニコチン、アルコール、カフェインのように「一度断ってみる」ことで気付かされることは多い。悲しいかな、その点において昨今のソフトウェアプロダクトの多くは既にそのようなアブナイ存在の仲間入りを果たしている。ところが、このような視点を踏まえたデザイン・技術に関する意思決定の議論がプロダクト開発の現場でなされることは極めて稀である。ベイプ（水蒸気タバコ）、ノンアルコール飲料、デカフェコーヒーに相当するソフトウェアプロダクトのあり方を、僕らは一体どこまでリアルに思い描くことができるだろうか。

というわけで、システム障害という形で「プチSNS断ち」を経験した社会からの圧力・注目は計り知れず、この先どこへ向かうにせよ、この一週間の出来事は世界にとって大変有意義なものであったと言える。

結果、公聴会の場では何が起こったか。The New York Timesのポッドキャストで言及されていたことではあるが、「（民衆の代表であり、必ずしも技術に理解が深いわけではない）政治家が『アルゴリズム』というモノの詳細に関心を示した」という事実。これは大変味わい深い現象だ。

<iframe allow="autoplay *; encrypted-media *; fullscreen *" frameborder="0" height="175" style="width:100%;max-width:660px;overflow:hidden;background:transparent;" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-top-navigation-by-user-activation" src="https://embed.podcasts.apple.com/us/podcast/the-facebook-whistle-blower-testifies/id1200361736?i=1000537716296"></iframe>

「何をどのような形でユーザに提示するか」は『アルゴリズム』によって設計・操作が可能なものであり、だからこそサービス開発者には慎重な判断が求められる。そしてFacebookの言う "Engagement-based ranking" はユーザのサイト滞在時間を増大させ、企業利益を最大化するためのアルゴリズムであり、そこに問題がある。

アルゴリズムは決してブラックボックスではなく、そこには確かに作り手の意図が介在する余地がある。それは書き下せば当たり前のことではあるのだが、この気付きから“非専門家”が得るであろう知見は「配慮を怠ることは紛れもなく“悪”である」というものだ。

> “簡単“に実装可能なセグメンテーション、A/Bテスト、パーソナライゼーションを無邪気に応用する前に、一歩立ち止まってそのプロダクトの外部性を問いただすこと。そのような客観性と冷静さもまた、昨今のプロダクトチーム・リーダーに求められる重要なスキルと言えるだろう。*&mdash;[ソフトウェアプロダクトマネジメントのバイブル "Inspired" の続編 "Empowered"、わかりみが深い。](/ja/note/empowered/)*

昨今、企業の社会的責任といえば「サステナビリティ」だが、今回論点となっている倫理的配慮も人類・生命・コミュニティの持続可能性を考える上で非常に重要な要素である、という点は見落とされがちだ。実際、大企業にとって環境負荷軽減や自然保護など持続可能性のハード面を語るのは“簡単”である一方、倫理・社会・コミュニティといった人を中心とするソフト面のメッセージ発信は圧倒的に不足している (c.f. "[Understanding Big Tech's Sustainable Commitment with Word Cloud](/note/sustainability-at-big-tech/)")。どれほど分かりやすい取り組みでポジティブなイメージを植え付けようとしても、自然と人の両輪で回ってこその持続可能性であり、そもそもの売り物（プロダクト）に問題があっては話にならない。

各社が「何もやっていない」とは思わないし、社内に倫理委員会などを設けている企業もあると聞く。しかし、それが権力（経営陣を中心とする指揮系統）から完全に独立し、かつ組織図の末端に至るまでの全社的な教育や意思決定プロセスの是正に繋がっているのかというと、まだまだ道のりは長そうだ。

そして究極的には、そのような“悪”に加担している個々の従業員、つまり自分自身にも責任は伴う。この点において、今回のFrances Haugen氏の言動は我々に多大な勇気を与えてくれる。

大企業のプロダクト組織に属する人間の中にも、同種の問題意識を抱いている者は確かに存在する。そしてソフトウェア倫理という未成熟の分野において、声を上げることによって議論・変化を促進することがいかに重要であるか。一連のニュースによって届けられたこのようなメッセージは、極めて前向きで希望に満ちたものであると言える。

収益や滞在時間を目的関数とした利己的なアルゴリズム開発・プロダクトデザインを止め、自分が開発しているシステムがデプロイ後にエンドユーザの生活に及ぼす影響を想像する事。そのために、まずは一個人として引き続きインプットとアウトプットを続け、同僚・同業者と議論の機会を積み重ねていくことに尽力したい。1人でも多くのエンジニア、デザイナー、プロダクトマネージャー、あるいはデータサイエンティストが共通の認識を持つことのできる未来に向けて、世界は少しずつ、着実に変わりはじめている。

なお、同種のトレンドはアカデミアにも見ることができる。個人的な見解として、推薦システムのトップカンファレンス RecSys 2021 のトレンドは「エンドユーザの存在」を推薦手法に明示的に織り込むことにあった (c.f. "[User-Centricity Matters: My Reading List from RecSys 2021](/note/recsys-2021/)")。それは従来の精度に基づく最適化のみでは到達しえない境地であり、今後の展望が大変楽しみである。