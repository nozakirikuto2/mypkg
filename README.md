# 角度からsin値の計算結果をだす
![test](https://github.com/nozakirikuto2/robosys2024/actions/workflows/test.yml/badge.svg)

## 概要

- ros2で利用可能なパッケージです
- 角度が増加するたびにsin値を計算して、出力します
- 360度に達すると0度にリセットされます

## ノードについて
### sin_publisher

- 0度~360度までの角度をsin値で計算し、0.5秒間隔で角度とsin値の計算結果のデータを送信します

### パブリッシュされるトピック

- countup
   - 角度とsin値をリアルタイムで送信

### sub

テスト用に使用するノードです。受け取った角度とsin値を端末に表示します。

## 必要なソフトウェア

- Python
   - テスト済みバージョン: 3.7~3.10

## ライセンス

- このソフトウェアパッケージは、3条項BSDライセンスの下、再分布および使用が許可されています。
- このパッケージのテストに利用したコンテナは本人の許可を得て使用しています。
以下が使用したリンクです。
   - [ryuichiueda/ubuntu22.04-ros2:latest](https://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2)
- © 2025 Rikuto Nozaki

## テスト環境

-  Ubuntu 22.04 LTS
