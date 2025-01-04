# countup (ros2パッケージ)
![test](https://github.com/nozakirikuto2/robosys2024/actions/workflows/test.yml/badge.svg)

## 概要

このプログラムはros2のパッケージとして作成されており、角度が増加するたびにsin値をだしてトピック```countup```に送信する機能を持つノード```sinpublisher```を実装しています。
sub.pyはテスト用として用いています。

## ノード:sinpublisher

- 0度~360度までの角度のsin値を計算し、0.5秒間隔でデータを送信します。
- 角度が360に達すると0度にリセットされる。

## トピック:countup

- 角度とsin値をリアルタイムで送信。
- 0.5秒ごとに新しいメッセージを送信。

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
