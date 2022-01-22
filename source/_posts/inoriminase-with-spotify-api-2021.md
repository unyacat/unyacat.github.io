---
title: SpotifyAPIで見る水瀬いのり楽曲
thumbnail: /images/inoriminase-with-spotify-api-2021/thumbnail.png
twitter_card: summary_large_image
toc: true
tags:
  - 水瀬いのり
  - Spotify
date: 2021-12-12 15:00:00
---

Spotifyには楽曲の特徴量を取得できるAPIがあります．

BPMやキーなど一意に決まりそうな特徴量もありますが，ダンスのしやすさやポジティブさなど曖昧な数値も取得することが出来ます．

<div class="bcard-wrapper"><span class="bcard-header"><div class="bcard-site"><a href="https://developer.spotify.com/documentation/web-api/reference/" rel="nofollow" target="_blank"></a></div><div class="bcard-url"><a href="https://developer.spotify.com/documentation/web-api/reference/" rel="nofollow" target="_blank">https://developer.spotify.com/documentation/web-api/reference/</a></div></span><span class="bcard-main"><div class="bcard-title"><a href="https://developer.spotify.com/documentation/web-api/reference/" rel="nofollow" target="_blank">Web API Reference | Spotify for Developers</a></div><div class="bcard-description">Music, meet code. Powerful APIs, SDKs and widgets for simple and advanced applications.
</div></span></div>

これを用いて水瀬いのりさんの楽曲を覗いてみました．

今回は，danceability(ダンスのしやすさ)，energy(活力さ)，acousticness(アコースティックさ)，liveness(ライブ音源っぽさ)，valence(ポジティブさ)に注目してみます．



<!-- more -->



## 🎵取得範囲

水瀬いのりさんがライブツアーで歌う楽曲とします．

具体的には，2021年末までにリリースされた「夢のつぼみ」以降のシングル・アルバム + 「まっすぐに、トウメイに。」です．

アルバムとシングルどちらも入っている曲も値が違ったためどちらとも取得しました．

## 👑ランキング

特徴量と説明，上位・下位，感想の順に書いていきます．

### 💃danceability(ダンスのしやすさ)

テンポ、リズムの安定性、ビートの強さ、全体的な規則性に基づいてダンスのしやすさを表現しています．高いほどダンスに適しています．

- 🥇1位: Morning Prism(0.726)
	
	<iframe src="https://open.spotify.com/embed/track/1Xn4m8cYJVos2xZortMGUW?utm_source=generator" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>
- 最下位: 僕らは今(0.198)
	
	<iframe src="https://open.spotify.com/embed/track/6RSETdPr48E4ICkTfmMG6W?utm_source=generator" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>

朝をテーマとした曲であるMorning Prismが1位でした．常に同じ調子で曲が進行するのでリズムの安定性という面では納得です．

反対にライブ映えする楽曲である「僕らは今」や「Ready Steady Go!」は下のほうになりました．

### 💪energy(活力さ)

高いほどエネルギッシュです．デスメタルでは高く，クラシックでは小さくなります．ダイナミックレンジ、知覚されるラウドネス、音色、オンセットレート、一般的なエントロピーなどに基づきます．

- 🥇1位: 夢のつぼみ(0.992)
	
	<iframe src="https://open.spotify.com/embed/track/3kOSLbJuIGEJPukQrsWW6a?utm_source=generator" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>
- 最下位: いつもずっと(0.41)
	
	<iframe src="https://open.spotify.com/embed/track/3sgGBPeJljUchFDW3GX4TQ?utm_source=generator" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>

デビューシングルがかなり高い値を取っての1位．元気の良さが楽曲にも現れていることでしょうか．下には「いつもずっと」「あの日の空へ」「BLUE COMPASS」など落ち着くような，少し長めの曲が並びました．

### 🎸acousticness(アコースティックさ)

高いほど非電気楽器的な楽曲です．

- 🥇1位: BLUE COMPASS(0.884)
	
	<iframe src="https://open.spotify.com/embed/track/5llfQWIaGFlL9OM4C7inAe?utm_source=generator" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>
- 最下位: クリスタライズ(0.000511)
	
	<iframe src="https://open.spotify.com/embed/track/1Upx0jgN8fU8DDerhHYyQe?utm_source=generator" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>

