---
categories: [データサイエンス, ビジネス]
series: [malawi]
date: 2023-09-29
lang: ja
title: アフリカの小国にて、データ保護の実態に見る途上国開発・国際協力をめぐるジレンマ。
images: [/images/data-protection-law-in-malawi-2023/me-speaking.jpg]
keywords: [保護, protection, マラウイ, データ, malawi, law, 現地, gdpr, data, 短期]
recommendations: [/ja/note/digital-malawi-2023/, /ja/note/one-year-in-malawi/, /ja/note/relativize-and-contextualize/]
---

[世界最貧国のひとつ・マラウイにおける「デジタル化」の実態](/ja/note/digital-malawi-2023/)は、未だ厳しいものであった。とはいえ、ゆっくりと、それでも着実にインターネット、コンピュータ、スマートフォン、ソーシャルメディアが国民に普及しているのもまた事実であり、僕がアドバイザーとして携わっている現地団体での業務の大半も、このような情報技術の利活用にまつわるものである。そこで気になるのは、テクノロジーに付随するデータの取り扱いだ。

Webサイトの立ち上げ、スマートフォンアプリの開発、オンライン決済の実装、デジタルマーケティングなど、Web2.0以降のテクノロジー利用において個人の属性・行動データの存在は切っても切れない。また、ブロックチェーンやIoT、AIなど、考えうる様々な応用は膨大なデータと計算資源に依存するものであり、だからこそ僕は[プロダクト開発者たちの倫理観](https://offers.jp/media/sidejob/workstyle/a_2103)と[この世界におけるデータ・情報の流れの歪さ](/ja/note/how-information-flows/)を憂いている。加えて、途上国における開発プログラムの実装にはモニタリング・評価というタスクが常に付き纏い、関わった人々の年齢、ジェンダー、居住地や連絡先といった個人情報の収集と分析が絶えず行われている。

そのような背景を踏まえて、ここマラウイで僕はいち開発者としてどのように「データ」と向き合うべきか？

ここで難しいのは「データ保護は大事。だからそれを扱う者に対する制約は厳しければ厳しいほど良い」とも言い切れない点であり、GDPRやCCPAに見られるように、その「標準規格」はコンテクストに強く依存する。[Yahoo! JapanがGDPR準拠の難しさを理由にヨーロッパから撤退したニュース](https://www.nikkei.com/article/DGXZQOUC015NP0R00C22A2000000/)は記憶に新しく、「正しいこと」をするためには相応のコストがかかるという事実を改めて教えてくれる。したがって、ユーザ理解の甘さはプロダクト・サービスそれ自体を中途半端なものにするだけでなく、開発者自身の問題を一層複雑にするだけの「劇薬」ともなりうる。

さて、アフリカ大陸南東部の小国・マラウイにおける「コンテクスト」の理解。それは、未だデータ保護法の類が存在しないという事実を受け入れることに始まる。とはいえ「何もしていない」わけではなく、重要なドキュメントとして次の3点がある。

1. 1994年に制定された[マラウイ憲法](https://www.malawi.gov.mw/index.php/resources/documents/constitution-of-the-republic-of-malawi)には「個人のプライバシーの権利」に関する項目があり (Section 21)、*"interference with private communications, including mail and all forms of telecommunications"* にも言及されている。
2. 2016年に公開された [Electronic Transactions and Cybersecurity Act No. 33](https://macra.mw/download/electronic-transaction-and-cyber-security-act-2016/) では、個人データの定義やその取り扱いにおける注意点など、世界各国のデータ保護法に見られるような基本的な枠組みの構築が試みられている。
3. 2021年には [Data Protection Bill](https://digmap.pppc.mw/data-protection-bill-draft/) が一般公開され、関係者各位から意見が収集された。この法案は先のAct No. 33をはじめとする過去の様々な議論を統合し、個人データ保護にまつわる法的枠組みを定めることを目標としている。

某メディアが *"[Data Protection Law on the Horizon in Malawi](https://cipesa.org/2021/06/data-protection-law-on-the-horizon-in-malawi/)"* と報じたように、Data Protection Billによってマラウイもデータ保護の標準化に向けてあと一歩のところまで来たのだが、そこから先のニュースはまだない。およそ2年後・2023年7月の時点でさえ未だ *"[Malawi needs data protection law](https://www.nyasatimes.com/malawi-needs-data-protection-laws-against-exploitation-suleman/)"* と言っているので、お察しである。そんなわけで、United Nations Economic Commission for Africaによる2022年のレポート [Digital Trade Regulatory Integration: Country Profile - Malawi](https://repository.uneca.org/handle/10855/48137) にも見られるように、政府やビジネスのデジタル化に際して、テクノロジー以前の基礎・基盤さえ整っておらず「まだまだ」というのが現実のようだ。

そんな背景もあって、僕が携わってきたビジネスや教育の現場を見る限り、マラウイ国内でデータ保護に関する話は全くといっていいほど耳にしない。2か月間観察してみて、これは概ね次のようなロジックではないかと、僕は分析している。

- ネットワークインフラが整っていない。ゆえに、デジタルリテラシーを語る側も語られる側も、今ひとつその内容がピンとこない。
- そんなことよりも「明日」のための短期的なリソース確保が最優先。だから *[The Social Dilemma](https://www.thesocialdilemma.com/)* や *[The AI Dilemma](https://www.youtube.com/watch?v=xoVJKj8lcNQ)* で語られるような「未来」のリスクにまで目が届かない。これは気候変動・環境問題の文脈でも共通する課題で、途上国においてその優先度は極めて低い[^1]。
- 結果として、先述の通り関連する法整備は遅々として進まず、企業やNGO、教育機関などもこの話題について真面目に議論する「理由」がない。
- 仮に「理由」ができたとして、議論の中心にいるステークホルダーや社会実装の核を担う現地の人々の知識と経験が圧倒的に不足しており、適切なアクションプランが立てられない。
- 海外からの支援は短期（長くても数年）の経済的なもの、あるいは人的でも極めて局所的な取り組みが主であり、現地への真の知識・技術伝承および持続可能性の点では課題が山積。

![garbage](/images/data-protection-law-in-malawi-2023/garbage.jpg)
▲ 優先度が先進国の「それ」とは大きく異なるので、町は絶望的に汚い。

もちろん全て僕個人の見解ではあるのだが、生まれも育ちもスキルも異なるマラウイ人の友人たちからヒアリングして得られた内容も含むので、それほど大きく外していないものと期待する。

そのような社会で、国内の企業・団体が何か少しでもデータ保護の実践に向けてできることはないのだろうか。そもそも「プライバシーポリシー」の類を公開している組織を見つけることさえ困難なのだが、限られた“事例”を挙げると次の通り。

- 政府機関：[マラウイ警察](https://www.police.gov.mw/about-us/privacy-policy)
- 金融機関：
  - [National Bank of Malawi モバイルアプリ](https://www.natbank.co.mw/mobile-app-privacy-policy)
  - [First Capital Bank](https://www.firstcapitalbank.co.mw/privacy/)
- 通信事業者：
  - Airtel
      - [著作権およびプライバシー](https://www.airtel.mw/copyRightPrivacy)
      - [Webサイト利用規約](https://www.airtel.mw/termCondition)
  - [TNM](https://www.tnm.co.mw/personal/support/privacy-policy/)

非常にベーシック。だが、それでいい。法律が無いわけだし、5年後にどうなっているかもわからないので、過度な最適化はリスクにもなりうる。問題は、おそらく[Privacy Policy Generator](https://www.termsfeed.com/privacy-policy-generator/)のようなテンプレートから生成したのだろうが、各組織内外のステークホルダーたちがこのようなコミュニケーションの意義と重要性、その背景をどれだけ理解しているかにかかっている。ただ「なんとなく」で他のサービスを見ようみまねでコピペしていたのだとすればあまり褒められたものではなく、無理解はメンテナンスされない腐ったポリシーと、将来的な対応の遅れを招く。

したがって、「デジタルリテラシーを語る側」のリテラシー教育を、ビジネス開発あるいは国際協力の文脈で協調しながら進めていくことが先決だと、僕は考える。まずは、すでにお付き合いのある国内外の団体と勉強会を開くなり相互レビューの体制を整えるなりして、データ保護を真面目に考え続けるための土壌を育むことだ。その上で、次のステップとして隣国や結びつきの強い第三国の「標準規格」に歩み寄ることができれば、それは大きな進歩と言えるのではないか。他の様々な分野と同様、ご近所では南アフリカが一歩先を行っており、彼らの[Protection of Personal Information Act (POPIA)](https://www.dataguidance.com/jurisdiction/south-africa)を参考にするのも悪く無い。

いずれにせよ、変化には時間がかかるものであり、その事実を受け入れて現地のコンテクストに沿った（そして寄り添った）動きをすることは必須である。これを無視して、たとえばGDPRの“専門家”を迎え入れて短期集中で改善を計ったとして、そのような「ショートカット」に意味があるとは僕は思えない。そんなわけで、日常業務で「もっとこうすればいいのに」と考えることは多々あれど、それを飲み込む頻度の多さたるや・・・もどかしいけれど、これが現実である。

![me-speaking](/images/data-protection-law-in-malawi-2023/me-speaking.jpg)
▲ 手を動かすよりも、現地のみなさんとの対話・議論の時間を重視する。「やること」よりも「やらないこと」を判断する回数の方がずっと多い。

いち開発者として、僕はマラウイでどのように立ち回るべきか？正直なところ、全くわからん。けれど、余所者が息巻いてプロジェクトを主導することが正解では無いというのはわかる。

[^1]: たとえば *[Globalization and environmental problems in developing countries](https://link.springer.com/article/10.1007/s11356-021-14105-z)* で議論されている様に、開発のフェーズによってその優先度は異なる。初期段階では経済成長を目指すが故に環境への配慮は置き去りになり、その後、国民の所得が向上するにつれて徐々に環境問題の認知度も向上していく。
