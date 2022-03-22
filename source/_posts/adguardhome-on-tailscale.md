---
title: Adguard HomeをTailscale上に載せて任意デバイスで広告をブロックする
twitter_card: summary_large_image
tags:
  - AdguardHome
  - Tailscale
  - 広告ブロック
date: 2022-03-22 17:15:08
---

Adguard HomeをTailscale上に載せます．Tailscaleを利用することでモバイル回線等宅外の回線を利用していても適用することができます．Tailscaleが使えるならOSによらず無料であらゆるデバイスで設定ができようできて便利です．

<!-- more -->



## コンテナを立ち上げる

Exit node指定で立ち上げます．

docker-compose.yml
```yaml
version: "2.4"
services:
  tailscale:
    hostname: centos-hosted-myhome              # This will become the tailscale device name
    image: jonoh/tailscale
    volumes:
      - "./tailscale_var_lib:/var/lib"        # State data will be stored in this directory
      - "/dev/net/tun:/dev/net/tun"           # Required for tailscale to work
    cap_add:                                    # Required for tailscale to work
      - net_admin
      - sys_module
    command: --advertise-exit-node -- --verbose 1

  adguardhome:
    restart: unless-stopped
    volumes:
      - './adguard_data:/opt/adguardhome/work'
      - './adguard_config:/opt/adguardhome/conf'
    image: adguard/adguardhome
    network_mode: service:tailscale
```

`$ docker-compose up -d`

起動して数秒するとログに認証URLが吐き出されます．開いてログインします．

`$ docker-compose logs`

```yaml
tailscale-tailscale-1    |
tailscale-tailscale-1    | To authenticate, visit:
tailscale-tailscale-1    |
tailscale-tailscale-1    |      https://login.tailscale.com/a/XXXXXXXXXXXX
tailscale-tailscale-1    |
tailscale-tailscale-1    | 2022/03/22 08:24:37 control: RegisterReq: onode= node=[iFaLD] fup=true
```

割り当てられた IP アドレスをコピーして DNS タブの Nameservers に指定します．override local dnsを選択します．

![Tailscaleの設定からDNSを上書きをする](/images/adguardhome-on-tailscale/Untitled.png)

これにて設定完了です．

ブラウザで当該IPを開くとAdguard Homeの設定画面が出てくるので好みに合わせてブロック・許可ドメインを設定します．

## LINEの広告をブロックする

[先人のツイート](https://twitter.com/cyberflamingo/status/1494960795905830915)を参考にAdguard Homeのカスタム・フィルタリングルールに書き込みます．

```
// LINE Block
// https://twitter.com/cyberflamingo/status/1494960795905830915
||naver.jp^
||line-scdn.net^
||line-apps.com^
||line.me^
@@||d.line-scdn.net^
@@||gw.line.naver.jp^
@@||ln.cdn.akamaized.net^
@@||obs-jp.line-apps.com^
@@||profile.line-scdn.net^
@@||scdn.line-apps.com^
@@||torimochi.line-apps.com^
@@||w.line.me^
```

モバイル回線でもブロックできていることを確認できました．

![上部の広告枠がブロックされている](/images/adguardhome-on-tailscale/Untitled%201.png)

