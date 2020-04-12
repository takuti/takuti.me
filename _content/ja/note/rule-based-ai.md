---
aliases: [/note/rule-based-ai/]
categories: [機械学習, 日記, データサイエンス]
date: 2017-10-21
lang: ja
recommendations: [/ja/note/from-cloud-to-ai/, /ja/note/2020/, /ja/note/the-amazon-way-on-iot/]
title: ルールベースは『人工知能』か
---

いま、世の中は空前の人工知能ブームである。あれもこれも人工知能、こっちだってAI、そっちはディープラーニング。『ファジィ』という言葉が流行り、ファジィ炊飯器などが大量に出回った90年代を想起する先輩方も多いらしい。

一方で、バズワードとしての『人工知能』を鼻で笑うエンジニア、研究者、学生もいる。彼らは世間の期待と現実のギャップを理解している。だからこそ、そんなバズワードを安易には受け入れない。

この現状に何を思うか。

僕だって、会話の中で **AI** という単語がでると胸がザワザワするのが正直なところ。しかし、じゃあその言葉が使われなくなれば良いのかというと、それもちょっと違う気がする。

はむかず先生の記事『[「人工知能」という言葉について考える](http://www.silveregg.co.jp/archives/blog/1175)』を読んで触発されたので、この『人工知能』という言葉の使われ方・使い方について、個人的な気持ちを書きなぐってみる。

### 言葉の定義は大きな問題ではない

まず、『人工知能』という言葉の定義については僕も「何が人工知能であるかは、必ずしもはっきりと境界線を引けるものではないし、引く必要もない」と思う。

もちろん定義がハッキリしていないと、お客さんの「AIでいい感じにやってほしい」という期待と、こちらがイメージする具体的な手法でできることの間にギャップが生じて危険だ。

が、これは別に人工知能に限った話ではない。

たとえばWeb制作の現場では、お客さんの要望は「いい感じのホームページが作りたい」であり、そこから製作者はデザインを考え、CMS利用やらJSのライブラリやら、具体案な実現手法をイメージしていく。詳しく話を聞いてみると、実は「ホームページで商品を売りたい」らしい・・・とか、日常茶飯事である。

言葉の意味を予め明確にして、曖昧な言葉は使わない―それは素晴らしい姿勢だけど、使われたときにコンテキストを紐解き、具体的な他の言葉に噛み砕いていく過程のほうがはるかに重要。

### 嫌でもその言葉を使わなければならないタイミングはある

「いやいや俺は曖昧な言葉は一切使わない主義だ」という方もいるでしょう。ただ、マジックワード『人工知能』が嫌いだろうが好きだろうが、それを使わなければならない、使うべきタイミングというものが存在するのもまた事実。

たとえばセールストーク。どれほどハイレベルな技術スタックとアルゴリズムを組み合わせて作ったモノでも、使ってもらえなければ意味がない。そのためには、光り輝くマジックワードを織り交ぜた宣伝活動も時として重要である。それが競合との勝敗を分けることだってあるのだから。

または、お偉いさんに提出する申請書類。なんの説明もなしに専門用語を並べて威圧したら申請却下待ったなしである。導入部分が「人工知能の活用」で始まるのは悪いことではない。そういう抽象的な話から、徐々に具体案を語っていけばよい。そのような書類から予算が生まれ、近年の周辺技術の発展が支えられているのも事実だしね。

ただし限度はある。相手の無知を利用してマジックワードを乱用した文章で翻弄し、中身のないモノを作って売るのは詐欺と言っても過言ではない。

### ルールベースのような単純な処理を人工知能と呼んでいいのか？

ではその限度がどこにあるのか。ルールベースで動く製品を『人工知能』として売るのはどうなのか。

個人的に、人工知能の本質はそこにはないと思っている。求められるのは常に“ふるまい”としての人工知能“らしさ”である。だからこそ、単純な処理だって人工知能になり得るという認識がもっと広がってほしい。

マジックワードが使われたときにコンテキストを紐解き、具体的な他の言葉に噛み砕いていく過程が重要だと書いたけど、

- 人工知能 → 機械学習 → （アルゴリズム名）

という変換が脳内で発生したら、「おっといけない。もっとシンプルな方法があるんじゃないか？」とブレーキをかけたい。

ルールベースで対応できる案件かもしれないし、自然言語処理という名の正規表現で十分なときだってある。数式だって必ずしも微分積分する必要はない ("[Do the Math](/note/the-amazon-way-on-iot/)")。あなたの考える根拠のないファンシーな手法よりも、そっちのほうがずっと現実的で人工知能“らしい”ものになるかもしれませんよ。

同様に、「いい感じのホームページが作りたい」という要望に対して、完成したものがどれだけ最新の技術的なトレンドを取り入れていようが、お客さんにとってそんなことはどうだったいい。成果物の“ふるまい”が全てである。

### 結局『人工知能』とは何なのか

この答えは人それぞれで、そこを見極めるためにはまず歴史を知ることも重要だろう。

僕は『期待に応えて人工知能“らしい”出力をする、「おぉすごい」と思ってもらえるもの』が人工知能だというスタンスで、それを満足する限りルールベースだって正規表現だってAIの一部だと思っている。この点は以下の書籍に影響された部分も大きくて、昔ブログでもまとめた：

<div class="booklink-box" style="text-align:left;padding-bottom:20px;font-size:small;/zoom: 1;overflow: hidden;">
<div class="booklink-image" style="float:left;margin:0 15px 10px 0;"><a href="http://www.amazon.co.jp/exec/obidos/asin/4022735155/takuti-22/" name="booklink" rel="nofollow" target="_blank"><img src="http://ecx.images-amazon.com/images/I/41luUaSrmXL._SL160_.jpg" style="border: none;" /></a></div>
<div class="booklink-info" style="line-height:120%;/zoom: 1;overflow: hidden;">
<div class="booklink-name" style="margin-bottom:10px;line-height:120%"><a href="http://www.amazon.co.jp/exec/obidos/asin/4022735155/takuti-22/" rel="nofollow" name="booklink" target="_blank">クラウドからAIへ アップル、グーグル、フェイスブックの次なる主戦場 (朝日新書)</a></div>
<div class="booklink-powered-date" style="font-size:8pt;margin-top:5px;font-family:verdana;line-height:120%">posted with <a href="http://yomereba.com" rel="nofollow" target="_blank">ヨメレバ</a></div>
</div>
<div class="booklink-detail" style="margin-bottom:5px;">小林雅一 朝日新聞出版 2013-07-12    </div>
<div class="booklink-link2" style="margin-top:10px;">
<div class="shoplinkamazon" style="display:inline;margin-right:5px"><a href="http://www.amazon.co.jp/exec/obidos/asin/4022735155/takuti-22/" rel="nofollow" target="_blank" title="アマゾン" >Amazon</a></div>
<div class="shoplinkkindle" style="display:inline;margin-right:5px"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/B00DZC0SI4/takuti-22/" rel="nofollow" target="_blank" >Kindle</a></div>
<div class="shoplinkrakuten" style="display:inline;margin-right:5px"><a href="http://hb.afl.rakuten.co.jp/hgc/10952997.eae88ca3.10952998.38cdd415/?pc=http%3A%2F%2Fbooks.rakuten.co.jp%2Frb%2F12382345%2F%3Fscid%3Daf_ich_link_urltxt%26m%3Dhttp%3A%2F%2Fm.rakuten.co.jp%2Fev%2Fbook%2F" rel="nofollow" target="_blank" title="楽天ブックス" >楽天ブックス</a></div>
</p></div>
</div>
<div class="booklink-footer" style="clear: left"></div>

- [人工知能関連技術の発展、それすなわちUI革命](/note/from-cloud-to-ai/)

まったく新しいユーザ体験を提供する手段としてのAI、という考え方は大好き。Amazonの『IoT』というバズワードに対する見方も似ていた：

- [The Amazon Way on IoT - Amazonのビジネスから学ぶ、10の原則](/note/the-amazon-way-on-iot/)

### まとめ

別に僕は「みんなもっとカジュアルに『人工知能』という言葉を使おう」とか思っているわけではない。けど、別にその言葉を毛嫌いする必要もないよなーという気持ち。それを書きたかった。案の定まとまりのない駄文となってしまったけど、たまにはこういうのもいいでしょう。

というわけで、[タイトルにAIという言葉を冠してセミナーでお話します](http://www.silveregg.co.jp/archives/event/1183)。AI、あるいは推薦アルゴリズムについて、楽しく議論できましたら幸いです（宣伝）。

(そういえば、似たようなマジックワードに『ロジック』というものがありますね…)