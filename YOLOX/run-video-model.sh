#!/bin/bash

# YOLOv5の実行コマンド
python3 ./tools/demo.py video -f yolox_s.py --device gpu --fp16 --path ./datasets/test.mp4 -c ./YOLOX_outputs/yolox_s/best_ckpt.pth --save_result

# 実行
echo "Running YOLOX-s..."
$PYTHON EXEC "$0" "$@"