---
title: Docker を利用して快適な Firefox Send のサーバーを自宅で建てる
date: 2020-10-05 22:08:17
tag: 
---

Firefox Send をネタに Web サーバーを自宅で建てます．自宅内外問わず円滑に使えるように設定をすることを目標にします．

<!--more-->

## Firefox Send とは

![設定完了](/images/firefox-send-host-on-local/Firefox_Send_logo.png)

ファイルを簡単に相手に送付できるWebサービスです．

特徴として n 日経ったら / n 回ダウンロードされたらリンク無効化できる機能に加え，アップロードされたファイルは暗号化されて安全に保管されるというものがあります．

後者の特徴故よからぬ使い方をする者も多かったようで Firefox によるホスティングは 2020 年 9 月で終了してしまいました．

## 目的

Firefox Send を家のネットワーク内にあるサーバー機でホスティングします．

また，家の内外でも支障なく利用できることを目指します．

## 環境

* サーバー機: CentOS 8
  * docker-compose version 1.27.4, build 40524192
  * ローカルIP を 192.168.1.111 に固定
* DNS: Cloudflare
  * send.example.com に立てたいとします．
* ルーター: PR-500MI

物理サーバーを「サーバー機」，ソフトウェアのサーバーを単に「サーバー」とします．

## 実行
### とりあえず Firefox Send サーバーを起動してみる

