---
title: Splatoon3の戦績をstat.inkに自動アップロードするGitHub Actions
tags:
  - GitHub-Actions
date: 2022-12-29 16:41:46
---

Splatoon3の戦績をstat.inkに自動アップロードするGitHub Actions

<!-- more -->

GitHub Actions上で実行すると環境を持たなくてよいメリットとともに最新のコードでアップロードできるので任天堂側の仕様変更による認証ミスで詰まらずに済むというメリットがあります．(※たぶん)

## やり方

[s3s](https://github.com/frozenpandaman/s3s)を用いてstat.inkにデータをアップロードします．

### 1. s3sを手元で動かす

手元で動かしてstat.inkにアップロードできるかどうかを試すとともに認証情報を手に入れます．

`git clone https://github.com/frozenpandaman/s3s`

`cd s3s`

`python3 -m pip install -r requirements.txt`

`python3 s3s.py -nsr -r`

コマンド実行して，

* stat.incの鍵をコピー&ペーストします．

* 生成された Nintendo.com のリンクを開いてこの人にするを右クリックしてリンクをコピーして貼り付けます．

両方入力したら戦績がアップロードされるはずなので待ちます．

s3sディレクトリにconfig.txtが生成されているはずなので開きます．


### 2. ymlに認証情報を書いてコミットする

適当なリポジトリを作って `.github/workflows` 以下に `適当なファイル名.yml` を作って以下のコードをペタリしておきます．

11行目以下env部をconfig.txtから同じ名前の部分を置換します．(GitHub ActionsのEnvironment secretsに書くべきな気はする) 

[Gist](https://gist.github.com/unyacat/6a44967b49ac239f32483506f16d8e27)

```yaml
name: Splatoon3 Battlelog Uplorder

on:
  schedule:
    - cron: '0 19 * * *'  # 朝4時
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    env:  # 適宜置換する
      API_KEY: "***"
      ACC_LOC: "***"
      GTOKEN: "***"
      BULLETTOKEN: "***"
      SESSION_TOKEN: "***"
      F_GEN: "***"

    name: Splatoon3 Battlelog Uploader
    steps:
      - name: Set up Python 3.11
        uses: actions/setup-python@v4
        with:
          python-version: 3.11

      - name: Checkout frozenpandaman/s3s
        uses: actions/checkout@v3
        with:
          repository: 'frozenpandaman/s3s'
          path: s3s

      - name: Generate config.txt
        working-directory: s3s
        run: |
          echo '{"api_key": "${{ env.API_KEY }}", "acc_loc": "${{ env.ACC_LOC }}", "gtoken": "${{ env.GTOKEN }}", "bullettoken": "${{ env.BULLETTOKEN }}", "session_token": "${{ env.SESSION_TOKEN }}", "f_gen": "${{ env.F_GEN }}" }' > config.txt
          cat config.txt
      - name: Install s3s requirements
        working-directory: s3s
        run: |
          pip install -r requirements.txt
      - name: Run s3s
        working-directory: s3s
        run: |
          python3 s3s.py -nsr -r
          # python3 s3s.py -osr -r
```

コミットすると毎朝4時に自動で戦績がアップロードされます．
