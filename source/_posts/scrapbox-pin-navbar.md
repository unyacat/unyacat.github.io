---
title: Scrapbox でナビゲーションバーにホームに戻るボタンを埋め込む UserCSS
date: 2021-02-06 11:40:00
thumbnail: /images/scrapbox-pin-navbar/thumbnail.png
tags:
- Scrapbox
---



Scrapbox のナビゲーションバーを一番上にピン留めしてそこにホームに戻るボタンを配置する CSS です．

どこからでもホームに戻れるのでとても便利です．

2021年2月に本家のCSSが更新されていたのを確認したので更新しました．

<!-- more -->

## 🌸 動作

![](/images/scrapbox-pin-navbar/output.gif)





## 👩‍💻 UserCSS

### アイコン隣の矢印を消す

```CSS
span.kamon.kamon-caret-down {
	display: none;
}
```



### ホームに移動するボタンを上に固定する

```CSS
.quick-launch .flex-box .flex-item .left-box {
   position: fixed;
   top: 0em;
   left: calc(calc(100% - 1184px) * 0.5 + 48px);
   color: white;
   z-index: 1000;
 }

 @media (max-width: 1276px) {
   .quick-launch .flex-box .flex-item .left-box {
     left: 86px;
   }
 }

 @media (max-width: 992px) {
   .quick-launch .flex-box .flex-item .left-box {
     left: 64px;
   }
 }

 @media (max-width: 768px) {
   .quick-launch .flex-box .flex-item .left-box {
     left: 56px;
   }
 }
```

もっと適切な設定はありそうですがとりあえず．

では良い Scrapbox ライフを👋



