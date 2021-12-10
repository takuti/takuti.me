---
aliases: [/note/chiir-2017/]
categories: [機械学習, 情報推薦, イベント参加記]
date: 2017-03-18
images: [/images/chiir-2017/program.jpg, /images/chiir-2017/city-hall.jpg, /images/chiir-2017/tutorial1.jpg,
  /images/chiir-2017/instagram.png, /images/chiir-2017/human.jpg]
keywords: [chiir, 検索, 情報検索, 会議, 画像, ユーザ, 動画, ノルウェー, web, 情報]
lang: ja
recommendations: [/ja/note/master-graduate/, /ja/note/recsys-2016/, /ja/note/euroscipy-2017/]
title: '情報検索・インタラクション系の国際会議 CHIIR2017 に参加した #chiir2017'
---

2017年3月7日から10日までノルウェー・オスロで開催された情報検索・インタラクション系の国際会議 [The ACM SIGIR Conference on Human Information Interaction & Retrieval 2017](http://sigir.org/chiir2017/) （CHIIR2017;
「ちあー」と読む）にポスター発表者として参加した。

![program](/images/chiir-2017/program.jpg)

▲ Chair氏「プログラム表紙の会議名が間違っていることになぜ誰も気づかなかったのか！」

採択された僕の論文は以下:

- **[Sketching Dynamic User-Item Interactions for Online Item Recommendation](http://dl.acm.org/citation.cfm?id=3022152)**

相変わらずテーマは情報推薦だけど、今回は**部分空間法**や**行列スケッチ**がキーワードになる。

部分空間法を用いてユーザ・アイテムを表現した特徴ベクトルをフィルタリングする、というのが基本的なアイディアで、似たような手法は異常検知の分野で多く見られる。しかし情報推薦の文脈ではこの手のアプローチはあまり研究されていなかった。

部分空間（観測したベクトル列の基底）は特異値分解によって得られる。そして、この基底をオンラインなアルゴリズムで効率的に更新するために行列スケッチを使う。

このテーマ設定は、2年前に[PFNの比戸さんのブログ記事](https://research.preferred.jp/2013/08/sketch/)を読んでから行列スケッチに興味が出て、なんとか応用研究に繋げられないかと考えた結果でもある。また、異常検知と情報推薦の接点という意味では[Treasure Dataインターンの経験](https://takuti.me/note/td-intern-2016/)が助けになった。

<blockquote class="instagram-media" data-instgrm-captioned data-instgrm-version="7" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:512px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:8px;"> <div style=" background:#F8F8F8; line-height:0; margin-top:40px; padding:50.0% 0; text-align:center; width:100%;"> <div style=" background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAsCAMAAAApWqozAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAMUExURczMzPf399fX1+bm5mzY9AMAAADiSURBVDjLvZXbEsMgCES5/P8/t9FuRVCRmU73JWlzosgSIIZURCjo/ad+EQJJB4Hv8BFt+IDpQoCx1wjOSBFhh2XssxEIYn3ulI/6MNReE07UIWJEv8UEOWDS88LY97kqyTliJKKtuYBbruAyVh5wOHiXmpi5we58Ek028czwyuQdLKPG1Bkb4NnM+VeAnfHqn1k4+GPT6uGQcvu2h2OVuIf/gWUFyy8OWEpdyZSa3aVCqpVoVvzZZ2VTnn2wU8qzVjDDetO90GSy9mVLqtgYSy231MxrY6I2gGqjrTY0L8fxCxfCBbhWrsYYAAAAAElFTkSuQmCC); display:block; height:44px; margin:0 auto -44px; position:relative; top:-22px; width:44px;"></div></div> <p style=" margin:8px 0 0 0; padding:0 4px;"> <a href="https://www.instagram.com/p/BRY3QxTFPUH/" style=" color:#000; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none; word-wrap:break-word;" target="_blank">Presented my poster, seriously :)</a></p> <p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;">A post shared by @takuti on <time style=" font-family:Arial,sans-serif; font-size:14px; line-height:17px;" datetime="2017-03-08T19:14:36+00:00">Mar 8, 2017 at 11:14am PST</time></p></div></blockquote> <script async defer src="//platform.instagram.com/en_US/embeds.js"></script>

▲ ポスターセッションでは発表者含め、みんなビール片手に議論していて楽しかった。

### 世界観

情報推薦 (recommender systems) はもともと情報検索 (information retrieval) から派生した分野なので、小さな会議だけど採択されたときはとても嬉しかったし、他の発表もかなり楽しみだった。しかし蓋を開けてみると "interaction" の色が強すぎて、全く違う分野の会議に来てしまった感じだった。

https://twitter.com/takuti/status/839460132950011908

「僕はもっと情報検索の理論的 (theoretical) な話を期待していたんだけど…」と漏らすと「あ〜ということは心理学とかに興味があるんだね？」と返ってくる、そんな世界。

しかしまぁこれはこれで新鮮だった。たとえばLibrary Scienceって国内だと筑波大の図書館情報くらいしか思い浮かばないけど、実際は世界中にたくさん研究者がいて勢いのある分野だということを知った。そんな人たちの世界に触れて、ポスターセッションで議論ができたのは貴重な経験。

CHIIR2017ではRecSys2016の**Past, Present, Future Paper**と似たような趣旨の**Perspective Paper**が別枠で募集・採択されていた。心理学、社会学、図書館情報学、コンピュータサイエンスなど、多くの分野が交わりつつある情報検索の世界、今がターニングポイントなのかな。SIGIR2018からは分野別（トラックごと）に論文募集が行われるという話もあるし。

https://twitter.com/takuti/status/839403781838225408

なお日本からの参加者は他に5,6名ほどいて、マイナーな小規模会議だと思っていた僕はとても驚きました。

![city-hall](/images/chiir-2017/city-hall.jpg)

▲ Welcome Receptionはノーベル平和賞授与式の会場でもあるオスロ市庁舎で行われ、オスロ市長が直々に歓迎のスピーチをしてくれた。ヒトと情報の関わり方に関する研究の大切さを、専門家たちも笑っちゃうくらい詳細に語っていてすごかった。

以下参加したセッションのメモ。

### Tutorial 1: Interactive Search in Video & Lifelogging Repositories

![tutorial1](/images/chiir-2017/tutorial1.jpg)

#### Part I: Video Search

- 情報検索の分野でこれまでやられてきたことと現実の間にはギャップがある
  - たとえば『クエリでキーワードやテキストを指定する』といってもユーザがそんなに明確なイメージを検索前に持っているわけではない
  - 『スケッチを描かせてそれで画像検索』といっても、ユーザはアーティストじゃない
- それも踏まえて動画検索という問題を考えると、これからは **flexible interactive search** を目指すべき
	- ＝ハイブリッドな方法
	- システムは複数の検索手段を用意しておいて、ユーザがそれをインタラクティブに適宜選択できるようにしたい
- **アプローチ1**: ユーザが探索的に探しやすい動画ブラウザ・ナビゲーションの設計
	- 例: [ZoomSlider](http://ieeexplore.ieee.org/document/1521484/)
		- 動画の上部をスライド or 下部をスライドでシークの粒度が変わる
		- 動画内の目的のシーンが近くなったら細かい粒度で探すことができて、
		- 遠いときは荒い留度でスキップしながら探すことができる
	- **いかにユーザの探索的な動画視聴体験を支援するか**、がポイント
		- どんな粒度（e.g., 時間/画像）で、
		- どんな情報（e.g., 色、類似度、動きベクトル、隣接フレーム）を、
		- どのようなインタフェースで提示するか
- どれだけ早く探している情報にたどり着けるか、が重要
	- 良いインタフェースならユーザはいち早く結果にたどり着ける
- **アプローチ2**: Region-of-Interest (ROI) サーチ
	- 検索対象を動画内のある興味領域のみに限定する
	- e.g., サッカー中継動画で、スコアが表示されているエリアに限定して検索すれば得点シーンが割り出しやすい
- **アプローチ3**: サムネの可視化
	- 時間軸、話題の移り変わりをいかにサムネイルという画像列で表現するか
	- 3Dで表現したり
	
何気なく使っている動画再生画面も多くの研究の積み重ねの上に成り立っているんだなーと思うと、先人に感謝しようという気持ちになる。
	
#### Part II: Lifelogging
	
- ライフログ検索の難しさ: **たくさんのセンサから集められたヘテロな情報からいかに検索するか**
- ウェアラブル機器の発展によって、いろいろなログをアグリゲーションするサービスが増えた (e.g., [exist.io](https://exist.io/))
- Visual Lifelogging （画像によるライフログ）も増えてる
	- たとえば食事の写真を撮る行為
		- ちなみに食事の画像からカロリーを推定するのは今最もチャレンジングなタスクのひとつ
	- 画像で記録すると、データが多くなりすぎて探すのが大変
		- 大量のライフログ画像をイベントごとにアノテーション＆セグメント化する、といった研究がある
		- 究極的にはその情報を使って1日を”要約”したい
- この分野の代表的なプロジェクトに Microsoft Research の [MyLifeBits](https://www.microsoft.com/en-us/research/project/mylifebits/) というプロジェクトがある

（このパートはひたすらライフログサービスの紹介を聞かされた感じで、正直微妙だった）

個人的にはセンサデータの解析という文脈でデータストリームについて話してほしかったけど、Open Questionとしてサラッと流されてしまった。残念。

ちなみに発表者の方は[NTCIRのLifelogタスク](http://ntcir-lifelog.computing.dcu.ie/)の主催者のひとりなので、その宣伝もあった。

### Keynote 1: Modeling interactive information retrieval as a stochastic process

https://twitter.com/takuti/status/839462163760693249

- 従来: Mean Average PrecisionなどをMetricとして用いる情報検索
	- 「ユーザがドキュメントをひとつひとつ順番に見たとき」という状況を仮定している
	- ユーザの行動の事前分布に一様分布を仮定しているようなもので、非現実的
- より現実的なのはランキングを考慮した予測モデルの構築
	- 上位のドキュメントに大きな重みを与える
	- たとえばNDCGなんかをMetricにすると、これになる
- 情報検索、そしてインタラクティブ情報検索はユーザのSequential Decision Makingを適切にモデリングする必要がある
	- Google検索を例に取ると、
		- サジェストされた検索ワードの選択
		- 検索結果のタイプ（All, Movie, Image, ...）の選択
		- 検索結果一覧からの選択...
	- これらはすべてranked listからのsequentialなdecision makingと言える
		- **ユーザはランキング形式で提示される結果からの選択行動を連鎖的に繰り返している**
		- いかにしてそのようなユーザのサーチパスを推定するか、という問題で**マルコフモデル**を考える
			- 従来の直線的なユーザ行動ではない、より複雑な意思決定プロセスのモデリング
	- Expected Gainの最大化によって推定を行うモデルとして **The card model** というものがある
		- [Information Retrieval as Card Playing: A Formal Model for Optimizing Interactive Retrieval Interface](http://dl.acm.org/citation.cfm?id=2767761)
		- [A Sequential Decision Formulation of the Interface Card Model for Interactive IR](http://dl.acm.org/citation.cfm?id=2911543)
		- 後者でMarkov Decision Processへの言及

終盤には、書籍検索アプリのUIコンポーネント間の遷移確率をEye Trackingの結果を使ってモデリングしたという独自の実験結果が紹介された。しかし、そのモデルがどの程度現実に即しているのか謎だった。そもそもこのアプリのUIは実験のために作られたものだし…。

と思っていたら、会場から「タイポグラフィや色などのUIデザインによってユーザの行動は変わるよね。それも踏まえて、あなたの実験結果を元に、具体的にUIデザイナーは何ができるのか教えて？」といった趣旨の質問が挙がった。それに対する回答は「自分はもっとFunctionalな部分をみているので、ガワのデザインはまた別の研究になっちゃうね」と。うーん…そんなもんかねぇ…。

### Keynote 3: CSS and user-adapted web presentation

https://twitter.com/takuti/status/840118237819883520

会議4日間で一番よかったコンテンツは間違いなくこのKeynote。特別目新しい話はなかったけど、ユーモア満載でショーとして素直に楽しかった。

- Webの歴史から話は始まって、ブラウザが背景色（グレー）や文字色を勝手に決めてしまっていて辛かった時代を振り返る
	- そして人々（広告主）はきれいなページにするために、画像でいろいろなコンテンツを作成・公開するようになった
- そんな時代に、やっぱりきれいな見た目、美しさは大切だよね、という思いでWeb上のドキュメントの表現手法として提案したのがCSS
	- メディアや目的に応じたuser-adaptableな、シンプルな表現手法を提供する
- それまでブラウザで見る背景色はずっとグレーだったので `background: #...` とかCSSで書いた日にはそれはもうみんなテンション上がった
- Google検索はスタイルをindexingしないけど、人間は見ればその違いがわかる
	- Semanticsから分離された表現、これが大事	
- Web font は良いぞ
	- デザインの幅が広がったのはもちろんのこと、今ではPCに入っていない言語もWeb上で表示できる
	- world-wideになったね、web
- 標準化のつらさはどうしても付きまとう 
	- [Acid2](https://ja.wikipedia.org/wiki/Acid2)　
	- MicrosoftのIEを含めて、みんながんばってます

終盤は彼が現在所属しているOperaの話が多かった。どれだけデータ量削減に力を入れているか、という話。

あと、最近イースター島まで航海した話。完全にただの個人の日記だったけど、「実際にこの目でみるとWikipediaに書かれていることと異なる発見もあった」みたいなことを言っていて、なんか良い話っぽくなってた。ずるい。

さらにWebの未来について、同じノルウェー国内でも地域ごとに新規ドメインを策定して、[Web上のZoneを分けていこうという話](https://secure.edps.europa.eu/EDPSWEB/webdav/site/mySite/shared/Documents/EDPS/Events/16-09-29_BigData_Hakon-Wium-Lie_EN.pdf)があった。『広告の無いドメイン』とか作っていきましょう、みたいな雰囲気。なんでもできるようになった広い広いWebの世界をいかに“住みやすく”するか。

この他に一般セッションもいくつか聞いたけど、そっちはあまり印象に残っていない。

自分の見た限りでは、**実験的にUXの有効性や検索行動の傾向を探る**という共通目標がまずあって、**どんな実験を設定して、結論が有意であることをいかに示すか**が重視されている様子だった。
	
### ノルウェー・オスロの良さ

[前回のRecSys](https://takuti.me/note/recsys-2016/)同様ひとりぼっちの国際会議だったけど、たくさん歩いて、たくさん食べて、たくさんコーヒーとビールを飲んで、最高だった。

![instagram](/images/chiir-2017/instagram.png)

▲ 滞在中に[Instagram](https://www.instagram.com/takuti/)に上げた写真は8枚がビールで、あと1枚はオスロの[Fuglen](http://www.fuglen.com/japanese/)に行ったときのもの。一番おいしかったのは乗り継ぎのヘルシンキ空港で飲んだ濃厚なフィンランドビール **Karhu**。ノルウェービールの定番 **Ringnes** はさっぱりしすぎていてつまらなかった。

会議のオープニングでChairの人が「とても暖かくて物価の安いオスロへようこそ！」と自虐するくらい、寒くて、洒落にならないほど物価の高い街だった。（とはいえ、気候は3月のノルウェー＝2月の北陸や東北の都市部、くらいの印象なので恐れることはない。）物価に関してはペットボトルの水が1本で360円もするし、1回の支払いが500円以内におさまることはほぼ無い。

そこさえ目をつぶると、人は穏やかで優しかったし、ご飯（特にチーズと穀類と魚）も美味しいし、彫刻が街にいっぱいあってテンションあがるし、朝はスズメじゃなくてカモメの鳴き声だし、なんだか全体的にとっても居心地がよかった。

<blockquote class="instagram-media" data-instgrm-captioned data-instgrm-version="7" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:512px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:8px;"> <div style=" background:#F8F8F8; line-height:0; margin-top:40px; padding:50% 0; text-align:center; width:100%;"> <div style=" background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAsCAMAAAApWqozAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAMUExURczMzPf399fX1+bm5mzY9AMAAADiSURBVDjLvZXbEsMgCES5/P8/t9FuRVCRmU73JWlzosgSIIZURCjo/ad+EQJJB4Hv8BFt+IDpQoCx1wjOSBFhh2XssxEIYn3ulI/6MNReE07UIWJEv8UEOWDS88LY97kqyTliJKKtuYBbruAyVh5wOHiXmpi5we58Ek028czwyuQdLKPG1Bkb4NnM+VeAnfHqn1k4+GPT6uGQcvu2h2OVuIf/gWUFyy8OWEpdyZSa3aVCqpVoVvzZZ2VTnn2wU8qzVjDDetO90GSy9mVLqtgYSy231MxrY6I2gGqjrTY0L8fxCxfCBbhWrsYYAAAAAElFTkSuQmCC); display:block; height:44px; margin:0 auto -44px; position:relative; top:-22px; width:44px;"></div></div> <p style=" margin:8px 0 0 0; padding:0 4px;"> <a href="https://www.instagram.com/p/BRxM_sCFBZL/" style=" color:#000; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none; word-wrap:break-word;" target="_blank">そういえばノルウェーで泊まったホテルの朝食バイキングが爆発的に美味しかった。</a></p> <p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;">A post shared by @takuti on <time style=" font-family:Arial,sans-serif; font-size:14px; line-height:17px;" datetime="2017-03-18T06:06:17+00:00">Mar 17, 2017 at 11:06pm PDT</time></p></div></blockquote> <script async defer src="//platform.instagram.com/en_US/embeds.js"></script>

観光地としての素晴らしさも文句なしで、きれいなオペラハウスやオスロ国立美術館（あのムンクの『叫び』が展示されていて館内撮影し放題！）、彫刻公園（広い敷地内に大量の彫刻があって面白い）などがあり飽きない。クルーズ船の運行日の都合でフィヨルドを見れなかったのが心残りだけど、それはまたの機会に。

「修士課程を終えるまでにもう一度国際会議にいきたいなぁ」「できれば未経験のポスター発表がいいなぁ」と思っていたところで見つけたのがCHIIR2017だった。研究分野という意味では少し期待外れだったけど、それでも全体としてはとても充実した楽しい時間を過ごせた。

ACM SIGIRの小規模会議として2016年にできたばかりのCHIIR、来年はアメリカ・ニュージャージー、再来年はスコットランド・グラスゴーでの開催がすでに決定している。参加者は多すぎず交流しやすいし、比較的採択されやすい会議でもあると思うので、情報検索、特にインタラクション(UI, UX)寄りの話題に興味がある方はぜひ。

![human](/images/chiir-2017/human.jpg)

▲ 会場の大学内にあった彫刻です。