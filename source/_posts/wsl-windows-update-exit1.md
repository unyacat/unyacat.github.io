---
title: Windows Updateを適用したらWSLが起動しなくなった
date: 2021-01-16 21:49:50
toc: true
tags:
  - 日記
  - Windows
  - WSL
---

備忘録です．今日，Windows Update を適用してバージョン20H2(ビルド 19042.746)に更新したところWSLが起動しなくなりました．

結局初期化して解決させました．

<!-- more -->

## 現象
Ubuntu が起動しなくなりました．最初は VSCode から WSL にアクセスできないとエラーが発生して何事かと思いましたが WIndows Terminal から開こうとしても [プロセスはコード 1 で終了しました] ([process exited with code 1])とだけ表示されて何もできなくなってしまいました．

![](/images/wsl-windows-update-exit1/process-exit1.png)

## 試す
管理者でPowershellを起動して `netsh winsock reset` と入力することで復活することもあるようです．

<div class="bcard-wrapper"><span class="bcard-header withgfav"><div class="bcard-favicon" style="background-image: url(https://www.google.com/s2/favicons?domain=https://github.com/microsoft/WSL/issues/4899)"></div><div class="bcard-site"><a href="https://github.com/microsoft/WSL/issues/4899" rel="nofollow" target="_blank">GitHub</a></div><div class="bcard-url"><a href="https://github.com/microsoft/WSL/issues/4899" rel="nofollow" target="_blank">https://github.com/microsoft/WSL/issues/4899</a></div></span><span class="bcard-main withogimg"><div class="bcard-title"><a href="https://github.com/microsoft/WSL/issues/4899" rel="nofollow" target="_blank">WSL2-Ubuntu [process exited with code 1] under updating 19564.1005 · Issue #4899 · microsoft/WSL</a></div><div class="bcard-description">As the title. I updated the insider version to 19564.1005. WSL2-Ubuntu cannot start. I got [process exited with code 1] error with Terminal-run.</div><a href="https://github.com/microsoft/WSL/issues/4899" rel="nofollow" target="_blank"><div class="bcard-img" style="background-image: url(https://avatars2.githubusercontent.com/u/6154722?s=400&v=4)"></div></a></span></div>

しかしこれでは解決せず，また更新プログラムを完全に適用したり再起動を繰り返しましたが変化はありませんでした．

## 初期化

結局Ubuntuを初期化することにしました．

[アプリと機能] > Ubuntu の [詳細オプション] > リセット項 [リセット] をクリック．

Ubuntu を起動しインストールを完了させます．

Powershell で `wslconfig.exe /setdefault Ubuntu` を入力することでデフォルトをUbuntuに設定できました．

