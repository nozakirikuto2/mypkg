# sin値を出す
![test](https://github.com/nozakirikuto2/robosys2024/actions/workflows/test.yml/badge.svg)

## 概要

- ros2で利用可能なパッケージです
- 角度が増加するたびにsin値を計算して、出力します
- 360度に達すると0度にリセットされます

## ノード説明
### sin_publisher

- 0度~360度までの角度のsin値を計算し、0.5秒間隔でデータを送信します
- 角度が360に達すると0度にリセットされる

## パブリッシュされるトピック

- countup
   - 角度とsin値をリアルタイムで送信。
   - 0.5秒ごとに新しいメッセージを送信。

## sub

テストを実行するために使用するノードです。受け取った角度とsin値を端末に表示します。


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
- このパッケージテストに利用したコンテナは下記のリンクのものを、本人の許可を得て使用しています。
   - [ryuichiueda/ubuntu22.04-ros2:latest](https://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2)
- © 2025 Rikuto Nozaki

## テスト環境

-  Ubuntu 22.04 LTS
