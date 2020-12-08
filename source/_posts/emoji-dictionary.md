---
title: 絵文字辞書📚を導入して文章を彩る🌸
date: 2020-12-09 00:00:00
thumbnail: ./images/emoji-dictionary/thumbnail.png
tags:
- 絵文字
- 日記
---

絵文字があると文章が華やか✨になりますし，気持ちも晴れやかになります🤗

Apple🍎製品だと豊かな絵文字の変換が可能ですが，Windows 💠だと思うように変換してくれないので残念ですよね😿

もしかして辞書📚があるのではないかと思い探してみると🔍・・・ありました👀

<!--more-->

<div class="bcard-wrapper"><span class="bcard-header withgfav"><div class="bcard-favicon" style="background-image: url(https://www.google.com/s2/favicons?domain=https://github.com/peaceiris/emoji-ime-dictionary)"></div><div class="bcard-site"><a href="https://github.com/peaceiris/emoji-ime-dictionary" rel="nofollow" target="_blank">GitHub</a></div><div class="bcard-url"><a href="https://github.com/peaceiris/emoji-ime-dictionary" rel="nofollow" target="_blank">https://github.com/peaceiris/emoji-ime-dictionary</a></div></span><span class="bcard-main withogimg"><div class="bcard-title"><a href="https://github.com/peaceiris/emoji-ime-dictionary" rel="nofollow" target="_blank">peaceiris/emoji-ime-dictionary</a></div><div class="bcard-description">日本語で絵文字入力をするための IME 追加辞書 📙 Google 日本語入力などで日本語から絵文字への変換を可能にする IME 拡張辞書です - peaceiris/emoji-ime-dictionary</div><a href="https://github.com/peaceiris/emoji-ime-dictionary" rel="nofollow" target="_blank"><div class="bcard-img" style="background-image: url(https://repository-images.githubusercontent.com/152870481/df5cbf00-61d0-11e9-9502-d1f252ce55fb)"></div></a></span></div>

見た限り直近にも更新🆙されていて良さそうです👍



## 🛠 改造

このままだと絵文字を使うには毎度コロン `:` を入力しなくてはいけません．
私は文章入力をしながら自然に絵文字を利用したいのでこれを削っていきます．

<div class="bcard-wrapper"><span class="bcard-header withgfav"><div class="bcard-favicon" style="background-image: url(https://www.google.com/s2/favicons?domain=https://gist.github.com/unyacat/aa2b9fc40d27a48ea2bcf8079cabe9cd)"></div><div class="bcard-site"><a href="https://gist.github.com/unyacat/aa2b9fc40d27a48ea2bcf8079cabe9cd" rel="nofollow" target="_blank">Gist</a></div><div class="bcard-url"><a href="https://gist.github.com/unyacat/aa2b9fc40d27a48ea2bcf8079cabe9cd" rel="nofollow" target="_blank">https://gist.github.com/unyacat/aa2b9fc40d27a48ea2bcf8079cabe9cd</a></div></span><span class="bcard-main withogimg"><div class="bcard-title"><a href="https://gist.github.com/unyacat/aa2b9fc40d27a48ea2bcf8079cabe9cd" rel="nofollow" target="_blank">v2.2.1 / MIT License: https://github.com/peaceiris/emoji-ime-dictionary/blob/main/LICENSE</a></div><div class="bcard-description">v2.2.1 / MIT License: https://github.com/peaceiris/emoji-ime-dictionary/blob/main/LICENSE - emoji_alt.txt</div><a href="https://gist.github.com/unyacat/aa2b9fc40d27a48ea2bcf8079cabe9cd" rel="nofollow" target="_blank"><div class="bcard-img" style="background-image: url(https://github.githubassets.com/images/modules/gists/gist-og-image.png)"></div></a></span></div>

削りました．(Gist は v2.2.1 リリースのものです)

Readme 📝に従って，無事に登録できました✨

![Google IME に登録した](/images/emoji-dictionary/gime.png)

では良い絵文字ライフを👋



## [おまけ] Python で詰まった

emoji.txt を改造するときに Python で行いました．ファイルに書き込むところを書くのはめんどうだったので標準出力に垂れ流してそれをファイルに書き込もうとしました．

しかし...標準出力はできるのに出力先をファイルにしようとするとエラーを吐いてしまいました．

```
$ python main.py >> output.txt
 Traceback (most recent call last):
 ...(略)...
 UnicodeEncodeError: 'cp932' codec can't encode character '\U0001f524' in position 4: illegal multibyte sequence
```



正解💡

```python
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('./emoji/emoji.txt', encoding="utf-8") as f:
    for line in f:
        print(line[1:], end='')

```

