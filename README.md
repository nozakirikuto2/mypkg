
- トピック```countup```をパブリッシュするノード
- タイマー(create_timer)を使用して、0.5秒ごとに角度を１度ずつ増加させsin値を計算してパブリッシュする。

## サブスクライブされるトピック

- トピック```countup```をサブスクライブし、受信したデータをログに出力する。

## 起動する手順

- リポジトリをクローン
```bash

```

- launchに移動
```bash
        cd launch
```

## 実行方法

```bash
        ros2 launch mypkg talk_listen.launch.py
```

## 必要なソフトウェア
- Python
        - テスト済みバージョン: 3.7~3.10

## ライセンス

- このソフトウェアパッケージは、３条項BSDライセンスの下、再分布および使用が>許可されています。
- © 2024 Rikuto Nozaki

## テスト環境

-  Ubuntu 22.04 LT