ソースコードは Archived になっているものの [GitHub](https://github.com/mozilla/send) から入手することができ，Docker 化もされているのですぐに起動することができます．[推奨されていません](https://github.com/mozilla/send/blob/ccbcb69666351a1c0fa40374649908f5bf5d89f8/docs/docker.md#user-content-setup:~:text=We%20don't%20recommend%20using%20docker%2Dcompose%20for%20production.)が docker-compose で組んでいきます．といいつつも[参考記事](https://qiita.com/moritalous/items/4de26a290787ae732fd0#docker-composeyml%E3%81%AE%E4%BF%AE%E6%AD%A3)の丸パクリです．

```yaml firefox-send/docker-compose.yml
version: "3"
services:
  web:
    build: .
    links:
      - redis
    ports:
      - "1443:1443"
    environment:
      - REDIS_HOST=redis
      - FXA_REQUIRED=false
  redis:
    image: redis:alpine
```

`192.168.1.111:1443` にアクセスして正常に動作していることを確認します．





### DDNS の設定
Cloudflare の DNS タブからサブドメインを登録します．固定 IP でない場合ダイナミック DNS を利用します．

#### DDNS 未設定の場合

アドレス更新には [oznu/cloudflare-ddns](https://hub.docker.com/r/oznu/cloudflare-ddns/) を利用しています．ひとまず A レコードで Name: send，Content: 適当な IP アドレス(ex. 1.1.1.1)を登録しておきます．

```yaml cloudflare-ddns/docker-compose.yml
version: '2'
services:
  cloudflare-ddns:
    image: oznu/cloudflare-ddns:latest
    restart: always
    environment:
      - API_KEY=XXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
      - ZONE=example.com
      - SUBDOMAIN=send
```

`docker-compose up -d` をして，Cloudflare の画面上で IP が変わっていれば良い感じです．

#### DDNS 設定済みの場合

既存で DDNS が設定されているドメインがあれば CNAME で登録しても動きます．

![設定完了](/images/firefox-send-host-on-local/image-20201005174958020.png)





これにより対象ドメインにアクセスがあれば家につながるようになりました．







### ポート開放

ルータにアクセスし(192.168.1.1) 詳細設定 > 静的IPマスカレード から 80 番(HTTP)と 443 番(HTTPS) にアクセスしたものをサーバー機に流すように設定します．

![](/images/firefox-send-host-on-local/image-20201005214232822.png)

### リバースプロキシと SSL(Let's Encrypt)

1 つのサーバーだけ建てるのならばそのまま通信受ければ良いですが，ほかにもサーバーを起動したくなった場合は通信を振り分けられず困ってしまいます．

同じサーバー機の上で複数サーバーを起動してても， send.example.com はこのサーバーで受ける，hoge.example.com はこのサーバーで受ける...... といったことができるようにリバースプロキシを設定します．[nginx-proxy](https://github.com/nginx-proxy/nginx-proxy) を使います．

ついでなので Let's Encrypt を利用して SSL 化しておきます．

```yaml nginx-proxy/docker-compose.yml
version: '3.7'

services:
  nginx-proxy:
    image: jwilder/nginx-proxy
    container_name: nginx-proxy
    ports:
      - 80:80
      - 443:443
    volumes:
      - html:/usr/share/nginx/html
      - dhparam:/etc/nginx/dhparam
      - vhost:/etc/nginx/vhost.d
      - certs:/etc/nginx/certs:ro
      - /var/run/docker.sock:/tmp/docker.sock:ro
    labels:
      - com.github.jrcs.letsencrypt_nginx_proxy_companion.nginx_proxy
    networks:
      - public

  letsencrypt:
    image: jrcs/letsencrypt-nginx-proxy-companion
    container_name: nginx-proxy-lets-encrypt
    depends_on:
      - nginx-proxy
    volumes:
      - certs:/etc/nginx/certs:rw
      - vhost:/etc/nginx/vhost.d
      - html:/usr/share/nginx/html
      - /var/run/docker.sock:/var/run/docker.sock:ro
    networks:
      - public

volumes:
  certs:
  html:
  vhost:
  dhparam:


networks:
  public:
    external: true
```

Firefox Send 側の docker-compose.yml も編集します．

```yaml firefox-send/docker-compose.yml
version: "3"
services:
  web:
    build: .
    links:
      - redis
    ports:
      - "1443:1443"
    environment:
      - FXA_REQUIRED=false
      - REDIS_HOST=redis
      - BASE_URL=send.example.com
      - VIRTUAL_HOST=send.example.com
      - LETSENCRYPT_HOST=send.example.com
      - LETSENCRYPT_EMAIL=admin@example.com
  redis:
    image: redis:alpine

networks:
  default:
    external:
      name: public
```

`docker network create --driver=bridge public` して，   `docker-compose up -d`  します．

ここまでで外からアクセスすれば正しく表示されるはずです．(されない場合は SSL まわりがうまくいってないかもしれません．Cloudflare の SSL/TLS 設定を変えると解決するかもしれません．)

しかしながらこのままだと家の中からアクセスした場合は無理です．



### DNS サーバーを家の中向けに起動する．

家の中のクライアントは Windows だけ・・・となれば hosts ファイルを直接いじることで家の中でも支障なく利用できます．

しかしながらスマートフォンなど hosts ファイルを通常操作できないものもあります．ここで DNS サーバーを起動して解決します．

[andyshinn/dnsmasq](https://hub.docker.com/r/andyshinn/dnsmasq/) を利用します．

```yaml dns/docker-compose.yml
version: '2'
services:
  dnsmasq:
    restart: always
    image: andyshinn/dnsmasq
    container_name: dnsmasq
    ports:
      - "53:53/udp"
      - "53:53/tcp"
    extra_hosts:
      - "send.unyacat.net:192.168.1.111"
    cap_add:
      - NET_ADMIN
```

`docker-compose up -d` します．

次に DNS サーバーの存在を家中に知らしめる必要があります．`$ip a` コマンドを打ち，物理ネットワークデバイスの inet6 の横

`inet6 xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/64 scope global dynamic noprefixroute` のアドレスを控えておきます．

ルータにアクセスし，詳細設定 > DNS 設定 から，自ドメインに対しては起動した DNS サーバーを利用するように設定します．

![](/images/firefox-send-host-on-local/image-20201005222418279.png)



### 完成

家の中でも外からでも同じアドレスにアクセスしても使えるはずです．

これを何に使うかは分かりませんが・・・．



## おまけ

試しに画像を 1 枚アップロードしてみました．

### ファイルの暗号化はされているのか

```
unyacat@rabbithouse /m/2/firefox-send> file IMG_6231.JPG  # アップロード前
IMG_6231.JPG: JPEG image data, Exif standard: [(略)], baseline, precision 8, 3626x5439, frames 3

unyacat@rabbithouse /m/2/firefox-send> file 1-17eeb501acab3f88 -i  # アップロード後
1-17eeb501acab3f88: application/octet-stream; charset=binary
```

### ファイルサイズに変化はあるか

```
unyacat@rabbithouse /m/2/firefox-send> wc -c IMG_6231.JPG | awk '{print $1}'  # アップロード前
12636056
unyacat@rabbithouse /m/2/firefox-send> wc -c 1-17eeb501acab3f88 | awk '{print $1}'  # アップロード後
12639358
```

中身は分からないですね．サイズは少し増大しました．



## 参考

[Firefox Send に何が起きたのですか？](https://support.mozilla.org/ja/kb/what-happened-firefox-send)

[さようならFirefox Send。あなたは私のT4gインスタンスの中で永遠に生き続けます!!](https://qiita.com/moritalous/items/4de26a290787ae732fd0#docker-composeyml%E3%81%AE%E4%BF%AE%E6%AD%A3)

[CA marked some of the authorizations as invalid](https://github.com/nginx-proxy/docker-letsencrypt-nginx-proxy-companion/issues/464#issuecomment-434234506)

[[Windows] Hostsファイルの追記方法、確認方法](https://faq.mypage.otsuka-shokai.co.jp/app/answers/detail/a_id/126047/~/%5Bwindows%5D-hosts%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AE%E8%BF%BD%E8%A8%98%E6%96%B9%E6%B3%95%E3%80%81%E7%A2%BA%E8%AA%8D%E6%96%B9%E6%B3%95)