数値に大きく差が付きました．energy項で下の方に並んだ楽曲ではこちらでは上位に入っています．「クリスタライズ」は納得の最下位．一つ上の「Catch the Rainbow!」と比べても1桁違い，圧倒的電子音楽ないのり楽曲と言えます．

### 🎤liveness(ライブ音源っぽさ)

高いほどライブ音源に近い値です．0.8を超えればライブ音源の可能性が高いです．

- 🥇1位: Dreaming Girls(0.544)
	
	<iframe src="https://open.spotify.com/embed/track/4xrUMkfaW1jsfmHo5oao5w?utm_source=generator" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>
- 最下位: Ready Steady Go!(0.0375)
	
	<iframe src="https://open.spotify.com/embed/track/4WHBEowThZOHkuBxElmgvs?utm_source=generator" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>

「Dreaming Girls」をライブっぽさという観点で聴いたことはありませんでした．でもこのランク付けなら「Ready Steady Go!」もライブっぽい気がするのですが・・・！？

### 🥰valence(ポジティブさ)

valence の値が大きいほど，ポジティブ（Happy, Cheeful, euphoric: 楽しい、陽気、多幸的）です．逆に値が低いとネガティブ (sad, depressed, angry: 悲しい、抑圧された、怒り) な楽曲です．

- 🥇1位: 夏の約束(0.941)
	
	<iframe src="https://open.spotify.com/embed/track/2WhsifNwNIyUx9LFuxqLUC?utm_source=generator" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>
- 最下位: 僕らは今(0.149)
	
	<iframe src="https://open.spotify.com/embed/track/6RSETdPr48E4ICkTfmMG6W?utm_source=generator" width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>

これも数値に大きな幅が生まれました．[女性向けコンテンツ](http://rejetweb.jp/hsd3/)の主題歌としてリリースされていることもあり取得範囲の中では少し特殊な楽曲である「夏の約束」が1位．一番下の「僕らは今」はlivenessさも低いところから見るとSpotifyさんは良さをわかってくれていないようです・・・．(いい曲ですよ！)

## 🖥結果生データ
<div class="bcard-wrapper"><span class="bcard-header"><div class="bcard-site"><a href="https://docs.google.com/spreadsheets/d/1qpGOeD6z1jSpTcGcbhGwAX54eIv-hTfdEJTnNHrrhpM/edit?usp=sharing&usp=embed_facebook" rel="nofollow" target="_blank">Google Docs</a></div><div class="bcard-url"><a href="https://docs.google.com/spreadsheets/d/1qpGOeD6z1jSpTcGcbhGwAX54eIv-hTfdEJTnNHrrhpM/edit?usp=sharing&usp=embed_facebook" rel="nofollow" target="_blank">https://docs.google.com/spreadsheets/d/1qpGOeD6z1jSpTcGcbhGwAX54eIv-hTfdEJTnNHrrhpM/edit?usp=sharing&usp=embed_facebook</a></div></span><span class="bcard-main"><div class="bcard-title"><a href="https://docs.google.com/spreadsheets/d/1qpGOeD6z1jSpTcGcbhGwAX54eIv-hTfdEJTnNHrrhpM/edit?usp=sharing&usp=embed_facebook" rel="nofollow" target="_blank">Spotify APIで見る水瀬いのり楽曲</a></div><div class="bcard-description">result

track_name,album_name,album_type,danceability(ダンスのしやすさ・高いほど踊りやすい),energy(活力さ・高いほどエネルギッシュ),key(https://en.wikipedia.org/wiki/Pitch_class),loudness(dB値・音の大きさ),mode(major=1 minor=0),speechiness(言語の多さ),acousticness(アコースティックさ・高いほど非電気楽器的),instrumentalness(インストルメンタルさ・目安0.5以上でインストルメンタルと判断できる),liv...</div></span></div>

## 💭感想

見たことない観点で楽曲を見れる楽しさもありますね．

BPM推定は「Happy Birthday」が203.961と圧倒的な値を叩き出してくれました．高難易度誕生日会が開けますね・・・．(体感98-102くらいな気がします．序盤(ゆっくり)とサビ(早め)の部分の両方をいい感じにするとこんなものなのかもしれません)
