---
title: 二酸化炭素濃度センサーMH-Z14AとNanoPiでブラウザで見れる濃度計を作った(後編)
date: 2021-02-07 22:00:00
thumbnail: /images/mh-z14a-2/thumbnail.png
toc: true
tags:
  - 日記
  - mh-z14a
  - NanoPi
  - 二酸化炭素濃度
---

集中力を高めるためには換気も大切らしい・・・ということでブラウザで見れる二酸化炭素濃度計を作りました．この記事は後編です．

<!-- more -->
[前編](https://unyacat.net/2021/02/06/mh-z14a-1/)まででセンサーから値を取得できるようになったので一安心しました．

## 適当に Web UI を構築する

必要とされる機能をざっと書き上げたとき以下のようなものになりました．

- 定期的な記録
- 過去の情報の閲覧
- 自動的な更新
- 通知機能

## 実装

![/images/mh-z14a-2/1.png](/images/mh-z14a-2/1.png)

<a href="https://github.com/unyacat/MH-Z14A-WebUI"><img src="https://github-link-card.s3.ap-northeast-1.amazonaws.com/unyacat/MH-Z14A-WebUI.png" width="460px"></a>

### 定期的な記録

定時実行といえば crontab かな，と思いこんでいたのですが APScheduler というライブラリでも定時実行できるようで Flask 拡張もあったのでこれで実装することにしました．

[viniciuschiele/flask-apscheduler](https://github.com/viniciuschiele/flask-apscheduler)

指定時間おきに関数を呼び出せるので可能性は無限大です．Webhook で通知させたいとかならすぐにできそうです．

取得して数値を日付とともに SQLite に保存していきます．

### 画面

Vue + Vuetify +  vue-chart で行いました．手軽に綺麗な画面を構築できるので使っていて楽しいです．

### リアルタイム更新

vue-chart の時間幅を記録時間ごとに変えることで実質リアルタイムグラフを実装できました．

また，リアルタイムの数値を見れるように 10 秒おきにセンサーに値を取りに行くようにしました．

## 電源起動するたびに稼働するように設定する

crontab で NanoPi が起動するたびにFlaskが起動するように登録しておきます．

`@reboot python3 app.py`

## 効果・感想

上の画像を見てもわかる通り，締め切ってオンライン授業を受けていたら線形的に上昇，部屋を出てしばらくすれば一定の値を示し，換気をするとグッと下がる，など思っていたより換気による効果が出ていて面白かったです．

通知機能は換気に支配される生活が嫌だったので実装しませんでした．

換気の重要性を理解し，意識が変わったということだけでも効果は大きそうです．