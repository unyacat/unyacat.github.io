---
date: 2017-12-04
title: にゃーん ~カンバセーショナルカードを使った定型ツイートの容易化~
---

この記事は、[Lava Bucket Advent Calendar](https://adventar.org/calendars/2598) 4日目の記事です。

### やりたいこと

* 早く楽に簡単に「にゃーん」を呟きたい
* 定型文をいち早くツイートしたい (あらかじめ決まっている文章をいちいちツイート画面に打つのは面倒！)

<!--more-->

### まず初めに
Twitterにおける「にゃーん」を知らない人は[こちら](http://sh4869.hatenablog.com/entry/2016/12/02/225248)を読んでほしい。

### きっかけ
「にゃーん」な気持ちな時は「にゃーん」と打つことさえも億劫なのである。  

それはそうと、Twitterを見ていると画像、動画、アプリ等様々なコンテンツがついた広告が流れてくる。  

言語内容とも多様な広告が流れてくるわけだが、そこに1タップするだけで広告主が設定した文章が瞬時にツイート画面に埋められ簡単にツイートできるといった大変便利な機能を持った広告がある。

これを利用したら簡単に「にゃーん」できるのではないだろうか…？

### 目標
この機能を持ったツイートに手軽にアクセスできるようになれば、簡単に「にゃーん」をツイートできそうなのでそれを目指す。  

TwitterではこのようなWebサイトに対してより多くの情報を持たせることのできるこの機能は「カード」と呼ばれている。  

### 「カード」って何？
Webサイトのリンクをツイートした時にツイート文の下にそのサイトに関する情報をより多く載せることができる機能。  

一般的なWebサイトに採用されているカードは4種類あり、[Summaryカード](https://dev.twitter.com/web/sign-inhttps://dev.twitter.com/cards/types/summary.html)、[大きな画像付きのSummaryカード](https://dev.twitter.com/web/sign-inhttps://dev.twitter.com/cards/types/summary-large-image.html)、[Appカード](https://dev.twitter.com/web/sign-inhttps://dev.twitter.com/cards/types/app.html)、[Playerカード](https://dev.twitter.com/web/sign-inhttps://dev.twitter.com/cards/types/player.html)がある。  
今回紹介するカードは広告向けのカードであるため、一般的に利用されているものとは異なる。

### 広告向けの「カード」ってどんなものがあるの？
種類が多くここでは全てを語ることはできないので、Twitter社の説明ページを読んでほしい。


[business.twitter.com](https://business.twitter.com/ja/help/campaign-setup/advertiser-card-specifications.html:embed:cite)


見たことある広告形式が並んでいることだろう。  
今回気になった広告は「カンバセーショナルカード」というものらしい。

![](https://lh3.googleusercontent.com/rDyEYqYeJnMYI33hht1ZkyTEvaNxd1n-sy7Ay84emNH3hF4FSL7w1HlNaHU=w2400)
引用元: [お問い合わせ内容の検索](https://business.twitter.com/ja/help/campaign-setup/advertiser-card-specifications.html)


<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle"
     style="display:block; text-align:center;"
     data-ad-layout="in-article"
     data-ad-format="fluid"
     data-ad-client="ca-pub-2565580640435634"
     data-ad-slot="9725407123"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>


### 実装しよう
##### 用意するもの
* Twitterアカウント
* (ボタンの上に載せるための) 画像 / 動画のどちらか
* クレジットカード  
クレジットカードだが、プリペイドのカードでもできる可能性がある。今回はLINE PAYカードを使用した。ただし後述の通り、100円以上の残高が必要と思われる。1円も使わないのでご安心を。

##### 「カード」を設定する
まず、 [https://ads.twitter.com/](https://ads.twitter.com/) にアクセス。
![](https://lh5.googleusercontent.com/v5yK3sg_tbGnZ9GyMJxW6zEfSD7pmZjdUl4DI_GfbshqfeVz8QOblojVURk=w2400)

「次に進む」をクリック。  

![](https://lh6.googleusercontent.com/0DOQL2N7u4XvpKUn5SXGPSpKoJbivGPL9kM8JevcEbvtcWFN6x8dqhbUrpk=w2400)
右上の右から2つ目のドロップダウンをクリックし、「クレジットカードを追加する」をクリック。

適当な住所を入力し、クレジットカード情報を登録する。    
ここで「アカウントに資格がありません。」とか言われてたらちゃんとリンクの[参加資格](https://business.twitter.com/ja/help/overview/about-eligibility-for-twitter-ads.html)を読む。  

ここでクレジットカードの有効性を確認されるためか、1度100円が決済されるが3分後くらいには100円が返還された。
![](https://lh5.googleusercontent.com/NRpOg8rNSToyauEw4to0CFTa6E41rjbOzltHi3OhWFBJOTS9c51oIt9-t4M=w2400)

正しく登録できたなら、[https://ads.twitter.com/](https://ads.twitter.com/) に戻ると「クリエイティブ」というタブが追加されているはずである。  

「クリエイティブ」をクリックし、ここで「カード」を選択。
![](https://lh6.googleusercontent.com/Xx06aQ7RkrMd_wSOXmF4o8Cu4JBjqAiJ7XpZwfzr1g0FwwMN5ajL2IQnpXI=w2400)

「カードを作成」をクリックし、ここで「イメージカンバセーショナルカード」もしくは「ビデオカンバセーショナルカード」を選択。  
![](https://lh3.googleusercontent.com/5PZ_30hUrQTA03pz7EUEHiTl7-pLCzmfCuWINWSN4kzgZ4_tKUmONV-hd0Y=w2400)

もしここで選択肢に存在しない場合は、右上の「お問い合わせ」から適当なものを選んで適当な文章をTwitter社に送ると有効化してくれるはずである。  

「カンバセーショナルカードを作成」が横から出てくるのでフォームを入力していく。一番下の「プレビュー」を押すことでどのように実装されるか確認できる。

* メディア  
用意した素材をアップロードする
* ハッシュタグ  
ボタンの中に表示される文章である。
(例: #○○○○ でツイート)
* ハッシュタグ1のツイートメッセージ  
ボタン押すと埋められるツイートの文字列
* ヘッドライン  
カードの中の文章
* お礼のテキスト  
ツイートした後にでてくるカードの中の文章
* お礼のURL  
ツイートした後そのカードがそのユーザーに対して押したときに飛ばされる先。  

今回は画像に[フリー素材写真ぱくたそ様](https://www.pakutaso.com)の[猫の寝顔写真](https://www.pakutaso.com/20171003283post-13605.html)をお借りさせてもらった。  
URLは " https://twitter.com/intent/tweet?text=にゃーん " と設定。  

「作成」ボタンを押して完成。  

完成したカードの上にカーソルを合わせると、目のアイコンが出てくるので「プレビュー」をクリック 
![](https://lh5.googleusercontent.com/rtpe25b7BvslkTwetIrxd4day04rdv1boPIyeKEswLWgiAnQEmIc1SGj6B8=w2400)

一番下のリンクをコピー (横の絵文字を押せば勝手にコピーしてくれる)
![](https://lh5.googleusercontent.com/kSh-w80_4NJv-rsfFrw8SPkuv2XaSniYDaYZfN3uJ9TFAH2ZxKwuugBO87g=w2400)

そのリンクをツイートすると以下のようにカードが埋め込まれた状態でツイートされる。
![](https://lh3.googleusercontent.com/BfTInrDKWeoVMgTHxrObsuFNURE7GO19S4sDRRZAY6BFZdLW__u1io60R7w=w2400)

ボタンを利用して、ツイートすると以下のようになる。
![](https://lh6.googleusercontent.com/S5a7XE4LuUcKainCD19pGjOxO1Ncijo07F2aOQQogEFuXxntvLe7jv0sl-4=w2400)

もう一度カードを押すと…
![](https://lh3.googleusercontent.com/ef_k0JaPjJNtkdDgDNpT9a7rm-WJ9ZaJEHIqRtkOaQjl58Hlz51lpB5mGkI=w2400)

できた！  
カード付きのツイートを固定ツイートにしておけばいつでも「にゃーん」できる！

### 完成したツイートがこちら


<blockquote class="twitter-tweet" data-lang="ja"><p lang="und" dir="ltr"><a href="https://t.co/pYwN6vVlhe">https://t.co/pYwN6vVlhe</a></p>&mdash; うにゃ (@unya_2) <a href="https://twitter.com/unya_2/status/937342751452012544?ref_src=twsrc%5Etfw">2017年12月3日</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
環境によって文字化けしたり正しく表示されないが、twitter.com上、アプリ内だと動作する。  
URLエンコードしたら直るかな？  
Twitter Liteだと表示されなかったりなのでアプリで見てください。  

### 一般的なカードと広告カードの違い
* 自分の管理下にないURLをリンクすることができる
* (カンバセーショナルカードならば)カードが他者にツイートされ拡散力がある
* カード専用のURLが生成される
* 動画を埋め込むことができる
* ads.twitter.comで直感的にカードを作ることができる
  

おわり！