"""image_processing.pyのクラスを実行するファイル."""

from image_processing import ImageProcessing

import argparse
import os

# 保存ファイルのパス設定


def make_save_path(input_path: str, add_str: str):
    """保存ファイルのパス設定を行う関数
    Args:
        input_path(str):編集すファイルパス
        add_str(str):ファイル名に付け加える文字列
    """
    directory, filename = os.path.split(input_path)
    if directory != "":
        return os.path.join(directory, add_str + filename)
    else:
        return (add_str + filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="リアカメラに関するプログラム")
    parser.add_argument("--resize", nargs='+',
                        type=int, help='リサイズする画像サイズ(高さ, 幅)')
    parser.add_argument("-shape", "--sharpening",
                        action='store_true', help="画像の鮮明化")
    parser.add_argument("-f", "--file", type=str,
                        help="処理を行う画像or画像を格納したディレクトリパス")
    parser.add_argument("-sd", "--save_directory", type=str,
                        default="processed_image", help="リサイズする画像を保存するディレクトリのパス")
    args = parser.parse_args()

    if not args.file:
        print("画像もしくはディレクトリのパスを指定してください")
        exit(1)

    # 単体画像の処理
    elif args.file.endswith((".png", ".jpg")):
        print("指定ファイル:", args.file)

        # リサイズ
        if args.resize:
            args.resize *= 2 if len(args.resize) == 1 else 1
            print("画像を", args.resize, "にリサイズします。")

            save_path = make_save_path(args.file, "resized_")
            ImageProcessing.resize_img(
                args.file, save_path, args.resize[0], args.resize[1])

        # 鮮明化
        if args.sharpening:
            print("画像の鮮明化を行います。")
            save_path = make_save_path(args.file, "shaped_")
            ImageProcessing.sharpening(args.file, save_path)

    # ディレクトリ内の画像を処理
    else:
        print("指定ディレクトリ:", args.file)
        # リサイズ
        if args.resize:
            args.resize *= 2 if len(args.resize) == 1 else 1

            print("画像を", args.resize, "にリサイズします。")
            for image in os.listdir(args.file):
                if image.endswith((".png", ".jpg")):
                    input_image = os.path.join(args.file, image)
                    save_path = os.path.join(
                        "resized_"+args.file, make_save_path(image, "resized_"))
                    print("image:", image)
                    print("save_path:", save_path)
                    ImageProcessing.resize_img(
                        input_image, save_path, args.resize[0], args.resize[1])

        # 鮮明化
        if args.sharpening:
            print("画像の鮮明化を行います。")
            for image in os.listdir(args.file):
                if image.endswith((".png", ".jpg")):
                    input_image = os.path.join(args.file, image)
                    save_path = os.path.join(
                        "shaped_"+args.file, make_save_path(image, "shaped_"))
                    print("image:", image)
                    print("save_path:", save_path)
                    ImageProcessing.sharpening(input_image, save_path)

    print("完了")
