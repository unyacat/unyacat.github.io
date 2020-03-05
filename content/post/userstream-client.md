+++
banner = "https://lh5.googleusercontent.com/YTA2cIAjg42nhqfg1mxpI--dhxWWDY13oOwJjqzEi501oZVgNqf9Aqh9C8M=w2400"
categories = ["Twitter"]
date = "2018-08-27"
description = "UserStream廃止と各サードパーティークライアントの対応まとめ"
images = []
menu = ""
title = "UserStream廃止と各サードパーティークライアントの対応まとめ"
+++

精度は保証しません。世の中にある全てのそれを載せているわけではありません。

<!--more-->


## Windows
### [Janetter for Windows](http://janetter.net/jp/)
[Janetter for Windows v4.5.0.1 公開](http://blog-jp.janetter.net/post/177049462397/janetter-for-windows-v4501-%E5%85%AC%E9%96%8B)

> 今回の更新ではUser Streams API終了に伴う対応をしました。リアルタイムでタイムラインを更新できなくなりました。また通知がリアルタイムで届かなくなります。アカウントの新規登録ができないため、新規ユーザーはご利用いただけません。

### [Tween](https://sites.google.com/site/tweentwitterclient/)
機能削除  
[Ver1.7.2.0リリース](https://sites.google.com/site/tweentwitterclient/project-updates/ver1720ririsu)

> TwitterのUserStreamsが段階的停止を経て廃止されるため、Tweenから接続機能を削除しました。

### [Krile](http://krile.troidworks.com/)
既に開発終了を宣言しているが将来的に公開も中止することを予告

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">Krileの開発についてはすでに終了を宣言していますが、8/16以降どこかのタイミングでバイナリの公開も終了させて頂きます。<br>Krile 0.41 のリリースからおよそ9年、長らくアップデートを続けて来られたのは、Krileをご利用頂いた皆様のおかげです。<br>本当にありがとうございました。</p>&mdash; くるるたん (@kriletan) <a href="https://twitter.com/kriletan/status/1028986589815300096?ref_src=twsrc%5Etfw">2018年8月13日</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


### [ツイタマ](http://twitter.softama.com/)
将来的公開中止を予告  
[UserStream APIの廃止と影響について](http://www.softama.com/blog/archives/1079)

> こちらは既に開発が終了しています。UserStreamへの依存が大きいことから、8/16前の適切なタイミングでアプリの公開を終了いたします。

## Mac
### [Tweetbot 3 for Twitter](https://itunes.apple.com/jp/app/tweetbot-3-for-twitter/id1384080005?mt=12&ign-mpt=uo%3D4)
機能削除  
v3.1  
1-2分おきの自動更新対応

> - Timeline streaming is now disabled. Your timelines will now refresh automatically every 1-2 minutes instead.

通知の削除 / 遅れを宣言

>- Notifications for Mentions, Direct Messages, Follows and Follower's Tweets will now be delayed by a few minutes.
- Notifications for Likes and Retweets have been disabled. 

### [Twitterrific 5 for Twitter](https://itunes.apple.com/us/app/twitterrific-5-for-twitter/id1289378661)
機能削除  
v5.3.4
毎分の自動更新対応

> Live streaming has been removed. Workaround: Twitterrific will now automatically refresh every few minutes while the app is open, or you can manually pull to refresh. 

## Linux
### [mikutter](https://mikutter.hachune.net/)
TweetDeckからいろいろするPluginを作っている人がいる  
[mikuttdeck](https://github.com/takemar/mikuttdeck)

## Android
### [SobaCha](https://play.google.com/store/apps/details?id=net.wakamesoba98.sobacha) / [MateCha](https://play.google.com/store/apps/details?id=net.wakamesoba98.matecha)
SobaCha v2.11.1 (WakameSoba)  
MateCha v3.2.1 (WakameSoba)

> UserStream API の対応を終了  

しかしSobaChaはTweetDeckにSobaChaの投稿UIをそのまま持ち込む事ができます

> TweetDeck オーバーレイモードを追加
<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">SobaChaをMastodonに対応することはUserStream廃止への本質的な対策ではないのでChromeで開いたリアルタイムに流れるTweetDeckの上にSobaChaのバーを表示するなんて言うメチャクチャなことをやってるんだ <a href="https://t.co/R55XpBLB9h">pic.twitter.com/R55XpBLB9h</a></p>&mdash; わかめそば@日曜日東ト03a (@wakamesoba98) <a href="https://twitter.com/wakamesoba98/status/1026862149954502656?ref_src=twsrc%5Etfw">2018年8月7日</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

### [Yukari](https://play.google.com/store/apps/details?id=shibafu.yukari)
機能削除  
v2.0.10.413 (planche 180824)  

> * UserStream接続機能の廃止

1分間隔での自動更新対応済み  
v2.0.8の更新内容

> * Home/Mentionsを1分前後の間隔で自動取得する機能の追加

### [Twitterのついっとぺーん (TwitPane)](https://play.google.com/store/apps/details?id=com.twitpane)  
機能削除  
v10.0.0

> UserStream 機能を廃止

### [Tweecha](https://play.google.com/store/apps/details?id=net.sinproject.android.tweecha) / [Tweecha Lite](https://play.google.com/store/apps/details?id=net.sinproject.android.tweecha.lite) / [Tweecha Prime](https://play.google.com/store/apps/details?id=net.sinproject.android.tweecha.prime)  
更新なし(説明文にはUserStream廃止に関する記述あり)  
Tweecha v67.1.2  
Tweecha Lite  v76.2.51  
Tweecha Prime v76.2.51  

### [twitcle plus](https://play.google.com/store/apps/details?id=jp.yoshika.twitcle.plus)
機能削除
v1.4.2

> UserStream API廃止のためUserStream機能を削除

### [びよーんったー](https://play.google.com/store/apps/details?id=jp.gifu.abs104a.twitterproject) / [びよーんったーPro](https://play.google.com/store/apps/details?id=com.ABS104a.biyontterpro)
ひよーんったー v4.2.4 ([?](https://twitter.com/alice_pidrkey/status/1029678207874654208))  
びよーんったー Pro v端末により異なります  
廃止

[https://twitter.com/ABS104a/status/1028525179968712704:embed]


### [Absolutter](https://play.google.com/store/apps/details?id=com.ABS104a.secondedition) / [Absolutter Lite](https://play.google.com/store/apps/details?id=jp.gifu.abs104a.biyonbeta2)
Absolutter v1.3.0 (?)  
Absolutter Lite v端末により異なります  
廃止(びよーんったーのツイート参照)

### [ツイタマ](https://play.google.com/store/apps/details?id=com.softama.twitama) / [ツイタマ+](https://play.google.com/store/apps/details?id=com.softama.twitamaplus)
ツイタマv2.1.0 / ツイタマ+v2.1.0

> TwitterのAPIの変更に対応しました

ツイタマにはそもそもUserStream APIに対応してないので影響なし  
ツイタマ+は検索のストリーミングを別のAPIに対応  
将来的廃止を予告(公式ブログ記事 [ツイタマ for Android v2.1のお知らせ](http://www.softama.com/blog/archives/1102))
UserStreamに関する公式ブログ記事あり [UserStream APIの廃止と影響について](http://www.softama.com/blog/archives/1079)

### [Talon for Twitter](https://play.google.com/store/apps/details?id=com.klinker.android.twitter_l)
機能削除  
v7.4.1

> Talon Pull has been removed from the app, Twitter is no longer supporting the service that this feature used.

### [Tweetings for Twitter](https://play.google.com/store/apps/details?id=com.dwdesign.tweetings)
機能削除  
v11.14.1.3

> - Removal of streaming feature as Twitter is imminently retiring this service

### [Fenix 2](https://play.google.com/store/apps/details?id=it.mvilla.android.fenix2)
機能削除  
v2.8

> Fenix will no longer be able to stream tweets, interactions and messages in real time.

### [Justaway](https://justaway.info/)
公開終了


<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">🙋 !!! 公開終了 !!!<br>・ストアでの公開を終了しました。<br>end.</p>&mdash; Justaway (@justawayfactory) <a href="https://twitter.com/justawayfactory/status/1029287452094001152?ref_src=twsrc%5Etfw">2018年8月14日</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


### [ツイッターするやつ](https://twitter.suruyatu.com/)
公開終了 
<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">ツイやつシリーズ終焉のお知らせ<br>google+に投稿しました！<a href="https://t.co/liHVIdCxVK">https://t.co/liHVIdCxVK</a></p>&mdash; ツイッターするやつ (@suruyatu) <a href="https://twitter.com/suruyatu/status/1029246003487039493?ref_src=twsrc%5Etfw">2018年8月14日</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
[Google+](https://plus.google.com/u/0/112977123297043486073/posts/csucu2dmP1i)
> ツイやつシリーズは、日本時間の2018年8月17日をもってサービスを終了します。
サービス終了の要因に関しては、ご存知可と思いますが、
TwitterのAPIの仕様変更により、アプリの維持が困難と判断したためです。
ツイやつで主に使われている、UserStreamが8月17日をもって終了します。
よって、ツイやつに関する全てのサポートを終了し、「ツイッターするやつ」シリーズの幕引きとします。
終了は残念ですが、今までご利用いただき大変感謝しています。
皆様、ありがとうございました！


### [Twidare](https://play.google.com/store/apps/details?id=org.mariotaku.twidere)
時間がないとの発言あり


<blockquote class="twitter-tweet" data-lang="ja"><p lang="en" dir="ltr">It&#39;s been a long time since last update. There&#39;re too much work to do in the past year so I really don&#39;t have time for Twidere. Now situation becomes better, and I&#39;ll continue develop Twidere.</p>&mdash; Twidere Project (@TwidereProject) <a href="https://twitter.com/TwidereProject/status/1024577817336532992?ref_src=twsrc%5Etfw">2018年8月1日</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

v3.7.3(更新日: 2017年11月15日)

### [beeter for Twitter](https://play.google.com/store/apps/details?id=me.b0ne.android.apps.beeter)
情報更新なし  
v0.87.3(更新日: 2017年4月20日)
http://apps-of-a-feather.com/

### [Janetter for Twitter](https://play.google.com/store/apps/details?id=net.janesoft.janetter.android.free) / [Janetter Pro for Twitter](https://play.google.com/store/apps/details?id=net.janesoft.janetter.android.pro) 
情報更新なし

## iOS
### [Tweetbot 4 for Twitter](https://itunes.apple.com/jp/app/tweetbot-4-for-twitter/id1018355599)
機能削除  
v4.9  
1-2分おきの自動更新対応

> - Timeline streaming on WiFi is now disabled. Your timelines will now refresh automatically every 1-2 minutes instead.

同時に独自通知の削除 / 遅れも宣言

> - Push notifications for Mentions and Direct Messages will now be delayed by a few minutes.
- Push notifications for Likes, Retweets, Follows and Quotes have been disabled. We'll be investigating bring some of these back in the future.

### [TheWorld for Twitter](https://itunes.apple.com/jp/app/theworld-for-twitter/id548994749)
更新なし  
v3.7(更新日: 2018年1月9日)
1分毎の自動更新実装予定の発言あり
https://twitter.com/TheWorld_JP/status/1029031198079631360


### [feather for Twitter](https://itunes.apple.com/jp/app/feather-for-twitter/id793157344) / [feather lite for Twitter](https://itunes.apple.com/jp/app/feather-lite-for-twitter/id1218696976)
v3.11.1  

> 今回のアップデートでは Twitter が 8/16 に User Stream API を削除するのに伴い関連する機能を削除しました。

### [Hel2um for Twitter](https://itunes.apple.com/jp/app/hel2um-for-twitter/id1146280429)
v0.5.3

>TwitterのAPI変更（UserStream廃止）の対応

### [Janetter for Twitter](https://itunes.apple.com/jp/app/janetter-for-twitter/id555594731) / [Janetter Pro for Twitter](https://itunes.apple.com/jp/app/janetter-pro-for-twitter/id555600657)
v1.8.6(更新日: 2018年8月14日)  
Streamingに関する記述なし

### [Echofon for Twitter](https://itunes.apple.com/jp/app/echofon-for-twitter/id286756410)
v11.4(更新日: 2018年8月1日)  
Streamingに関する記述なし  
機能削除


<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">Hel2um v0.5.3をリリースしました<br>8/16のUserStream廃止の対応で色々機能が無くなってます</p>&mdash; Hel2umApp (@Hel2umApp) <a href="https://twitter.com/Hel2umApp/status/1029536455649980416?ref_src=twsrc%5Etfw">2018年8月15日</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>




## あとがき
海外大手サードパーティークライアントが[問題提起するページ](http://apps-of-a-feather.com/)を作成しTwitterに訴えた。  
国内サードパーティークライアント開発者は[レズと青い鳥](https://mikutter-book.booth.pm/items/965207)という本を書きC94で頒布しTwitterへの愛を語った。  
[UserStreamの代替実装](https://github.com/SlashNephy/Tweetstorm)をする者も現れた。  
UserStreamで息をする(していた)ツイ廃はどこへ向かうのだろう。

## あとがきのあとがき
このメモはUserStream代替実装へ対応(=UserStream機能がいつまで残っていたかのメモ)に向けたものだった、けれど書いてるうちに長くいろいろ使ってきたサードパーティクライアントへの弔いの気持ちになってしまった。  
レズと青い鳥は実際ビッグサイトに行って手に入れてUS廃止前に読ませていただいた。(一緒にいたツイ廃と中身をちら見して会場で大騒ぎした)(すごくよかった)  
使ったことないクライアントも多くあるので記事自体かなり適当だし、まず実行できる環境持ってない物もあるので参考程度に。