---
date: 2017-04-08
title: Twitterのアイコンはちょっとした工夫で綺麗になる
---

きれいなアイコンは見ていて気持ちが良いものです．

<!--more-->

## 切り抜きたい

Twitter でアップロードしたときに出てくる切り抜き機能を使うと画像が劣化します．

そのため予め端末側で標準でついてる機能でもいいので画像を切り抜いて置くと良いでしょう．



## 画質の向上を図る

切り抜くことで画質が悪くなっても画質を向上させる手段があります．

[waifu2x](http://waifu2x.udp.jp/index.ja.html)を試してみます．

<iframe class="hatenablogcard" style="width:100%;height:155px;max-width:680px;" title="waifu2x" src="https://hatenablog-parts.com/embed?url=http://waifu2x.udp.jp/index.ja.html" width="300" height="150" frameborder="0" scrolling="no"></iframe>

2回目以上やるとちょっと違和感がある場合が増えてくるので何回か試行してみるといいでしょう。  

この時にAPIのアップロード上限、700KBを超えないように気をつけます。  

もし超えてしまった場合、またPCスマホの標準の切り抜き機能でちょっと切り抜くと画像容量がぐっと減ることがあるので試してみてください．

## アップロード

このサイトを利用します。

[TwitterのアイコンをAPI経由でアップロードするツール](https://retrorocket.biz/upico/)

<iframe class="hatenablogcard" style="width:100%;height:155px;max-width:680px;" title="TwitterのアイコンをAPI経由でアップロードするツール" src="https://hatenablog-parts.com/embed?url=https://retrorocket.biz/upico/" width="300" height="150" frameborder="0" scrolling="no"></iframe>

サイト下の注意点をよく読んで利用しましょう． 

よく失敗するのは「700KB以上の画像をアップロードできない」「iOSからPNGの透過データが黒くなる」です．


### 4.完成

自分のTwitterを見ると大きく綺麗な画像がアップロードできていることが確認できます．

公式のスマホアプリからだとアプリ側でまた画像が縮小するので効果がわかりにくいかもしれませんが，公式以外のアプリやWeb版公式を使ったりすると綺麗な画像をアップロードできていることがよくわかります．
