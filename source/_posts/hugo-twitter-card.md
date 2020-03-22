---
date: 2018-12-12
title: Hugo で Twitter Cards をいい感じに適用させる
---

この記事は [Kaigen Discord Advent Calendar 2018](https://adventar.org/calendars/2886) の12月12日枠です。

## このブログを見てできること

記事.mdに画像 URL が埋め込まれているときは summary_large_image (2:1の画像が使われた大きめのカード)を適用し、ない場合は summary (正方形の画像が使われた小さめのカード) で埋め込めるようになる機能を実装します。

<!--more-->

標準実装されている機能だと画像が一切適用されなかったので作りました。

### 環境

使用テーマ:  [Icurus](https://github.com/digitalcraftsman/hugo-icarus-theme)

```toml
# 記事.md
+++
banner = "https://lh5.googleusercontent.com/hogehoge"
description = 
Title = 
etc = 
+++

# config.toml
[social]
 	twitter         = "unya_2"
```

バージョン

```css
$ hugo env
Hugo Static Site Generator v0.49.2 windows/amd64
```



## 実装

1. layout/partials 下に twitter_cards.html を作ります。  
```html
  {{- with $.Params.banner -}}
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:image" content="{{ $.Params.banner }}"/>
{{ else -}}
<meta name="twitter:card" content="summary"/>
<meta name="twitter:image" content="{{ .Site.Params.avatar | absURL }}"/>
{{- end }}
<meta name="twitter:title" content="{{ .Title }}"/>
<meta name="twitter:description" content="{{ with .Description }}{{ . }}{{ else }}{{if .IsPage}}{{ .Summary }}{{ else }}{{ with .Site.Params.description }}{{ . }}{{ end }}{{ end }}{{ end -}}"/>
{{ with .Site.Social.twitter -}}
<meta name="twitter:site" content="@{{ . }}"/>
<meta name="twitter:creator" content="@{{ . }}"/>
{{ end -}}
```
3行目 banner ではない名前の設定をしていれば置換したり、banner のところに相対パスを書いているならば "| absURL" を追加したりしてください。  
config.toml に Twitter ID を書いていないのならば 11，12 行目 content 部に Twitter ID を直接書くことでも対応可能です．

1. head.html に埋め込みます。
```html
    {{ partial "twitter_cards" . }}
```
を head タグ内の好きなところに追記します。  

1. おわり。  
  [Card validator](https://cards-dev.twitter.com/validator) に URL を打ち込むと確認し、即時実装可能です。