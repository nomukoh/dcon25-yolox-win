# 自動車認識 YOLOX-s (Windows 開発用)

本プログラムは、 DCON2025 で自動車の認識を YOLOX-s で行うために使用したものです。

## 著作権表示および引用元

このリポジトリのコードは、[GitHubリポジトリ](https://github.com/Megvii-BaseDetection/YOLOX)から引用したものに変更を加えたものです。また、[zennの記事](https://zenn.dev/opamp/articles/d3878b189ea256)を参考に開発されています。  
引用元の著作権およびライセンス情報は各所有者に帰属します。  
このリポジトリは Apache License 2.0 の条件の下で配布されています。

## ※注意※
このリポジトリにはサブリポジトリが含まれているため、cloneしたあとに以下のコマンドを実行すること。もしくは、clone時にオプションをつけること。

```bash
git submodule init
git submodule update
```

```bash
git clone --recurse-submodules https://github.com/urbanecho-25/yolox-s-win.git
```

## 参考
https://zenn.dev/opamp/articles/d3878b189ea256

## 環境構築の手順

```bash
docker build -t yolox .
bash run_docker_container_notrm.sh
```

### 追加で入れたもの

```bash
apt-get update
apt-get install -y libgl1-mesa-dev
apt-get install -y libglib2.0-0
pip install loguru
pip install opencv-python
pip install psutil
pip install tensorboard
pip install pycocotools
pip install tqdm
pip install tabulate
pip install thop
```

## ハイパパラメータの定義ファイル

./yolox/exp/yolox_base.py  
./yolox_s.py（優先）

## クラスの名前を変更

./yolox/data/datasets/coco_classes.py

## trainデータ、valデータの配置

./datasets/dataset/annotations/train_annotations.json  
./datasets/dataset/annotations/val_annotations.json  
./datasets/dataset/train2017  
./datasets/dataset/val2017

## 学習

```bash
python3 train.py -f yolox_s.py -d 1 -b 16 --fp16 -o -c ./yolox_s.pth --cache
```

## 推論

```bash
python3 demo.py image -f yolox_s.py --device gpu --fp16 --path ./datasets/dataset/inference2017/[検査画像までのパス] -c ./YOLOX_outputs/yolox_s/best_ckpt.pth --save_result
```

## 親子関係

yolox-s-winリポジトリ内にあるYOLOX_jetsonフォルダは、yolox-s-jetsonリポジトリと同期されています。  
そして、yolox-s-winリポジトリのサブリポジトリとして設定されています。  
通常のリポジトリと同じように add, commit, push できます。

※親のリポジトリにも変更履歴が反映されるが、サブリポジトリ内でcommitされたところまでしか追えないので注意。
