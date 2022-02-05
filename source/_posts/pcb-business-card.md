---
title: プリント基板でNFCタグ名刺を作った
thumbnail: /images/pcb-bussiness-card/thumbnail.jpg
twitter_card: summary_large_image
tags:
  - 名刺
  - 基板
  - JLCPCB
toc: true
date: 2022-02-06 00:08:42
---

名刺風の基板を設計してみました．

基板にはイラストを載せ，NFCタグとしての機能を持たせることにしました．

そして基板製造サービスに依頼し製造してもらいました．

<!-- more -->



## 🧭 設計方針

- 基板にイラストを載せる
- NFCタグとして機能する
- 名刺としての役割を持たせる

基板設計ソフトにはEagleを使いました．

## 💳 基板のサイズ

交通系IC・クレカ風にしてみたいということで同じ形の 86mm x 54mm としました．また角は3mm丸く削りました．一般的な名刺サイズより少し小さめです．

<img src="/images/pcb-bussiness-card/Untitled.png" width="40%" style="display: block; margin: auto;">

Dimensionレイヤーでサイズを指定しました．

## 🎨 基板にイラストを描く

### 基板での表現手法

基板で多色表現をするには

- 導線・銅箔を配置する(Top, Bottom)
- シルクを載せる(tPlace, bPlace)
- レジストを載せない(tStop, bStop)

を組み合わせます．

例えば，シルクを載せたら白くなり，導線を配置してレジストを載せないようにしたら導線が露出してキラキラします．

プリント基板での表現が実際にどうなるかは以下のサイトで丁寧に解説されています．

<div class="bcard-wrapper"><span class="bcard-header withgfav"><div class="bcard-favicon" style="background-image: url(https://www.google.com/s2/favicons?domain=https://e3w2q.github.io/13/)"></div><div class="bcard-site"><a href="https://e3w2q.github.io/13/" rel="nofollow" target="_blank">e3w2q.github.io</a></div><div class="bcard-url"><a href="https://e3w2q.github.io/13/" rel="nofollow" target="_blank">https://e3w2q.github.io/13/</a></div></span><span class="bcard-main"><div class="bcard-title"><a href="https://e3w2q.github.io/13/" rel="nofollow" target="_blank">PCBでの多色表現の解説と2UキーマクロパッドMX2U!を作った話</a></div><div class="bcard-description"></div></span></div>

### イラスト・文字を事前処理する

各レイヤーに配置したい部分を白黒画像で出力します．

事前にお好みのペイントソフトで各レイヤーごとに分けておきます．出力時はEagleで読める2ビットBMPにしておきます．

対応してなければWindows標準のペイントソフトを使えば2ビットBMPに変換できます．

文字も同様に画像にして用意します．

今回，イラストは以前にことかす先生に依頼して描いてもらったものを使いました．

