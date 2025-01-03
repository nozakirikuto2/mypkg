# countup
![test](https://github.com/nozakirikuto2/robosys2024/actions/workflows/test.yml/badge.svg)

## 概要

度が増えていくたびにsin値の計算結果を送り続ける

## ノード:SinPublisher



## トピック:countup

- このトピックに```SinPublisher```ノードは角度（```self.angle```）とそのsin値（```sin```）をメッセージとしてパブリッシュする。
- タイマー(create_timer)を使用して、0.5秒ごとに角度を１度ずつ増加させsin値を計算してパブリッシュする。
- トピックに関連付けられたメッセージの型は```std_msgs.msg.String```です。このメッセージには角度とsin値が含まれる。

## 起動する手順

- リポジトリをクローン
```bash
	https://github.com/nozakirikuto2/mypkg.git
```

- mypkgに移動
```bash
	cd mypkg
```

## 実行方法

```bash
        ros2 run mypkg sin_publisher
```
・何も表示されないので起動させたままで別の端末を開く。
```bash
	ros2 topic echo /countup
```

## 必要なソフトウェア
- Python
	- テスト済みバージョン: 3.7~3.10

## ライセンス

- このソフトウェアパッケージは、3条項BSDライセンスの下、再分布および使用が許可されています。
        - テスト済みバージョン: 3.7~3.10
- © 2024 Rikuto Nozaki

## テスト環境

-  Ubuntu 22.04 LTS
