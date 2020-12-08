---
date: 2017-04-07
title: Twitterのアイコンはちょっとした工夫で綺麗になる
tags:
- Twitter
---

きれいなアイコンは見ていて気持ちが良いものです．

<!--more-->

## 切り抜きたい

Twitter でアップロードしたときに出てくる切り抜き機能を使うと画像が劣化します．

そのため予め端末側で標準でついてる機能でもいいので画像を切り抜いて置くと良いでしょう．



## 画質の向上を図る

切り抜くことで画質が悪くなっても画質を向上させる手段があります．

[waifu2x](http://waifu2x.udp.jp/index.ja.html)を試してみます．

<div class="bcard-wrapper"><span class="bcard-header withgfav"><div class="bcard-favicon" style="background-image: url(https://www.google.com/s2/favicons?domain=http://waifu2x.udp.jp/index.ja.html)"></div><div class="bcard-site"><a href="http://waifu2x.udp.jp/index.ja.html" rel="nofollow" target="_blank"></a></div><div class="bcard-url"><a href="http://waifu2x.udp.jp/index.ja.html" rel="nofollow" target="_blank">http://waifu2x.udp.jp/index.ja.html</a></div></span><span class="bcard-main"><div class="bcard-title"><a href="http://waifu2x.udp.jp/index.ja.html" rel="nofollow" target="_blank">waifu2x</a></div><div class="bcard-description">深層畳み込みニューラルネットワークによる二次元画像のための超解像システム。 写真にも対応。</div></span></div>


2回目以上やるとちょっと違和感がある場合が増えてくるので何回か試行してみるといいでしょう。  

この時にAPIのアップロード上限、700KBを超えないように気をつけます。  

もし超えてしまった場合、またPCスマホの標準の切り抜き機能でちょっと切り抜くと画像容量がぐっと減ることがあるので試してみてください．

## アップロード

このサイトを利用します。

[TwitterのアイコンをAPI経由でアップロードするツール](https://retrorocket.biz/upico/)

<div class="bcard-wrapper"><span class="bcard-header"><div class="bcard-site"><a href="https://retrorocket.biz/upico/" rel="nofollow" target="_blank"></a></div><div class="bcard-url"><a href="https://retrorocket.biz/upico/" rel="nofollow" target="_blank">https://retrorocket.biz/upico/</a></div></span><span class="bcard-main"><div class="bcard-title"><a href="https://retrorocket.biz/upico/" rel="nofollow" target="_blank">TwitterのアイコンをAPI経由でアップロードするツール</a></div><div class="bcard-description"></div></span></div>

サイト下の注意点をよく読んで利用しましょう． 

よく失敗するのは「700KB以上の画像をアップロードできない」「iOSからPNGの透過データが黒くなる」です．


### 4.完成

自分のTwitterを見ると大きく綺麗な画像がアップロードできていることが確認できます．

公式のスマホアプリからだとアプリ側でまた画像が縮小するので効果がわかりにくいかもしれませんが，公式以外のアプリやWeb版公式を使ったりすると綺麗な画像をアップロードできていることがよくわかります．
