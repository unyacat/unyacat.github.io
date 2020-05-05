---
title: Google Colab で学習済みモデルを利用して無限にアニメ顔を生成して幸せになろう
date: 2020-05-05 21:39:21
---



Google Colab 上で StyleGAN2 を動かし [This Waifu Does Not Exist](https://www.thiswaifudoesnotexist.net/) で利用されているモデルを借りてアニメ顔を生成させます．

自前で動かすことでパラメータの調整が可能になり満足行くまで何枚でも生成できます．

<!--more-->

## 準備

モデルを用意します．学習済みモデルのダウンロードは[こちら](https://mega.nz/file/PeIi2ayb#xoRtjTXyXuvgDxSsSMn-cOh-Zux9493zqdxwVMaAzp4)

7-ZIP等を利用し解凍した上で Google Drive の適当な場所にアップロードします．



## 実行

Google Colab に 上げておいたのでこれを実行すれば試すことができます．

下記 URL にアクセスして Playground モードにし ドライブにコピー してからランタイム > すべてのセルを実行．

https://colab.research.google.com/drive/1GeKHArMzxBiBNNp_Kk-W-y7tnIay_Op9

序盤に Drive へのアクセス権を求められます．URLに飛んでログインし，枠にコード貼り付けて Enter すれば許可されます．

### truncation-psi

truncation-psi オプションを変更することで平均に近い顔を求めたりぶっとんだ画像を求めたりすることができます．負の値も取れます．[参考](https://www.gwern.net/Faces#psitruncation-trick)

0 にすると平均の顔が出てきます．

![truncation-psi=0](https://lh3.googleusercontent.com/wmc79kQtuSgGjKChT0N0_7m7583VVlJneZq25qljbZ4mwduJZQrtlgEQqz0hGpG44ms3_Lu11Ko-5OTP0bYX-cY1trnv0xFY5_ad_z-dZuzSY9BNVnZOR5ojTMs-KF3e73GIK8NJXsA=w2400)

かわいい．茶眼茶髪の女子高生．

#### 0.1

まだ面影があります．

![truncation-psi=0.1](https://lh3.googleusercontent.com/sFCIXflsCFDtqHPqUj_G5gT2zxMUXFxC2J-Rs3fWiEb48BiFlngst6cuFJJwVhNfqGwKc3Xl54GbVBLbfuDFheZqDiN9Kt5bIAFKsQtTBG8Si63MBVEFJABWhMbShv9UGWx0n-K6Xn4=w2400)

#### 0.3

面影はあるものの別のキャラと言えそうです．

![truncation-psi=0.3](https://lh3.googleusercontent.com/OJNSPXbSMRCofd7iuS8QI0I5uWR_Dlndwhq9ZtkHRH5P7m46Dtx_U74MQpxMBsx4KqhGYJDyJfPAGx3SJVT-LOTFvz_F4PGvMtwEShOOJVyuZyIMJCayAtPy5mkZgg8xw7_p6RNJ930=w2400)

#### 0.5

キャラが区別できる上に安定していますね．

![truncation-psi=0.5](https://lh3.googleusercontent.com/Bl1gKSo8KllL0Dl6t2j_OxPEyK7I31jH_tENt6KjHvyweEJ3xv7lEiQJzc1YD368PkUVSerGnsRfET0ZRFYaZC5QOPN2n3DbtEZQ0d9QfK0yVTxNCOfn_CW9ywsedONaSf_J-lEcX9A=w2400)

#### 0.7

サイトに上がっている設定． 

![truncation-psi=0.7](https://lh3.googleusercontent.com/Y1z8xIPIVsy8D4KLMdSkct6a7PlvkzswuJ3tgeKhDRy90T4lzC9qizcvuMVzZgITWyeWU1Ecw7SNB_Mem7qMJRnDrPEjbYxqTquayCBJnWb8nsgQ_jpTzux-tlENfudwkJzyMhUyptg=w2400)

#### 1.0

![truncation-psi=1](https://lh3.googleusercontent.com/jk11Vaab8JbXnlmokCF-T5fN006omYe-I0qvrmmv4U4v1uI5o2dPksI3qBpZb2yhIAtp8FSLOLtz2mAkbgbQ493PXwAoifnse5nduAg-bnJwnFR26bWGHF4vJTA6rTEaaAHySx707t0=w2400)

#### 1.2

良くも悪くも興味深い攻めた設定

![truncation-psi=1.2](https://lh3.googleusercontent.com/xOl3g8uCsHJO0uOsnf9mloUgIpgzR4ZxkploDOADeXgKJ_p4t8rrXUQQj54JbFBMDMXlfAvvB056_xu7wv88srLCUnIHkSIZwXATC6yVxN3B32VSuSQdbrNVuQVb8juOWqRHqH_kMB8=w2400)

#### 10

概念が生まれます．

![truncation-psi=10](https://lh3.googleusercontent.com/hrdlYgDQjhiaK5DF7Z6NunoN-GSvKzrjBoP2suiJmCRvGMw-ikrD-QHNZqzIDgUUwubRv5BCrJezeh2-HQn7NaBQcjjrIa8LMgDGs1kCDoiAAkmK3cmy02AdqAUN3WCB287eBKD2zK4=w2400)

## 著作権等

すべての生成画像はパブリックドメイン(CC-0)のようです．[参考](https://www.gwern.net/TWDNE#copyright)



