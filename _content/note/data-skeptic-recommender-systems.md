---
date: 2017-11-17
lang: ja
recommendations: [/note/trends-in-real-world-recommender-systems-2017/, /note/the-amazon-way-on-iot/,
  /note/coursera-recommender-systems/]
title: Podcast "Data Skeptic" の推薦システム回が良すぎて3回聞いた
---

推薦システムの業界で知らぬものはいない、ミネソタ大学のレジェンド級プロフェッサー[Joseph Konstan先生](http://konstan.umn.edu/)が Podcast "Data Skeptic" に出演していた：

- [Recommender Systems (live from Farcon) | Data Skeptic](https://dataskeptic.com/blog/episodes/2017/recommender-systems-live-from-farcon)

[Courseraの推薦システムのコース](/note/coursera-recommender-systems)でお世話になり、その後 [RecSys 2016](/note/recsys-2016) でユーモア満載の生Konstan先生を見たときはすごく感動したことを覚えている。

振り返れば、RecSys 2016 で他の発表者がアルゴリズム寄りの“普通”の話をしている中、先生のグループ ([GroupLens](https://grouplens.org/)) の研究は真剣に『ユーザ体験』『インタフェース』『HCI』という視点で議論を展開していて、やっぱりこの人はすごい…と感じたものである。推薦システム≠機械学習であり、非常に奥が深い分野なのだと改めて気付かされた。

そんな先生が推薦システムについて語るPodcastエピソードは、とても示唆的で聞きごたえのある内容だった。みんなもぜひ聞いてほしい。

以下、特に印象的だった話題についていくつか。

### “良い”推薦システムとは

「完璧な推薦システムってあるの？」という聞き手の質問に対して、「存在しないし、推薦システムの“良さ”をいかに測るかに依る」と答えるKonstan先生。

従来、推薦システムの評価には機械学習的な方法が用いられてきた。ECサイトなら、ユーザの購入履歴のうち80%でモデルを作って、20%で評価、とった具合。しかし、そんな『放っておいてもいずれ買うような、絶対に好きなモノ』を正しく当てるシステムに意味があるのだろうか？

推薦システムは**薦められなければ絶対に買わなかったであろうモノの中で、ベストなモノ**を提示すべきであり、これは機械学習的な意味の“精度”などでは測れない。

たとえばワインの推薦をするとして、既に好きなワインを正しく予測することがゴールではない。好きなワインに似ていて、より良いワイン―それを推薦して、ユーザの嗜好を広げることが推薦システム本来の役割だと言える。

そのような考え方から、推薦システムの評価指標に関する議論はいまだに続いており、ゆえに『完璧な推薦システム』など定義することすらできないのだ。

### Serendipity = like + didn't expect

既存の評価指標のなかで有望そうなもののひとつに**セレンディピティ**がある。これはどうだろう？

Konstan先生は **Serendipity = like + didn't expect** の組み合わせで達成されるのだと言い、その意味を決して履き違えないことだと警笛を鳴らす。たとえセレンディピティを議論するのだとしても、まずはユーザの嗜好を正しくモデリングできることが前提だ。

推薦システムの研究で、精度が出ないときに「セレンディピティ的には有望」という言い訳をするひとがいるが、精度が出ていないのなら嗜好 (**like**) のモデリングにはおそらく失敗しているわけで、それはセレンディピティでもなんでもない。**bad + didn't expect = just "BAD"** である。

### Cycling and Serpentining

聞き手がKonstan先生のグループの [CSCW2017](https://cscw.acm.org/2017/) の論文 "**[Cycling and Serpentining Approaches for Top-N Item Lists](https://dl.acm.org/citation.cfm?id=2998211)**" について質問していて、この研究がなかなか面白い。

<iframe src="//www.slideshare.net/slideshow/embed_code/key/zjZEohHOa3yb9U" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/QianZhao12/toward-better-interactions-in-recommender-systems-cycling-and-serpentining-approaches-for-topn-item-lists" title="Toward Better Interactions in Recommender Systems: Cycling and Serpentining Approaches for Top-N Item Lists" target="_blank">Toward Better Interactions in Recommender Systems: Cycling and Serpentining Approaches for Top-N Item Lists</a> </strong> from <strong><a href="https://www.slideshare.net/QianZhao12" target="_blank">Qian Zhao</a></strong> </div>

この論文ではTop-N推薦の結果を表示する際のテクニックとして、2つの新しい考え方 "**Cycling**" と "**Serpentining**" を提案し、実験を行った：

- **Cycling**
  - 推薦結果を何回も見ているユーザに対してはTop-Nリストを回転させて、上から順に第5, 6, 7, 8, 9, 10, 1, 2, 3, 4位のような順番で表示させたりする
- **Serpentining**
  - 複数ページに渡って推薦結果が表示されるとき、予測の上位アイテムを各ページに分散させる
  - たとえば、1ページ目には第1, 3, 5位のアイテム、2ページ目には第2, 4, 6位のアイテム…といった雰囲気

Top-N推薦の結果を素直に第1, 2, 3, ..., N位の順で表示していると、ユーザはいつも同じ推薦結果を見ることになって退屈だ。なので推薦リストの Cycling と Serpentining によって、ユーザにもっと目新しい推薦結果を提示しよう、という話[^1]。聞き手はこの『目新しさ』の重要性をウィンドウショッピングで例えていて、なるほどと思った。

[RecSys 2016](http://localhost:1313/note/recsys-2016/) の Industry Session で、ニュースサイト [Bloomberg](https://www.bloomberg.com/asia) が「フロント側ではあえてTop-Nリストをシャッフルして表示している」という話をしていたけど、まさにそれと似たようなモチベーションだろう。

『Top-Nアイテムをソートして表示する』という世の中の“当たり前”を疑い、HCIの文脈でその問題を真面目に考え、実サービスの上で実験を行う…この姿勢がこの分野を切り開いてきた [GroupLens](https://grouplens.org/) というグループのカッコよさだと思う。

推薦システムに限らず、昨今のアプリケーション寄りの研究は "Online Experiment" の有無が勝敗を分けることも多い。その点、自分たちの持つ [MovieLens](https://movielens.org/) というサービスの上で多くのユーザを対象に実験ができる GroupLens は強い。そんな彼らならではの実験設計の際の心がけが聞けたのも面白かった。実験対象ユーザを幾つもの設定で細かくグループ分けするのではなく、2〜3の少ない要素でグループ分けして、あとは各ユーザの行動ログが全てを物語るのだという姿勢。

### "I hate Amazon's first page"

この Podcast エピソードで最高なのは、Konstan先生の口から出たこの一言。[Amazonの推薦システムがこの業界で果たしてきた役割は大きい](/note/two-decades-of-amazon-recommender/)が、いまのAmazonの推薦、特にトップページの推薦は大変お粗末なものである。

サービスのトップページは、ユーザの興味を広げたり、なにか“新鮮”な情報を提示するのに最高の場所。なのに、Amazonは最近の閲覧履歴に基づいて類似商品を列挙しているだけで、なんの工夫も感じられない。

この問題は、Konstan先生のレストランメニューの例えが分かりやすい。レストランのメニューには『固定メニュー』と『限定メニュー』（季節モノやランチメニューなど）があり、テーブルの上に置かれる際は一番上に限定メニュー、その下に固定メニューとなっていることが多い。なぜなら、一番上の一番目を引く場所は、お客さんに新しいモノを“オススメ”するには最高の場所だからだ。

一方、個別の商品ページでは、類似品の中で（値段的、質的に）より良い他の選択肢を示すことに注力してほしい。こんな商品はどうですか？と無関係なモノを出すことは期待していない。

Amazonの推薦を神格化する時代はすでに終わっており、大きなサービスのやっていることが常に“正解”とは限らない。1ユーザとして「この推薦ダメだな」と思ったのならその感覚はたぶん正しくて、そこにより良い推薦システム、新しい推薦のカタチのヒントがあるんだと思う。

### これからの推薦システム

業界のレジェンドは推薦システムの未来に何を見るのか。

1つは教育分野への応用。コンピュータを使った授業も増え、（初等）教育のあり方が多様化しているにも関わらず、授業というものは未だにシーケンシャルに進行する。先生の教え方や教材はそれぞれ異なり、ひとりひとりに合った学習方法があるはずなのに、「5つの学習スタイルのうち好みのモノを1つ選択してください」というカタチの教育にはなっていない。今後はそういった方向に世の中が変わっていくはずで、そこに推薦手法が応用できるのではないか、という考え。

また、GroupLens としては音声など異なるインタフェースを用いた際の推薦システムのあり方を考えている。

そして、Konstan先生の個人的な興味は、今も昔も『正しい評価指標とはなにか』というところにある。

いずれにせよ、"Recommender Systems" は "Machine Learning" や "Artificial Intelligence" のサブセットではなく、それらを手段とした個性的な分野であり、今後も多様な展開が期待できる。くれぐれも、この魅力的な分野をアルゴリズム的な側面だけで捉えないことだ。そんなことを改めて強く感じた、素敵なインタビューでした。

[^1]: ただし検索エンジンは例外。検索結果第2位が10ページ目とかに存在するのが好ましいはずがない。