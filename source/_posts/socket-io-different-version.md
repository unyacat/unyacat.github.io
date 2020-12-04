---
title: socket.io で接続は確認できるがイベントに反応してくれない問題の解決
date: 2020-12-04 14:55:57
thumbnail: images/socket-io-different-version/thumbnail.jpg
tags:
- socket.io
- React
- Node.js
---

socket.io でサーバーに接続されてそうだけどそれ以上何もしてくれなくて困った話．

<!--more-->

## 結論

[socket.io](http://socket.io) のバージョンはクライアントとサーバーで揃えよう

## 事象

環境: Node.js + Express / React 

サーバー側に

```jsx
io.on('connection', function (socket) {
  socket.on('message', (msg) => {
		console.log('socketio connected')
  })
});
```

と書くとたしかに [socket.io](http://socket.io) が接続されてそうなのに emit とか on には何も反応してくれない．

`localStorage.debug = '*';` でデバッグするとどうやら

```jsx
browser.js:181 engine.io-client:socket socket receive: type "error", data "parser error" +8ms
browser.js:181 engine.io-client:socket socket error {"code":"parser error"} +0ms
browser.js:181 socket.io-client:manager error +8ms
browser.js:181 socket.io-client:manager cleanup +0ms
browser.js:181 socket.io-client:manager reconnect attempt error +1ms
browser.js:181 socket.io-client:manager will wait 2696ms before reconnect attempt +0ms
browser.js:181 engine.io-client:socket socket close with reason: "transport error" +1ms
```

と，エラーが出ていることは確認できるけどコードは正しそう．

## 解決

クライアントの [socket.io](http://socket.io) のバージョンが 2.0.3，サーバーのバージョンが 3.0.3 だった．

両者を 3.0.3 に揃えたらうごいた．

```jsx
// server 
const express = require('express');
const app = express();
http = require('http').createServer(app);
const io = require('socket.io')(http, {
  cors: {
    origin: '*',
  }
})
...

// client (React)
import io from "socket.io-client";
const socket = io.connect(":3000");
...
class BulletinBoard extends React.Component<
	... 
	componentDidMount() {
		socket.on('message', function(data: any) {
      console.log(data);
    })
	...
}
```