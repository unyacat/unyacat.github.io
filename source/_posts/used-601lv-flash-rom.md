---
title: 中古で買った601LVを文鎮にして蘇生させた
thumbnail: ./images/used-601lv-flash-rom/IMG_20211108_203626.jpg
twitter_card: summary_large_image
tags:
  - null
date: 2021-11-08 16:48:41
---

名古屋 大須の「ワールドモバイル 大須アメ横店」でLenovo Tab3(601LV) を買ってきました．

[](https://www.softbank.jp/partners/kyoiku-press/products/list/lenovo-tab3/spec/)

ジャンクコーナのカゴにどっさりタブレットとかスマホが並んでいる中からこれならまだ使えそうと選んだ一品．

価格は1,650円．外観はSD・SIMトレイカバーがないことや黄ばみが目立つ感じ．

それよりも問題なのは画面ロックが掛けられたままの状態ということ．まぁ適当に検索すればなんとかなると甘く考え購入．しかし・・・

<!-- more -->

## 👨‍🔧工場出荷状態へリセットを試みるもできず

一度電源を落として電源ボタン・音量ボタンをタイミング良く押すとドロイド君が拝めたりリカバリー画面に突入できます．

中のデータには興味がないので全リセットの勢いで向かってきます．

[隠しコマンド、見つけちゃいました！ | 札幌でiPhone修理・故障は安心の道内企業アイフォンクリア 信用・信頼・高技術の『期待に応える誠実なiPhone修理店』](https://www.iphoneclear.jp/blog/rafirahonten/androidkaitori/)

なんとか突入できたもののFactory Reset に類する項目は見つかりませんでした．

![Untitled](/images/used-601lv-flash-rom/Untitled.png)

![Untitled](/images/used-601lv-flash-rom/Untitled%201.png)

## 🙀海外ROMを焼きを試すも失敗

601LVの前機種，501LVで海外版のROMを焼いている人がいました．

501LVはソフトバンク向けにカスタムされたものですが，海外で中身が同じ「Lenovo Tab 2 A8-50」という機種が発売されているされているようです．

[【501LV】文鎮化したのでROMを焼き直した話](https://old.haruroid.com/haruroid.0t0.jp/blog/archives/934.html)

601LVで同じことができないかと，中身で似た機種を探すと「TB3-850M」が出てきました．

早速 ROM 探して書き込みを試みます．

[Lenovo Tab 3 8 TB3-850M Stock Firmware ROM (Flash File)](https://firmwarefile.com/lenovo-tab-3-8-tb3-850m)

しかし，エラーを吐いてしまいます．

よくみると搭載チップがTB3-850MのほうはMT6735に対して601LVのほうはMT8735が搭載されています．チップが違うので書き込めないとエラーを出されてしまいました．

しかもここで文鎮化してしまいます．絶望．

![Untitled](/images/used-601lv-flash-rom/Untitled%202.png)

他に601LVは501LVの上位互換という情報からLenovo Tab 2 A8-50のROMを焼いてみたりしましたが動かずでした．

## 🔥601LVのROMを購入して焼いた

買ってから絶望し，半年以上が経ちました．

なんとなく2chを探すとソフトバンク版のROMが海外サイトで買えるされているという情報がありました．

![Untitled](/images/used-601lv-flash-rom/Untitled%203.png)

[【全機種】Lenovoタブレット総合【全キャリア】](https://egg.5ch.net/test/read.cgi/android/1521950867/112)

ここまでやってきてもう消費したくなかったのでリンク先からROMを購入することにしました．

[601LV_S_USR_S100021_1707031034_MPM0._JPSECURE.zip | GEM-FLASH Firmware](http://firmware.gem-flash.com/index.php?a=browse&b=file-info&id=32302)

3GB2.99ドルのプランを購入．買った時は日本円で340円でした．

支払画面は選択肢が多くややこしうえにPaypalは見当たらなかったのですが，とりあえずカード番号が入りそうなPaymentwallを選び決済しました．Revolutの使い捨てカード番号はこういうときに気軽に利用できるので便利ですね．

![Untitled](/images/used-601lv-flash-rom/Untitled%204.png)

## ✨起動

SPFlashToolを使い，書き込みを行うと無事起動することができました．

ようそこの画面は安心します．

![Untitled](/images/used-601lv-flash-rom/Untitled%205.png)

Wi-Fiの選択画面でエラーらしきものが表示されていますがこのあとはなんら問題なく動作しました．

2.4GHz帯は掴むのですが5GHz帯は掴んでくれません．

![Untitled](/images/used-601lv-flash-rom/Untitled%206.png)

## 601LVの動作

文章を読むのには十分に使えそうですし，機嫌がいい時はテレビ番組も視聴にも使えます．

でもストレージが16GBしかなくアプリのインストール・更新をしているときにストレージが足りませんと怒られてしまいました．実際に使えるのは10.3GBだけのようです．

8インチで1280×800ドットなので画面がモヤっとしますし，YouTubeで2倍速再生したら紙芝居のようになることも．Wi-Fiの速度もあんまりでていないようです．

とはいえ4年以上前の端末に求めることではないのかもしれません．

2021年5月時点で新品で1万弱のものを実質2000円で手に入れられたのでとても満足です．

[Androidタブレット「Lenovo TAB3」が9,980円！LTE対応の未使用品が大量入荷 - AKIBA PC Hotline!](https://akiba-pc.watch.impress.co.jp/docs/news/news/1324690.html)

