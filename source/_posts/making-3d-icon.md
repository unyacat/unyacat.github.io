---
title: 3Dプリンタで物理アイコンを作った
thumbnail: /images/making-3d-icon/thumbnail.jpg
twitter_card: summary_large_image
tags:
  - 3Dプリンタ
  - Fusion360
date: 2021-07-12 0:30:13
---
画像を元に3Dモデルを生成して自分の利用しているアイコンを3Dプリンタで印刷してみました．
ついでに裏にNFCタグをつけて機能をもたせてみました．

<!-- more --> 
## つくったもの

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">3Dプリンタで物理アイコンを生成した〜 <a href="https://t.co/n1jF4NQOPq">pic.twitter.com/n1jF4NQOPq</a></p>&mdash; うにゃ (@unya_2) <a href="https://twitter.com/unya_2/status/1413106388138561542?ref_src=twsrc%5Etfw">July 8, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

アイコンは [三白眼女の子メーカー｜Picrew ](https://picrew.me/image_maker/37650) で作りました．ありがとうございます🙏

## つくる

### 画像からSTLファイルを作る

画像から STL ファイルにする都合の良いサイトがあったのでこれを活用しました．

<div class="bcard-wrapper"><span class="bcard-header"><div class="bcard-site"><a href="https://imagetostl.com/jp" rel="nofollow" target="_blank"></a></div><div class="bcard-url"><a href="https://imagetostl.com/jp" rel="nofollow" target="_blank">https://imagetostl.com/jp</a></div></span><span class="bcard-main"><div class="bcard-title"><a href="https://imagetostl.com/jp" rel="nofollow" target="_blank">2D画像から3D STLファイルに変換する無料オンラインツール - ImageToStl</a></div><div class="bcard-description">無料で高速なオンラインツールで、.PNGと.JPGの2D画像を3D .STLファイルに変換し、3Dプリンタで印刷したり、お気に入りの3D編集パッケージにロードするのに適しています。ｇｐｇ</div></span></div>

カラー画像のまま入れると高低差がなめらかなのではっきりと凸凹が欲しいなら n 段階で白黒にすると良さそう．
3Dモデルをうまく編集できない人間(私)は画像の段階でいじっておきましょう．



### Fusion360でストラップ穴をつける

Fusion360でストラップを通す穴と土台をつけました．
生成したSTLを読み込むときに大きさが10倍になったのでimagetostlの段階で1/10の大きさにし直しました．(そのままCHITUBOXとかに入れれば正しい大きさになのですが......) 
同じく下面オフセットもimagetostlでできるのですが円形画像だと思ったようにできなかったのでFusion360で作りました．

![](/images/making-3d-icon/fusion.png)

### 印刷
印刷してストラップつけるといい感じ！
![](/images/making-3d-icon/thumbnail.jpg)

## おまけ: 裏にNFCタグを貼ってみる

裏にNFCタグを貼ることで自サイトに飛ぶ機能を持たしてみました．

まるでアイコンが画面の中に移っていくのよう・・・．

<blockquote class="twitter-tweet" data-conversation="none" data-dnt="true"><p lang="ja" dir="ltr">裏にNFCタグ貼ったので名刺代わりにもなる <a href="https://t.co/SBsfaU3q50">pic.twitter.com/SBsfaU3q50</a></p>&mdash; うにゃ (@unya_2) <a href="https://twitter.com/unya_2/status/1413107184875966469?ref_src=twsrc%5Etfw">July 8, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
