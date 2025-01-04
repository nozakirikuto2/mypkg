# sin_publisher Node (ros2パッケージ)
![test](https://github.com/nozakirikuto2/robosys2024/actions/workflows/test.yml/badge.svg)

## トピック:countup

- このトピックに```sinpublisher```ノードは角度（```self.angle```）とそのsin値（```sin```）をメッセージとしてパブリッシュする。
- タイマー(create_timer)を使用して、0.5秒ごとに角度を１度ずつ増加させsin値を計算してパブリッシュする。
- トピックに関連付けられたメッセージの型は```std_msgs.msg.String```です。このメッセージには角度とsin値が含まれる。
- sub.pyはテスト用

## 概要

## ノード:sinpublisher



## 起動する手順

- gitをインストール
```bash
	sudo apt install git
```

- リポジトリをクローン
```bash
	git clone https://github.com/nozakirikuto2/mypkg.git
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
- © 2024 Rikuto Nozaki

## テスト環境

-  Ubuntu 22.04 LTS
