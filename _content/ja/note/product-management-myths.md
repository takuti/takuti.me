---
categories: [エッセイ, 読書記録]
date: 2021-08-12
keywords: [プロダクト, 職業, 仕事, プロダクトマネジメント, プロダクトマネージャー, デザイン, チーム, product, 開発, 信頼]
lang: ja
recommendations: [/ja/note/product-management-and-bullshit-job/, /ja/note/design-engineer/,
  /ja/note/first-quarter-as-a-product-manager/]
title: いい加減、プロダクトマネージャーという職業に幻想を抱くのはやめよう。
---

プロダクトマネージャー (PM) としてのこれまでの私的な経験を踏まえて、『[プロダクトマネジメントのすべて 事業戦略・IT開発・UXデザイン・マーケティングからチーム・組織運営まで](https://amzn.to/3s1E5eo)』を読んで思ったことをつらつらと。

<a href="https://www.amazon.co.jp/dp/B08W51KLQJ?_encoding=UTF8&btkr=1&linkCode=li2&tag=takuti-22&linkId=57e691f2c065cfd2a7e5cce1266b5000&language=ja_JP&ref_=as_li_ss_il" target="_blank"><img border="0" src="//ws-fe.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B08W51KLQJ&Format=_SL160_&ID=AsinImage&MarketPlace=JP&ServiceVersion=20070822&WS=1&tag=takuti-22&language=ja_JP" ></a><img src="https://ir-jp.amazon-adsystem.com/e/ir?t=takuti-22&language=ja_JP&l=li2&o=9&a=B08W51KLQJ" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />

- [プロダクトマネージャーは本当に“魅力的な職業”か](#%E3%83%97%E3%83%AD%E3%83%80%E3%82%AF%E3%83%88%E3%83%9E%E3%83%8D%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC%E3%81%AF%E6%9C%AC%E5%BD%93%E3%81%AB%E2%80%9C%E9%AD%85%E5%8A%9B%E7%9A%84%E3%81%AA%E8%81%B7%E6%A5%AD%E2%80%9D%E3%81%8B)
- [“完璧な世界”など存在しない](#%E2%80%9C%E5%AE%8C%E7%92%A7%E3%81%AA%E4%B8%96%E7%95%8C%E2%80%9D%E3%81%AA%E3%81%A9%E5%AD%98%E5%9C%A8%E3%81%97%E3%81%AA%E3%81%84)
- [良かった点](#%E8%89%AF%E3%81%8B%E3%81%A3%E3%81%9F%E7%82%B9)
  - [「PMはミニCEOである」という言説や「PMとプロジェクトマネージャーの違いは？」というよくある質問に対する補足](#%E3%80%8Cpm%E3%81%AF%E3%83%9F%E3%83%8Bceo%E3%81%A7%E3%81%82%E3%82%8B%E3%80%8D%E3%81%A8%E3%81%84%E3%81%86%E8%A8%80%E8%AA%AC%E3%82%84%E3%80%8Cpm%E3%81%A8%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%83%9E%E3%83%8D%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC%E3%81%AE%E9%81%95%E3%81%84%E3%81%AF%EF%BC%9F%E3%80%8D%E3%81%A8%E3%81%84%E3%81%86%E3%82%88%E3%81%8F%E3%81%82%E3%82%8B%E8%B3%AA%E5%95%8F%E3%81%AB%E5%AF%BE%E3%81%99%E3%82%8B%E8%A3%9C%E8%B6%B3)
  - [「プロダクトの成功」を定義するところから始めることの重要性](#%E3%80%8C%E3%83%97%E3%83%AD%E3%83%80%E3%82%AF%E3%83%88%E3%81%AE%E6%88%90%E5%8A%9F%E3%80%8D%E3%82%92%E5%AE%9A%E7%BE%A9%E3%81%99%E3%82%8B%E3%81%A8%E3%81%93%E3%82%8D%E3%81%8B%E3%82%89%E5%A7%8B%E3%82%81%E3%82%8B%E3%81%93%E3%81%A8%E3%81%AE%E9%87%8D%E8%A6%81%E6%80%A7)
  - [PMの武器は信頼、情熱、共感、論理の4つ](#pm%E3%81%AE%E6%AD%A6%E5%99%A8%E3%81%AF%E4%BF%A1%E9%A0%BC%E3%80%81%E6%83%85%E7%86%B1%E3%80%81%E5%85%B1%E6%84%9F%E3%80%81%E8%AB%96%E7%90%86%E3%81%AE4%E3%81%A4)
  - [一口にPMといっても様々なタイプが存在する](#%E4%B8%80%E5%8F%A3%E3%81%ABpm%E3%81%A8%E3%81%84%E3%81%A3%E3%81%A6%E3%82%82%E6%A7%98%E3%80%85%E3%81%AA%E3%82%BF%E3%82%A4%E3%83%97%E3%81%8C%E5%AD%98%E5%9C%A8%E3%81%99%E3%82%8B)
  - [Part 6「プロダクトマネージャーに必要な基礎知識」が秀逸](#part-6%E3%80%8C%E3%83%97%E3%83%AD%E3%83%80%E3%82%AF%E3%83%88%E3%83%9E%E3%83%8D%E3%83%BC%E3%82%B8%E3%83%A3%E3%83%BC%E3%81%AB%E5%BF%85%E8%A6%81%E3%81%AA%E5%9F%BA%E7%A4%8E%E7%9F%A5%E8%AD%98%E3%80%8D%E3%81%8C%E7%A7%80%E9%80%B8)
- [PMのこれから](#pm%E3%81%AE%E3%81%93%E3%82%8C%E3%81%8B%E3%82%89)

### プロダクトマネージャーは本当に“魅力的な職業”か

まえがきの一文目からツッコみたくなる本というのも珍しいのだが・・・

> 現在、世界で一番魅力的な職業はプロダクトマネージャーではないだろうか。

「[データサイエンティストは21世紀で最もセクシーな職業である](https://hbr.org/2012/10/data-scientist-the-sexiest-job-of-the-21st-century)」と言われてから約9年、今日そんなことを言ったら、もしかしたら鼻で笑われてしまうかもしれない。キャッチーなタイトルによって「データ駆動のビジネス」という考え方の普及には多大な貢献をした一方、上っ面だけの「キレイな話」ばかりが一人歩きしてしまい、データサイエンティストという職業に対して過度な期待や誤解を招く原因になったとも捉えている。

近年、日本のIT（スタートアップ）界隈に巻き起こっているある種の「PM信仰」からは、同様の流れを想起せずにはいられない。そして本書『プロダクトマネジメントのすべて』は、そのような幻想を誘起する恐れのある一冊である、と僕は感じた。

まず、全体として教科書的に「理想」を広く浅く列挙しているだけで軸となるメッセージがなく、結局何が大切なのかが分かりづらい。すでにPMをやっている人が読んで新たに得るものは無さそうだし、これからPMをやる人はこの長大な（カタカナだらけの）目次を見てただ途方に暮れるだけに思える。「PMは魅力的な職業である」という謳い文句から飛躍して、無邪気に「ビジョン策定、アイディア創出、デザイン、開発、法務に関するコミュニケーション、意思決定・・・PMはこのすべてを担う万能人材なのだ！」と勘違いされても困る。

なお、"Myths about Product Management"（PMという職業に関する誤解）を議論した記事はネット上にも数多く存在し、それは日本のPMコミュニティやこの書籍に限った話ではない：

- [Five Dangerous Myths about Product Management](https://medium.com/@noah_weiss/five-dangerous-myths-about-product-management-d1d852ed02a2)
- [5 Product Management Myths…Busted!](https://productschool.com/blog/product-management-2/5-product-management-myths-busted/)

様々なツールやデバイス、ノウハウの普及によって誰もが容易に「プロダクトづくり」に携わることのできる昨今。確かに、ビジネス・テクノロジー・デザインから成る「総合格闘技としてのプロダクトマネジメント力」の重要性は日に日に増している。しかし、そのようなスキルの重要性と「PMという仕事の魅力や価値」は別の問題である。

> 多くの場合、最終的に手を動かしてプロダクトを作るのはPMではない。そして、関係各位と必要最低限のコミュニケーション・調整を行い、無難な決断を下し、タスクを割り振って定期的に進捗を確認するだけなら、あなた以外にもできるひとは大勢いる。もっと言えば、ユーザリサーチャー、ビジネスアナリスト、プロジェクトマネージャーなど、**各仕事をより効果的にこなすプロフェッショナルは他に存在する。ならばPMよ、あなたはなぜそこにいる？** *&mdash;[プロダクトマネジメントは「クソどうでもいい仕事」か](/ja/note/product-management-and-bullshit-job/)*

さらに、職業という括りで見るのであれば、PMのみならずデザインエンジニアなどのBTC型人材も検討の余地があるわけで。

> 限られた人的リソースの中でイノベーションを起こすことのできる、**B**usiness, **T**echnology, **C**reativity **のスキルを兼ね備えたBTC型人材**の存在が不可欠となる。[...] その仕事はデザイン思考で言うところの観察→課題定義→仮説構築→プロトタイプ作成→検証というステップの繰り返しに相当し、**仮説の精度を上げながら自力でプロダクト開発を推進する**。*&mdash;[デザインエンジニアになろう](/ja/note/design-engineer/)*

PMが“魅力的な職業”としてピタリとハマる人もいるだろう。しかし、その仕事を手放しに賛美できるほど単純な話でもない。

### “完璧な世界”など存在しない

Amazonの書籍紹欄には「400ページ超の大充実内容。永久保存版。」とあるが、果たしてそれは誇るべきことなのだろうか。これは「PMの仕事はこんなに分厚い本になってしまうほど多岐にわたる」という事実を元にした開き直りとも読み取れる。その先で読者（と、彼ら彼女らに巻き込まれるチームメンバー）が直面するのは、何でもやろうとして何もできない・・・そんな悲しい未来だ。

参考書に書かれている手法が素直に通用すると信じ込み、"Perfect World" という名の理想郷に生きたい人というのは常に存在する。

- 突然アジャイル/スプリントによる開発をチームに持ち込んでみたり、
- トップダウンによる統制のとれた意思決定プロセスが存在すると信じて疑わなかったり、
- エンジニア・デザイナー・PMの役割を1ミリの重なりもなく明確に分けようとしたり。

気持ちはわかるが、個々のチームメンバーもまた人間であり、まぁ現実はそんなにうまくいかないわけで。

他方、実際のPMの働きは極めて流動的で、一冊の本で体系的にまとめられるようなモノではないはずだ。

> 属する組織の規模や仕組み、製品の種類によってプロダクトマネージャーの役割は大きく異なる。仮に今のチームで世界に轟く大きな成果を挙げたとして、次のプロジェクトで同様に活躍できる保証はどこにもない*&mdash;[僕は「世界で闘うプロダクトマネージャー」にはなれない。](/ja/note/first-quarter-as-a-product-manager/)*

個人的には、いま業界に必要なのは日本の動向・市場にチューニングされた（１）よりコンパクトにまとまったPMという仕事のエッセンスと（２）「その時、あのプロダクトのPMはどう動いたか」という具体的な事例・ロールモデル[^1]ではないかと考える。読者を着実に次の一歩へと駆り立てるような、前向きかつ実践的なコンテンツが望まれる。

### 良かった点

重要なことがうまくハイライトされていない「のっぺりとした一冊」感は否めないが、一方で随所に「これは」と思うような重要な記述が散見されたことも確かであり、著者たちの経験の厚みと、この仕事への理解の深さが読み取れる。

#### 「PMはミニCEOである」という言説や「PMとプロジェクトマネージャーの違いは？」というよくある質問に対する補足

誤解されがちだが、PMに人事権はなく、エンジニアやデザイナーと同じ一人のチームメンバーにすぎない。したがって、全体の意思決定にこそ責任を持つが、メンバーそれぞれの行動や選択のすべてをマイクロマネージするのとは違う。

PMとプロジェクトマネージャーの違いとしては、前者は後者の役割を内包するのに対し、後者は期限の決まったプロジェクトの遂行のみに注力する点が挙げられる。ゆえに、世にあるプロジェクトマネジメントの方法論の多くは、プロダクトマネジメントの現場でも応用可能である。

#### 「プロダクトの成功」を定義するところから始めることの重要性

いきなり「何を作るか」から議論を始めても、そのプロダクトはなかなか成功しない。

1. ミッション・ビジョンといった「プロダクトの世界観」という軸 (Core)
2. ユーザ・市場の動機 (Why) 
3. 提供する体験とビジネスモデル (What)
4. インタフェースおよびシステム設計と実装 (How)

という階層モデルの上にプロダクトを作り上げていくことが重要だ、と著者は言う。プロダクトの世界観、それは「ストーリー」と読むこともできる。

> 価値を生み出すプロダクトに必要なのは、『ストーリー』を軸に据えるのはもちろんのこと、そこに技術とデザインが渾然一体となった実装がなされることではなかろうか。ストーリー駆動で届けたい体験をデザインし、それを適切な技術で実現する。**ストーリーありきのデザインであり、デザインありきのテクノロジーである**べきなのだ。*&mdash;[ストーリーを伝えられないプロダクトの虚しさ](/ja/note/tech-design-story/)*

これに関しては、軸が無いプロダクトのメタファー「[魚でも哺乳類でもない何か](https://note.com/tably/n/n61ee3bcbeea0)」が秀逸なので必読。軸のないプロダクトを作ることほど、PMにとって苦痛で無意味なことはない。

#### PMの武器は信頼、情熱、共感、論理の4つ

WritingにせよSpeakingにせよ、PMの仕事の8割はコミュニケーションである。データを元に論理的にストーリーを展開し、信頼し、信頼され、共感し、共感されなければその仕事は成り立たない。

> 僕にとっての良いPMの指標は何か？それは「**自分の意思決定・発言にどれだけ自信を持ち、仲間を信用し、信用されるか**」である。*&mdash;[僕は「世界で闘うプロダクトマネージャー」にはなれない。](/ja/note/first-quarter-as-a-product-manager/)*

同時に、情熱無くして書籍にして400ページ超の多様な役割・振る舞いをこなすことなど誰にできようか。

> PMに関して言えば、「**プロダクトと自分の間には、むしろ積極的に強固な繋がりを求めなければならない**」というのが僕の仮説だ。「とにかく好き」「自分だからできる」「自分がやらねばならない」という情熱や使命感。それがあるからこそチームはPMを信頼し、確信を持って開発を進めることができ、顧客とのコミュニケーションが自然と促され、結果的に最高のプロダクトが生まれていくのではないか。*&mdash;[プロダクトマネジメントは「クソどうでもいい仕事」か](/ja/note/product-management-and-bullshit-job/)*

#### 一口にPMといっても様々なタイプが存在する

先述の通り、属する組織の規模や仕組み、製品の種類によってPMの役割は大きく異なる。その点についても本書はきちんと言及している。

ひとつはプロダクトのフェーズ・規模による分類。

- イノベータ系PM（0→1のマーケットフィットを意識した新規開発フェーズ特化）
- グロース系PM (1→10)
- タウンビルダー系PM (10→100)

もうひとつは B2C PM と B2B PM の比較。

- 開発のスピード感
- 顧客層とその母数
- 仕様上のトレードオフ
- 課金モデル
- コスト・収益計算

コンシューマ向けか企業向けかによって、プロダクト開発におけるありとあらゆる変数の値が異なる。この点、日本のPM市場はtoCに偏っており、toB PMの絶対数（あるいは彼ら彼女らの社外への露出）が極端に少ない印象があるのだが、どうだろうか。

#### Part 6「プロダクトマネージャーに必要な基礎知識」が秀逸

これも繰り返しになるが、重要なのはPMという職業に就くことではなくて、ビジネス・テクノロジー・デザインから成る「PM力」を身につけてプロダクト開発の現場に活かすことだ。

とはいえ、何を学べば良いのだろうか？PMとして仕事をする上でMBAやコンピュータサイエンスの学位は不要だ。では一体どこまでが「基礎知識」と呼べるものなのだろうか。Part 6ではそのような問いに対して簡潔な指針を与えてくれる。

お金（コスト、収益性、課金モデル）、個人情報保護などの法律と知財管理、効果測定、データ処理・分析、デザイン原則、消費行動モデル（AIDMAの法則）、ソフトウェアテストと品質管理、開発プロセス、クライアントサーバシステム、セキュリティリスクまで。これが過不足の無いチョイスでなかなか「ちょうどいい」。PM業の雰囲気を知りたいのであれば、このPart 6と、Part 1「プロダクトの成功」を眺めるだけでも十分に有意義だろう。

### PMのこれから

冒頭にも触れたように、ねじれて伝わってしまった部分はあれど、「データサイエンティストは21世紀で最もセクシーな職業である」というトレンドが業界の裾野を大幅に拡げたことは確かである。

同様に、現場のPMとしては「そんなに良いもんじゃないですよ・・・」と言いたくなるものの、昨今のPMという職業の認知度向上には目を見張るものがある。それは先人たちの継続的なアウトプットの成果にほかならず、（翻訳ではなく）日本発で『プロダクトマネジメントのすべて』という本が出版されたという事実は大変喜ばしい。

とはいえ、随所で言及されているが、グローバルで見ればPMなんて別に新しくもない「居て当然」の人材なのだ。だからこそ、PMの「なんでも屋さん」感を強調して煽るのではなく、もう一歩踏み込んだ「リアルなPM像」というものに目を向けることが大切なのではないかと、僕は思う。

それはPMがPMのために望むことでもあるし、一緒に働くことになるエンジニアやデザイナーのみなさんの、PMに対する期待値を適切に設定するためにも欠かせない配慮である。

> **他人の仕事の難しさ・勘どころを正しく想像できる者に、私はなりたい**。もちろん専門外の話であればそれを100パーセント理解するのは難しいし、知った気になって軽々しく口を出すのも違う。でもその仕事に向き合う人の“気持ち“を知る努力はできるはずだ。その努力なくして「あのチームは仕事が遅い」「なんでこの程度のモノしか作れないのか」などと批判をするのは大変格好が悪い、と僕は思う。*&mdash;[なぜUI/UXデザイナーの仕事は批判の的になるのか？その謎を解明すべく我々は（以下略）](/ja/note/coursera-ui-ux-specialization/)*

お互いの役割を理解し、得手不得手を尊重し、面と向かった健全なコミュニケーションの下にプロジェクトを推進する。「プロダクトマネジメント力」を行使した先に見ることのできるそんな景色を夢見て、僕らは今日も学び、働くのです。

[^1]: 海外発の書籍『[INSPIRED 熱狂させる製品を生み出すプロダクトマネジメント](https://amzn.to/345iRyE)』や『[世界で闘うプロダクトマネジャーになるための本](https://amzn.to/3lYqjrQ)』も同様の事例が豊富に記載されている。