---
title: 二酸化炭素濃度センサーMH-Z14AとNanoPiでブラウザで見れる濃度計を作った(前編)
date: 2021-02-06 17:54:44
thumbnail: /images/mh-z14a-1/thumbnail.png
toc: true
tags:
  - 日記
  - mh-z14a
  - NanoPi
  - 二酸化炭素濃度
---

集中力を高めるためには換気も大切らしい・・・ということでブラウザで見れる二酸化炭素濃度計を作りました．

<!-- more -->

## きっかけ
### 換気推奨が推奨される今日この頃

最近換気をするようによく耳にします👂．換気をすることで感染症対策😷のみならず，作業効率のアップ⤴️にもつながるようです．実際，建築物環境衛生管理基準(環境衛生上，良好な状態を目標にしている基準らしい) では 1000 ppm以下になるよう決められています．[(Wikipedia)](https://ja.wikipedia.org/wiki/%E5%BB%BA%E7%AF%89%E7%89%A9%E7%92%B0%E5%A2%83%E8%A1%9B%E7%94%9F%E7%AE%A1%E7%90%86%E5%9F%BA%E6%BA%96)

そこで自室の二酸化炭素濃度が気になりました👀

### 既存の商品は高い

二酸化炭素濃度計を購入しようと Amazon 🛒でざっと検索したところまともそうな商品は 1 万円弱くらいで販売されていて，換気指標にするという目的に見合う金額ではありません😢

どうせならセンサーだけ買ってきた方がカスタマイズできるし良いのではないかと思いシステムを自作してみることにしました😄


## 用意したもの

### 二酸化炭素濃度センサー(MH-Z14A)

中華通販に興味があったのもあって Banggood で「NDIR 二酸化炭素」などと適当に検索して買いました💸

<div class="bcard-wrapper"><span class="bcard-header"><div class="bcard-site"><a href="https://jp.banggood.com/NDIR-CO2-Sensor-MH-Z14A-PWM-NDIR-Infrared-Carbon-Dioxide-Sensor-Module-Serial-Port-0-5000PPM-Controller-p-1248270.html" rel="nofollow" target="_blank">www.banggood.com</a></div><div class="bcard-url"><a href="https://jp.banggood.com/NDIR-CO2-Sensor-MH-Z14A-PWM-NDIR-Infrared-Carbon-Dioxide-Sensor-Module-Serial-Port-0-5000PPM-Controller-p-1248270.html" rel="nofollow" target="_blank">https://jp.banggood.com/NDIR-CO2-Sensor-MH-Z14A-PWM-NDIR-Infrared-Carbon-Dioxide-Sensor-Module-Serial-Port-0-5000PPM-Controller-p-1248270.html</a></div></span><span class="bcard-main"><div class="bcard-title"><a href="https://jp.banggood.com/NDIR-CO2-Sensor-MH-Z14A-PWM-NDIR-Infrared-Carbon-Dioxide-Sensor-Module-Serial-Port-0-5000PPM-Controller-p-1248270.html" rel="nofollow" target="_blank">NDIRCO2センサーMH-Z14APWMNDIR赤外線二酸化炭素センサーモジュールシリアルポート0-5000PPMコントローラー</a></div><div class="bcard-description">Only US$22.99, buy best ndir co2 sensor mh-z14a pwm ndir infrared carbon dioxide sensor module serial port 0-5000ppm controller sale online store at wholesale price.</div></span></div>

私は 2958 円で購入しましたが，この記事を書いているときに見たらセールで 2457 円で売ってました 😢

最初は 2 週間かかると書いてありましたが 5 日で届きました，初めての中華通販でしたが思ったより早くて驚きです💨

データシート📖はここです．仕様とか通信方法とか載っています．

[](https://www.winsen-sensor.com/d/files/MH-Z14A.pdf)


### NanoPi NEO2 

秋葉原の秋月電子で昔購入したものです．家に転がっていたので実質 0 円です(購入金額は3240円です．)

1から作るなら Raspberry Pi Zero とかが無線接続できるので便利そうです．

OS を入れるための micro SD も必要です．今回は Armbian をインストールしました．

[Nanopi Neo / Core](https://www.armbian.com/nanopi-neo/)

### 通信するための銅線 4本

いい感じの被覆銅線がなかったので適当に落ちてた通信ケーブルの被覆を引きちぎりました．実質 0 円です．

## サイズ感

左がMH-Z14A，右がNanoPi NEO2です．大きさは両者ともほぼほぼ同じで手の中に収まる大きさです🖐

![](/images/mh-z14a-1/1.png)

## センサーとNanoPiを接続する



### ケーブルで繋ぐ

赤枠のあたりを繋ぎます．
![](/images/mh-z14a-1/2.png)

Tx の対は Rx，Rx の対は Tx です．

T は Transmitter，R は Receiver の意味なようです．

5V を V+，GND を V- につないで完成しました✨

![](/images/mh-z14a-1/3.png)

### 通信を有効化する

UART，DAC，PWM の 3 つの方法で値を取得できるようです．今回は Serial port(UART) でやりました．

`$ sudo armbian-config`

System > Hardware > uart1 に ✔ して Save

これにより ttyS1 としてアクセスできるようになりました．

> It supports UART0/1/2/3. You can access it via "/dev/ttySX".
[NanoPi NEO2](http://wiki.friendlyarm.com/wiki/index.php/NanoPi_NEO2)

## 動作確認
### 値を取得する
Python で実装・公開されている方がいたのでお借りしました．デバイスのパスを修正して実行💻．


<div class="bcard-wrapper"><span class="bcard-header"><div class="bcard-site"><a href="https://github.com/chez-shanpu/co2-sensor-pi" rel="nofollow" target="_blank">GitHub</a></div><div class="bcard-url"><a href="https://github.com/chez-shanpu/co2-sensor-pi" rel="nofollow" target="_blank">https://github.com/chez-shanpu/co2-sensor-pi</a></div></span><span class="bcard-main"><div class="bcard-title"><a href="https://github.com/chez-shanpu/co2-sensor-pi" rel="nofollow" target="_blank">chez-shanpu/co2-sensor-pi</a></div><div class="bcard-description">MH-Z14Aモジュール. Contribute to chez-shanpu/co2-sensor-pi development by creating an account on GitHub.</div></span></div>
```python
$ python3 sensor.py
{"ppm": 1676, "dt": "2021-02-06T15:34:21.435596", "ts": 1612593261.435775}
```

取得できました．

### キャリブレーション

指定のコマンドを送信することでその時点での濃度を 400ppm として測定するようにしてくれます．

到着してすぐののときは外に放置しても 750ppm と考えられない数値が出てきたのでキャリブレーションは必要だと思います．

20分以上 400ppm 環境下に放置してコマンドを送信します．外気は410.5 ppm だそうので精度を求めない限り外気に晒すのが良いでしょう．[二酸化炭素濃度の経年変化](https://ds.data.jma.go.jp/ghg/kanshi/ghgp/co2_trend.html)

先程のリポジトリにも実装されているのでそれを実行しました．

自動キャリブレーション機能もありオフィス・家庭向けにいい感じにしてくれるようです．





## 後半

[後半](http://unyacat.net/2021/02/07/mh-z14a-2/)は WebUI 実装編です．