[三白眼女の子メーカーあ... by ことかす@料理研究家 | Skeb](https://skeb.jp/@NNPS_KM_SONYA/works/29)

<img src="/images/pcb-bussiness-card/Untitled%201.png" width="40%" style="display: block; margin: auto;">

### 基板に載せる

画像を基板データに変換していきます．

オレンジ色のULPボタンを押して「import-bmp」，作成したBMPを選択し，黒白にチェック．スケールを選びそのまま「OK」，スクリプト実行画面が出てきたら「Run Script」を押して変換を始めます．

![](/images/pcb-bussiness-card/sch.png)

<img src="/images/pcb-bussiness-card/Untitled%205.png" width="40%" style="display: block; margin: auto;">

「Selection Filter」で欲しいレイヤーのみを指定し全体を選択．「Inspector」タブで全体を選びLayerを欲しいレイヤーに変更します．

![](/images/pcb-bussiness-card/Untitled%206.png)

## 🌐 NFCコイルを搭載する

### 部品の選定

#### NFCチップ

マルツで調べて1個単位で買える物の中で一番安いやつにしました．

裏面実装でハンダ難度高いし，容量少ないけど安さは正義です．

[NFC FORUM TYPE 2 TAG IC WITH 1.6 ST25TN01K-AFH5 STマイクロエレクトロニクス製｜電子部品・半導体通販のマルツ](https://www.marutsu.co.jp/pc/i/41560978/)


[データシート](https://www.st.com/resource/en/datasheet/st25tn01k.pdf)

#### LED

コイルとして機能しているかどうかを見るためにチップLEDも適当に購入しました．

[薄型SMD1608チップLED(緑色、10個入) LTST-C190KGKT*10 Lite-on製｜電子部品・半導体通販のマルツ](https://www.marutsu.co.jp/pc/i/1633530/s1=%E7%B7%91%EF%BC%8F10%E5%80%8B/)

- データシート
    - $I = 20$mA時
    - $V_F = 2$V

#### チップ抵抗

LEDに流れる電流を調整するために必要な抵抗です．

入力電圧は[アンテナ設計推奨ルール](https://www.st.com/resource/ja/application_note/an5276-antenna-design-for-st25r3916-st25r3917-and-st25r3920-devices-stmicroelectronics.pdf)に基づいて2.8Vとします．

$$
R = \frac{V_{CC} - V_{LED}}{I_{LED}} = \frac{2.8 - 2}{20 \times 10 ^ {-3}} = 40 \Omega
$$

40Ωのチップ抵抗を買いました．

注文パーツと価格は以下の通りです．

![](/images/pcb-bussiness-card/Untitled%207.png)

### NFCコイルの設計

Suicaの左側の台形を意識したコイルを搭載しました．

<img src="/images/pcb-bussiness-card/Untitled%208.png" width="40%" style="display: block; margin: auto;">

まずNFCチップの内蔵容量から計算して，コイルの必要なインダクタンスを算出します．

$$
f = \frac{1}{2 \pi\sqrt{LC}}
$$

$$
L = \frac{1}{C (2 \pi f) ^ 2 }
$$

$$
L = \frac{1}{50 \times 10 ^ {-12} \times (2 \pi \times 15.56 \times 10^6)^2 } = 2.755 \mathrm{\mu H}
$$

雑なシミュレーションの結果(ページ最後参照)，台形で5回巻きを線と線の間は0.4mm開けて実装することでうまくいきそうであることがわかりました．

## ✨ 基板データ完成

コイルの中に銅箔は配置できないので右側にイラストを載せてコイルの内側にシルクで文字を載せました．

表面デザインで力尽きてしまったので裏面はQRを載せただけにしました．

![](/images/pcb-bussiness-card/board_data.png)


## 👨‍🏭 製造

製造は[JLCPCB](https://jlcpcb.com/)に依頼することにしました．

他のプリント基板製造サービスに比べてWebサイトのUIが良かったのと，送料は安いけど早いという口コミを見て選びました．

注文時にTwitterを見ると[7ドルオフクーポン](https://twitter.com/JLCPCB_Japan/status/1456555665648881664)が配布されており，お得に製造してもらえました．感謝🙏

製造過程のGIFも見れて楽しかったです．

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">基板をJLCPCBで発注したんだけど各製造過程で行なっていることの動画がついてきて見ててとても楽しい <a href="https://t.co/fDOP2Zen1Z">pic.twitter.com/fDOP2Zen1Z</a></p>&mdash; うにゃ🐈 (@unya_2) <a href="https://twitter.com/unya_2/status/1481809951039254528?ref_src=twsrc%5Etfw">January 14, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## ✨ 基板完成

中国から2週間弱で届きました．

![](/images/pcb-bussiness-card/Untitled%209.png)

メガネと髪留めは銅箔が露出しているため光を照らすとキラキラします．

![](/images/pcb-bussiness-card/Untitled%2010.png)

顔の部分にも銅箔を入れているため光にかざすと肌色に見えます．

![](/images/pcb-bussiness-card/Untitled%2011.png)

LEDと抵抗をつければ光ります．タグICをつければタグになります．LEDとICは両方つけても機能します．

![](/images/pcb-bussiness-card/Untitled%2012.png)

コイルもイラストも上手く出来てよかったです．完．

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">NFCタグ機能付きの名刺基板を作ってみました💳 <a href="https://t.co/QOId6AlyOS">pic.twitter.com/QOId6AlyOS</a></p>&mdash; うにゃ🐈 (@unya_2) <a href="https://twitter.com/unya_2/status/1489994499702996994?ref_src=twsrc%5Etfw">February 5, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<br />

<br />

<br />





## おまけ

### 雑なコイルシミュレーション

基板コイルのインダクタンスの計算式を探したところ，[ST公式のPDF](https://www.st.com/resource/en/application_note/an2866-how-to-design-a-1356-mhz-customized-antenna-for-st25-nfc--rfid-tags-stmicroelectronics.pdf)に載っていたものの，形状に応じた定数があると判明．

なんとなく長方形と同じだろうと思いつつも，練習を兼ねてFemtetでシミュレーションをしてみることに．とは言いつつも斜めのモデリングがめんどくさすぎたので1周で断念．

[ST公式計算サイト](https://eds.st.com/antenna/#/)の四角の計算結果215.42μHに対して，214.7μHだったので最後余計に隙間開けた分も考慮すればほぼ同じだろうし，角丸くしたりするので精度はそこそこでいいやと判断し，四角のコイルとして計算サイトを使うことにしました．

![](/images/pcb-bussiness-card/rect846.png)

![](/images/pcb-bussiness-card/Untitled%2013.png)

![](/images/pcb-bussiness-card/Untitled%2014.png)

![](/images/pcb-bussiness-card/Untitled%2015.png)

コイルとしての機能を持ちつつも，Suica風の形を保てそうなパラメータを探し，最も近しそうな以下の値で作ることにしました．

![](/images/pcb-bussiness-card/Untitled%2016.png)

### ソルダレジストの色

同じデータで同タイミングで注文したのですが，レジスト部が緑と黒で製造結果が異なってしまいました．

シルクを1milごとにボーダー柄することで半分の白色になるのではないかと考え製造を依頼したものの，緑は全面白指定と変わりなく，黒では疎に線が入ってしまいました．

基板製造メーカによるかもしれませんが色の濃淡を調節するのは難しそうです．

<img src="/images/pcb-bussiness-card/Untitled%2017.png" width="40%" style="display: block; margin: auto;">



### NFCチップの選び方

基板に実装する際にサイズが小さすぎてコテで出来るが大変むずかしいです．

それとアドレス帳データが入る容量くらいはあったほうが名刺としては良かったかもです．
