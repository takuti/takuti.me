---
aliases: [/note/nand2tetris/]
categories: [読書記録, プログラミング, コンピュータシステム]
date: 2017-05-21
lang: ja
title: 『コンピュータシステムの理論と実装』は“娯楽”である
lastmod: '2022-01-18'
keywords: [実装, tetris, nan, 機械語, hdl, hack, コンピュータシステム, 忍耐力, アセンブリ, jack]
recommendations: [/ja/note/recommender-libraries/, /ja/note/cognitive-science-and-behavioral-economics/,
  /ja/note/power-of-language/]
---

途中長いこと放置していたせいで [takuti/nand2tetris](https://github.com/takuti/nand2tetris) の initial commit から1年くらい経ってしまったけど、『**[コンピュータシステムの理論と実装](https://www.oreilly.co.jp/books/9784873117126/)**』を読み終えた。

### 内容

『**コンピュータシステムの理論と実装**』（通称 ***nand2tetris***）は、その名の通りNANDのような論理演算からテトリスのようなアプリケーションの実装までを一気に学ぶことでコンピュータシステム全体を俯瞰しましょう、という一冊。

章が進むにつれてハードウェアからソフトウェアへと話が進んでいき、各章には“プロジェクト”として何らかの実装パートがある。実装の結果は予め用意されたシミュレータやエミュレータを通して確認・デバッグできる。

- [公式サイト](http://nand2tetris.org/)

目次を見るとそれだけでワクワクする：

1. **Boolean Logic**
	- HDLでANDやORなどの論理ゲートを実装する
2. **Boolean Arithmetic**
	- HDLで加算器やALUを実装する
3. **Sequential Logic**
	- HDLでフリップフロップやレジスタ、（部品としての）メモリ、カウンタを実装する
4. **Machine Language**
	- アドレス指定方式やプロセッサ、レジスタの利用などについて、本書のためにデザインされた機械語（Hack機械語）に基づいて解説
	- 乗算や入出力操作をHackのアセンブリで書く
5. **Computer Architecture**
	- HDLで、これまでに実装したコンポーネントを組み合わせて、Hack機械語のビット入力に対応するメモリやCPUを実装する
	- これがハードウェアとしての“Hackコンピュータ”となる
6. **Assembler**
	- アセンブリ→機械語
7. **VM**
	- VMコード→アセンブリ
8. **High Level Language**
	- 本書のためにデザインされた高水準言語Jackの紹介
9. **Compiler**
	- Jackプログラム→VMコード
10. **Operating System**
	- キーボード入力の処理やスクリーンへの描画、ひいてはメモリ操作など、OS的な機能をJack言語で実装する

（アセンブラ、VM変換器、コンパイラは好きな言語で実装してよい）
	
しかし騙されることなかれ。これだけの話題を一冊（1つの授業）に詰め込んでいるので、各章の記述はとても浅い。

著者も繰り返し述べている通り、最適化という最も重要な話題からはほぼ完全に目を背けているし、ネットワークはどこへ行ったという話もある。OSに至っては『OS的な機能をアプリケーションのレベルで擬似的に実装している』にすぎないので、実際の話とは大きくかけ離れている。

とはいえ、基礎的な部分はしっかりと抑えられていた印象。たとえば、よくある「CPUを作りましょう！」という課題は実際にはALUを作っただけで終わるものだけど、この本はもう一歩踏み込んだところまできちんと解説している。

このコンテンツをどう評価するかは人それぞれだけど、まぁとにかく非常にチャレンジングな一冊ということです。
	
### 感想

最初から最後までずっと頭の体操をしている気分だった。これに尽きる。

とにかく広く浅い内容なので、コンピュータサイエンスを修めた人間がこの本から知識として新たに得られるものはほとんど無いと思う。

しかしその浅さ故に、章末プロジェクトたちが『ちょうどいい』のだ。本書のために簡略化された未知のシステム/言語仕様に従って、様々なビルディングブロックをゆるゆると実装してゆく。「ゼロから言語を設計しなさい」という話でもなければ、「ほとんど完成された実装を、あと少し修正して仕上げなさい」という単純さともまた違う。

なので（仕様をよく読まずに実装を始めて何度かハマったけど）難しすぎて無理！ということは無い。落ち着いて取り組めば、忍耐力さえあれば先に進めるはず。

そう、忍耐力ですよ。忍耐力。

おもちゃの世界の仕様書を実装に落とし込むだけなので、やる意義を問うてはならない。

というわけで「これは…コンピュータサイエンス版ナンプレとでも言うべきか…」というのが率直な感想（一応褒めている）。

平日の夜とか、帰り際にカフェに寄るじゃないですか？そこでコーヒーを飲みながら2時間くらい、あーでもないこーでもないと仕様を眺めながら試行錯誤するわけですよ。これが不思議と心地よい。

### 『世界を俯瞰する』ことの大切さ

やる意義を問うな、と書いておきながら、それでもこの本は『上から下まですべてが繋がる』という一点においてとても有意義な一冊だと思った。

書かれている話題のひとつひとつは過去に講義や本、経験を通して学んだものかもしれない。けれど、それらを一歩引いて“コンピュータシステム”という大きな枠組みの中で見つめ直す機会は無かった気がする。

自分の興味が具体化して、専門性が出てきたときこそ、こういった普遍的な知識の全体像の“スケッチ”をインプットし直す機会を大切にしたいなぁと思うのでした。

それで思い出したのが『**思考する機械 コンピュータ**』という本。読み物だけど、これも電気信号（論理回路）のレベルから並列計算、人工知能まで、広い世界を俯瞰できる素晴らしい一冊だった：

<blockquote class="instagram-media" data-instgrm-captioned data-instgrm-version="7" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:512px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:8px;"> <div style=" background:#F8F8F8; line-height:0; margin-top:40px; padding:50% 0; text-align:center; width:100%;"> <div style=" background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAsCAMAAAApWqozAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAMUExURczMzPf399fX1+bm5mzY9AMAAADiSURBVDjLvZXbEsMgCES5/P8/t9FuRVCRmU73JWlzosgSIIZURCjo/ad+EQJJB4Hv8BFt+IDpQoCx1wjOSBFhh2XssxEIYn3ulI/6MNReE07UIWJEv8UEOWDS88LY97kqyTliJKKtuYBbruAyVh5wOHiXmpi5we58Ek028czwyuQdLKPG1Bkb4NnM+VeAnfHqn1k4+GPT6uGQcvu2h2OVuIf/gWUFyy8OWEpdyZSa3aVCqpVoVvzZZ2VTnn2wU8qzVjDDetO90GSy9mVLqtgYSy231MxrY6I2gGqjrTY0L8fxCxfCBbhWrsYYAAAAAElFTkSuQmCC); display:block; height:44px; margin:0 auto -44px; position:relative; top:-22px; width:44px;"></div></div> <p style=" margin:8px 0 0 0; padding:0 4px;"> <a href="https://www.instagram.com/p/1wrZh0RWO2/" style=" color:#000; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none; word-wrap:break-word;" target="_blank">ぼくがひとに本を一冊だけ薦めるならこれ</a></p> <p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;">A post shared by @takuti on <time style=" font-family:Arial,sans-serif; font-size:14px; line-height:17px;" datetime="2015-04-22T02:33:41+00:00">Apr 21, 2015 at 7:33pm PDT</time></p></div></blockquote> <script async defer src="//platform.instagram.com/en_US/embeds.js"></script>

網羅性の高い平易で魅力的な本は「もっと早く出会っていれば…」という感想から「新人/学部1年生に薦めたい」といった扱われ方をされがちだけど、これまでの知見があるからこそそう思えるのであって…なんというか、タイミング…ですね。

以上、nand2tetris本は娯楽として案外楽しく、有意義な一冊だったというお話でした。しかしまぁ、好きなことなら難しい問題だろうがなんだろうが全部娯楽になり得るし、同じ娯楽ならあえてnand2tetris本を手に取る必要はないかな…と書きながら思ったり。

（ところで、nand2tetrisなのに、書かれている内容に従うと最後に起動するアプリケーションがテトリスではなくて Pong という壁当てピンポンゲーム（？）なのはいかがなものか。）