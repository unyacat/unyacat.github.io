---
title: bootstrap-vueを利用するとsr-only要素が見える問題
thumbnail: /images/bootstrap-vue-version-4-5/sr1.png
twitter_card: summary_large_image
toc: true
tags:
  - Vue
  - BootstrapVue
date: 2021-09-19 23:15:00
---


[bootstrap-vue](https://bootstrap-vue.org/)のGetting Startedにしたがってインストールすると謎の文字がでてくることがあります．

<!-- more -->

例えば...
![](/images/bootstrap-vue-version-4-5/sr1.png)


## ✅ 解決策
`$ npm install bootstrap@4.5.3`

## これ何
謎の文字は `sr-only` というクラスを持っています．
`<label class="sr-only" id="_BVID__6__value" for="__BVID__6">2021年9月19日日曜日</label>`
これはスクリーンリーダー(音声読み上げソフト)のためのようです．
つまり画面上には必要ないものが見えていることになります．

### 原因
bootstrapのバージョンが新しすぎるためです．
bootstrap-vueではv4.5.3が推奨されていますが，Getting Startedの通りに`npm install bootstrap`をするとsr-onlyが廃止されたv5をダウンロードしてきます．
v4.5.3を指定してダウンロードすることで見えなくなります．

### リンク
Getting Started | BootstrapVue - [https://bootstrap-vue.org/docs]()

Accessibility · Bootstrap v5.0 - [https://getbootstrap.com/docs/5.0/getting-started/accessibility/]()
