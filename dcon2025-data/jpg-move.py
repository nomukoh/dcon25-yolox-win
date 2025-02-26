import os
import shutil

def move_jpg_to_orijinal(directory):
    """
    指定されたディレクトリ内のJPG画像を./originalディレクトリに移動する。

    :param directory: JPG画像が格納されているディレクトリのパス
    """
    # 保存先ディレクトリを定義
    orijinal_dir = os.path.join(directory, "original")
    
    # 保存先ディレクトリを作成（存在しない場合）
    if not os.path.exists(orijinal_dir):
        os.makedirs(orijinal_dir)
        print(f"保存先ディレクトリを作成しました: {orijinal_dir}")
    
    # ディレクトリ内のファイルを取得
    files = os.listdir(directory)
    for file in files:
        # JPGファイルのみ処理
        if file.lower().endswith(".jpg") or file.lower().endswith(".jpeg"):
            try:
                # ファイルパスの生成
                file_path = os.path.join(directory, file)
                destination_path = os.path.join(orijinal_dir, file)
                
                # ファイルを移動
                shutil.move(file_path, destination_path)
                print(f"移動完了: {file} -> {orijinal_dir}")
            except Exception as e:
                print(f"エラーが発生しました ({file}): {e}")

# 使用例
if __name__ == "__main__":
    target_directory = input("JPG画像が格納されているディレクトリを指定してください: ")
    move_jpg_to_orijinal(target_directory)
