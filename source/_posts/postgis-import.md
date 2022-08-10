---
title: PostGISにshpファイルをインポートする(Windowsで変換してDockerでインポート)
tags:
  - PostGIS
  - PostgreSQL
  - Windows
  - Linux
date: 2022-08-04 23:02:00
---

GISデータをDocker上PostGISにインポートする方法．  
手元のWindows機でshpファイルを処理した後，Linux機にアップロードしてインポートするときの流れ．

<!-- more -->
## 流れ

今回は国土交通省のGISデータをインポートする．

### shp2pgsqlをダウンロード

shp2pgsqlはshpファイルをSQLファイルに変換するやつ．  
PostgreSQLのバージョンにあった番号が振られてるやつ以下から落としてきたら良さそう  
[https://download.osgeo.org/postgis/windows/](https://download.osgeo.org/postgis/windows/)

展開した後，コマンドプロンプトを開き，中の`bin`ディレクトリに移動する．

### shpをSQLに変換

`.\shp2pgsql -W cp932 -D -I -s 4612 .\{shp_filename}.shp {table_name} > {hogehoge}.sql`

`-W`：文字コードの指定  
`-D`：ダンプ形式で出力(インポート効率がいい)  
`-I`:空間インデックスの作成  
`-s`：座標系指定  

参考: https://qiita.com/miyatomo1122/items/0cb67455c294943ae649#%E3%82%B7%E3%82%A7%E3%83%BC%E3%83%97%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AE%E5%8F%96%E3%82%8A%E8%BE%BC%E3%81%BF

### データベースの作成
コンテナの中に入る  
`$ docker exec -it {container_name} sh`

PostgreSQLに接続
`$ psql -U postgres`  

データベース作成  
`postgres=# CREATE DATABASE {database_name}`

データベース選択  
`postgres=# \c n0221;`

PostGIS有効化  
`postgres=# CREATE EXTENSION postgis;`

### インポート
`# psql -U postgres n0221 < /N02-21_GML/N02-21_RailroadSection.sql`

終わり．インポートできたことを確認する．


## 詰まりどころ

### PowerShellの文字コードのデフォルトがUTF-16LE

`chcp 65001`でUTF-8になる

### PowerShellでリダイレクトすると文字化けする

コマンド実行結果をファイルにリダイレクトしたときのデフォルトの文字コードはUTF-16に設定されている．(ﾄﾞｳｼﾃ)  
UTF-8にする設定もあるようで試してみたけどうまくいかず．  
コマンドプロンプトで実行したら解決．

### PostGISの有効化忘れ

インポート時エラー文
```
ERROR:  function addgeometrycolumn(unknown, unknown, unknown, unknown, unknown, integer) does not exist
LINE 1: SELECT AddGeometryColumn('','stations','geom','4612','MULTIL...
```

解決方法: コンテナ内で，`psql -U postgres -d n0221 -c "CREATE EXTENSION postgis;"`