---
title: Scrapbox でナビゲーションバーにホームに戻るボタンを埋め込む UserCSS
date: 2020-12-10 11:20:00
thumbnail: /images/scrapox-pin-navbar/thumbnail.png
tags:
- Scrapbox
---

Scrapbox のナビゲーションバーを一番上にピン留めしてそこにホームに戻るボタンを配置する CSS です．

どこからでもホームに戻れるのでとても便利です．

<!-- more -->

## 🌸 動作

![](/images/scrapbox-pin-navbar/output.gif)





## 👩‍💻 UserCSS

### ナビゲーションバーを固定する

ナビゲーションバーを固定する CSS は他の人が提供してくれているので利用します．



<div class="bcard-wrapper"><span class="bcard-header withgfav"><div class="bcard-favicon" style="background-image: url(https://www.google.com/s2/favicons?domain=https://scrapbox.io/kiito-themes/%E3%83%8A%E3%83%93%E3%82%B2%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%90%E3%83%BC)"></div><div class="bcard-site"><a href="https://scrapbox.io/kiito-themes/%E3%83%8A%E3%83%93%E3%82%B2%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%90%E3%83%BC" rel="nofollow" target="_blank">Responsive Grid Theme</a></div><div class="bcard-url"><a href="https://scrapbox.io/kiito-themes/%E3%83%8A%E3%83%93%E3%82%B2%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%90%E3%83%BC" rel="nofollow" target="_blank">https://scrapbox.io/kiito-themes/%E3%83%8A%E3%83%93%E3%82%B2%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%90%E3%83%BC</a></div></span><span class="bcard-main withogimg"><div class="bcard-title"><a href="https://scrapbox.io/kiito-themes/%E3%83%8A%E3%83%93%E3%82%B2%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%90%E3%83%BC" rel="nofollow" target="_blank">ナビゲーションバー - Responsive Grid Theme</a></div><div class="bcard-description">ページ上のナビゲーションバーのデザイン #UserCSS #design #spin-off メニュー固定 ソース: /scrasobox/ヘッダーメニューを固定する 若干改変 code:style.css @media screen and (min-height: 600px) and (min-width: 768px) { body:not(.presentation) { padding</div><a href="https://scrapbox.io/kiito-themes/%E3%83%8A%E3%83%93%E3%82%B2%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%90%E3%83%BC" rel="nofollow" target="_blank"><div class="bcard-img" style="background-image: url(https://scrapbox.io/assets/img/content-logo.png)"></div></a></span></div>



### アイコン隣の矢印を消す

```CSS
span.kamon.kamon-caret-down {
	display: none;
}
```



### ホームに移動するボタンを上に固定する

```
.quick-launch .flex-box .flex-item .left-box {
   position: fixed;
   top: 0.45rem;
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



