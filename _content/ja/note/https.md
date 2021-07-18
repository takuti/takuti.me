---
aliases: [/note/https/]
categories: [プログラミング]
date: 2017-02-04
images: ['https://res.cloudinary.com/takuti/image/upload/l_text:Sawarabi%20Gothic_32_bold:%E3%82%B5%E3%82%A4%E3%83%88%E3%82%92HTTPS%E3%81%AB%E3%81%97%E3%81%9F,co_rgb:eee,w_800,c_fit/v1626628472/takuti_bgimyl.jpg']
keywords: [発行, 証明書, サイト, トップページ, はてブ, 従う, 唯一, 事項, 諦め, 懸念]
lang: ja
recommendations: [/ja/note/one-month-in-canada/, /ja/note/hello-jekyll/, /ja/note/why-spark/]
title: サイトをHTTPSにした
---

今はとてもいい時代なので **[Let's Encrypt](https://letsencrypt.org/)** が無料でSSL証明書を発行してくれる。というわけで、サイトのHTTPS化を行った。

### 証明書の発行と nginx.conf の変更

作業自体はとても簡単で、証明書の発行に関する処理はすべて **[certbot](https://certbot.eff.org/)** （旧名：letsencrypt）というツールがやってくれる。[トップページ](https://certbot.eff.org/)からサーバとOSを選択すれば、それに応じたinstallationが表示される。どこまで親切なんだ！

ここは **CentOS 6** 上の **Nginx** で動いているので、以下それに従う。

certbotの導入は、適当な場所にwgetして実行権限を与えるだけ。

```
$ wget https://dl.eff.org/certbot-auto
$ chmod a+x certbot-auto
```

あとはWebサーバのドキュメントルートとドメインを指定してcertbotを実行してあげればよい。

```
$ /path/to/certbot-auto certonly --webroot -w /var/www/example -d example.com
```

うちはNginxだけど、Apacheの頃の名残で `/var/www/html` をドキュメントルートにしている。`/etc/nginx/nginx.conf` は以下のような感じ。

```conf
server {
	listen 80;
	server_name  takuti.me;

	location / {
		root   /var/www/html;
		index  index.html index.htm index.php;
	}

	# 以下略
```

なので叩いたコマンドは以下。

```
$ /path/to/certbot-auto certonly --webroot -w /var/www/html -d takuti.me
```

途中でメールアドレスなどを聞かれ、無事完了すると Congratulations と言われる。証明書の類は `/etc/letsencrypt/live/takuti.me` 以下に作成され、ドキュメントルート直下には認証用プラグインのために `.well-known` というディレクトリが作成される。

あとは `/etc/nginx/nginx.conf` を、

- httpリクエストをすべてhttpsにリダイレクト
- SSLを有効にして証明書のパスを指定

について書き換えればよい。

```conf
server {
	listen 80;
	listen [::]:80;
	return 301 https://$host$request_uri;
}

server {
	listen 443 default ssl;
	server_name  takuti.me;

	ssl on;

	ssl_certificate /etc/letsencrypt/live/takuti.me/fullchain.pem;
	ssl_certificate_key /etc/letsencrypt/live/takuti.me/privkey.pem;
	ssl_protocols TLSv1 TLSv1.1 TLSv1.2;

	location / {
	   root   /var/www/html;
	   index  index.html index.htm index.php;
	}

	# 以下略
```

```
$ service nginx restart
```

簡単！

### HTTPSポート443番の開放

次に、 `/etc/sysconfig/iptables` に443番ポートを開ける記述を追加して、

```
-A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport 443 -j ACCEPT
```

iptablesをrestartする。

```
$ service iptables restart
```

これでサイトのHTTPS化は完了。

### 証明書の自動更新の設定

最後に、証明書の自動更新を設定する。証明書の更新は、

```
$ /path/to/certbot-auto renew
```

これだけでできるので、このコマンドをcronに登録してあげればよい。ここでは毎月1日午前3時に更新をかけるようにした。

```
00 03 01 * * /path/to/certbot-auto renew --quiet
```

これでよし。

### おまけ1: 静的サイトジェネレータ Hugo の baseUrl を https:// にする

このサイトのコンテンツはGo製の静的サイトジェネレータ **[Hugo](https://gohugo.io/)** で生成している。

Hugoはコンテンツ生成時に `--baseUrl` オプションを付与すると、HTML中のパスをURLに置換してくれる。たとえば、

```
$ hugo --baseUrl='http://takuti.me'
```

と叩いたならば、 `/style/style.css` といったパスによるアセットの指定は、URLによる指定 `http://takuti.me/style/style.css` に置換された上でサイトコンテンツが生成される。

HTTPS化以降はこの `--baseUrl` を **https://~** に書き換えなければならない点に注意。

### おまけ2: サイトコンテンツのデプロイ時に .well-known を消さないようにする

Hugoで生成したコンテンツは、

```
$ rsync （中略） --delete {ユーザ}@{ホスト}:{ドキュメントルート}
```

でサーバに転送しており、転送前にドキュメントルートの中身をすべて削除している。

しかし今、certbotによって作成された `.well-known` というディレクトリがドキュメントルート直下にある。これは削除したくない。

なので以後 `.well-known` をrsyncの対象から除外することを忘れずに。

```
$ rsync --exclude ".well-known" （中略） --delete {ユーザ}@{ホスト}:{ドキュメントルート}
```

そんなこんなでサイトのHTTPS化に成功した。

HTTPS化に対する唯一の懸念事項は **http://~** でのはてブ数が残らないことだったけど、これはもう諦めた。仕方あるまい。