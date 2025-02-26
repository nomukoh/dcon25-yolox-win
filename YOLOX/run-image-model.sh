#!/bin/bash

# YOLOv5の実行コマンド
python3 ./tools/demo.py image -f yolox_s.py --device gpu --fp16 --path ./datasets/dataset/inference2017/test.jpg -c ./YOLOX_outputs/yolox_s/best_ckpt.pth --save_result

# 実行
echo "Running YOLOX-s..."