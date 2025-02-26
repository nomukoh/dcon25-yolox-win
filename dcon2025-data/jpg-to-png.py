import os
from PIL import Image

def convert_jpg_to_png(directory):
    """
    指定されたディレクトリ内のJPG画像をPNG形式に変換する。

    :param directory: 画像ファイルが格納されているディレクトリのパス
    """
    if not os.path.exists(directory):
        print(f"指定されたディレクトリが見つかりません: {directory}")
        return

    # ディレクトリ内のファイルを取得
    files = os.listdir(directory)
    for file in files:
        # JPGファイルのみ処理
        if file.lower().endswith(".jpg") or file.lower().endswith(".jpeg"):
            try:
                # ファイルパスの生成
                file_path = os.path.join(directory, file)
                img = Image.open(file_path)
                
                # 新しいファイル名を生成（拡張子を変更）
                new_file_name = os.path.splitext(file)[0] + ".png"
                new_file_path = os.path.join(directory, new_file_name)
                
                # 画像をPNGとして保存
                img.save(new_file_path, "PNG")
                print(f"変換完了: {file} -> {new_file_name}")
            except Exception as e:
                print(f"エラーが発生しました ({file}): {e}")

# 使用例
if __name__ == "__main__":
    target_directory = input("JPG画像が格納されているディレクトリを指定してください: ")
    convert_jpg_to_png(target_directory)
