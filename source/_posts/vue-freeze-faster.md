---
title: Vue.js でリアクティブを捨てて高速にレンダリングする
date: 2021-01-20 18:07:38
tags:
  - Vue
  - JavaScript
---

Vue.js + vue2-leaflet で v-for を利用している箇所で明らかに遅くなる事象にぶつかってしまいました．

20 個程度の配列だとなめらかに動くのに何千個の配列を扱うとかなり重くなってメモリをモリモリ食って Chrome を落としてしまうほどになってしまうほどでした．

<!-- more -->

## Object.freeze()

リアクティブから解き放つには Object.freeze() を利用すると良いようです．リアクティブを諦めることで高速化を望めるようです．

```jsx
data: function () {
  return {
    data: {"id": 123, "name": "hoge", ...}
  }
}

mounted(): {
  this.data = Object.freeze(this.data)
}
```





早速試してみましたが，どうやら恩恵が受けられているとは思えず速度が改善することはありませんでした．



## 深くまで Object.freeze() が効かない

例えば以下のように，

```jsx
deta = {"id": 123,
 "name": "hoge", 
 "like": {  // ここまで効いてない
   "fruit": "strawberry",      
   "pasta": "carbonara",
   ...    
 }
}
```

子のプロパティを持っていた場合，子は freeze されていないようです．

再帰的に実行することで深くまで Object.freeze() してあげると良さそうです．(あんまり深いとパフォーマンスが心配になりますが)

```jsx
methods: {
  deepFreeze(obj) {
    Object.keys(obj).forEach(prop => {
      if (typeof obj[prop] === 'object' && !Object.isFrozen(obj[prop])) deepFreeze(obj[prop]);
    });
    return Object.freeze(obj);
  }
};
```

これで無事解決しました．

## Devtools を導入していない環境で確認してみる

なぜか Vue Devtools 拡張を導入していると遅くなる事象が発生するようです．

悩む前に一度シークレットモードなどで試してみたほうが良さそうです．

## 参考
<div class="bcard-wrapper"><span class="bcard-header withgfav"><div class="bcard-favicon" style="background-image: url(https://www.google.com/s2/favicons?domain=https://qiita.com/isuke/items/441c21e7f99e3a619803)"></div><div class="bcard-site"><a href="https://qiita.com/isuke/items/441c21e7f99e3a619803" rel="nofollow" target="_blank">Qiita</a></div><div class="bcard-url"><a href="https://qiita.com/isuke/items/441c21e7f99e3a619803" rel="nofollow" target="_blank">https://qiita.com/isuke/items/441c21e7f99e3a619803</a></div></span><span class="bcard-main withogimg"><div class="bcard-title"><a href="https://qiita.com/isuke/items/441c21e7f99e3a619803" rel="nofollow" target="_blank">Vue.jsで大きなObjectを扱うときはObject.freezeすると100倍くらい速くなるよ - Qiita</a></div><div class="bcard-description">タイトル通りなのでとりあえず結果を見てもらいましょう。


  See the Pen 
  EMNpVM by isuke (@isuke)
  on CodePen.




実行結果 



正確な測定ではないですが明らかな速...</div><a href="https://qiita.com/isuke/items/441c21e7f99e3a619803" rel="nofollow" target="_blank"><div class="bcard-img" style="background-image: url(https://qiita-user-contents.imgix.net/https%3A%2F%2Fcdn.qiita.com%2Fassets%2Fpublic%2Farticle-ogp-background-1150d8b18a7c15795b701a55ae908f94.png?ixlib=rb-1.2.2&w=1200&mark=https%3A%2F%2Fqiita-user-contents.imgix.net%2F~text%3Fixlib%3Drb-1.2.2%26w%3D840%26h%3D380%26txt%3DVue.js%25E3%2581%25A7%25E5%25A4%25A7%25E3%2581%258D%25E3%2581%25AAObject%25E3%2582%2592%25E6%2589%25B1%25E3%2581%2586%25E3%2581%25A8%25E3%2581%258D%25E3%2581%25AFObject.freeze%25E3%2581%2599%25E3%2582%258B%25E3%2581%25A8100%25E5%2580%258D%25E3%2581%258F%25E3%2582%2589%25E3%2581%2584%25E9%2580%259F%25E3%2581%258F%25E3%2581%25AA%25E3%2582%258B%25E3%2582%2588%26txt-color%3D%2523333%26txt-font%3DHiragino%2520Sans%2520W6%26txt-size%3D54%26txt-clip%3Dellipsis%26txt-align%3Dcenter%252Cmiddle%26s%3D43754f22b42bdd7798abb579e58abcba&mark-align=center%2Cmiddle&blend=https%3A%2F%2Fqiita-user-contents.imgix.net%2F~text%3Fixlib%3Drb-1.2.2%26w%3D840%26h%3D500%26txt%3D%2540isuke%26txt-color%3D%2523333%26txt-font%3DHiragino%2520Sans%2520W6%26txt-size%3D45%26txt-align%3Dright%252Cbottom%26s%3D07432a05c4e993be9d70f1e53c2620dc&blend-align=center%2Cmiddle&blend-mode=normal&s=9e20a9579f026ce2c01b00c658e19c2c)"></div></a></span></div>


<div class="bcard-wrapper"><span class="bcard-header withgfav"><div class="bcard-favicon" style="background-image: url(https://www.google.com/s2/favicons?domain=https://github.com/30-seconds/30-seconds-blog)"></div><div class="bcard-site"><a href="https://github.com/30-seconds/30-seconds-blog" rel="nofollow" target="_blank">GitHub</a></div><div class="bcard-url"><a href="https://github.com/30-seconds/30-seconds-blog" rel="nofollow" target="_blank">https://github.com/30-seconds/30-seconds-blog</a></div></span><span class="bcard-main withogimg"><div class="bcard-title"><a href="https://github.com/30-seconds/30-seconds-blog" rel="nofollow" target="_blank">30-seconds/30-seconds-blog</a></div><div class="bcard-description">The official 30-seconds blog. Contribute to 30-seconds/30-seconds-blog development by creating an account on GitHub.</div><a href="https://github.com/30-seconds/30-seconds-blog" rel="nofollow" target="_blank"><div class="bcard-img" style="background-image: url(https://avatars1.githubusercontent.com/u/43479428?s=400&v=4)"></div></a></span></div>