"""画像をリサイズするモジュール.

author kawnaoichi

実行コマンド:
    # 一枚の画像を指定したサイズにリサイズ 
    $ python3 resize_img.py height(int) width(int) --file 画像パス
    # ディレクトリ内の複数枚画像を指定したサイズにリサイズ
    $ python3 resize_img.py height(int) width(int) --directory ディレクトリパス
"""
import cv2
import argparse
import os
import shutil
from tqdm import tqdm


def Resize(args):
    """一枚の画像をリサイズ."""
    # 保存パス
    save_path = "resize_" + args.file

    # 読み込み
    img = cv2.imread(args.file, cv2.IMREAD_UNCHANGED)
    height, width, _ = img.shape
    print("入力画像    :", "(", height, ",", width, ")")
    print("リサイズ画像:", "(", args.hsize, ",", args.wsize, ")")

    # リサイズ
    resize_img = cv2.resize(img, (args.wsize, args.hsize))
    cv2.imwrite(save_path, resize_img)


def Resizes(args):
    """ディレクトリ内の画像をリサイズ."""
    # 保存先ディレクトリがあったら作り直す
    save_dir = "resize_image"
    if os.path.exists(save_dir):
        shutil.rmtree(save_dir)
    os.mkdir(save_dir)

    pre_height, pre_width = 0, 0
    for filename in tqdm(os.listdir(args.directory), desc="Processing"):
        # 画像パス
        image_path = os.path.join(args.directory, filename)
        # 保存パス
        save_path = os.path.join(save_dir, filename)

        # 読み込み
        img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        height, width, _ = img.shape
        # 画像サイズの表示(前に参照した画像サイズと違う場合は表示)
        if (height, width) != (pre_height, pre_width):  # 一方でも違ければTrue
            print("入力画像    :", "(", height, ",", width, ")")
            print("リサイズ画像:", "(", args.hsize, ",", args.wsize, ")")
            pre_height, pre_width = height, width

        # リサイズ
        resize_img = cv2.resize(img, (args.wsize, args.hsize))
        cv2.imwrite(save_path, resize_img)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="リアカメラに関するプログラム")
    parser.add_argument("hsize", type=int, help="リサイズする画像サイズ(Height)")
    parser.add_argument("wsize", type=int, help="リサイズする画像サイズ(Width)")
    parser.add_argument("-f", "--file", type=str,
                        default=None, help="リサイズする画像パス")
    parser.add_argument("-d", "--directory", type=str,
                        default=None, help="リサイズする画像のあるディレクトリのパス")
    args = parser.parse_args()

    if args.file is not None:
        Resize(args)

    if args.directory is not None:
        Resizes(args)

    print("Resize Finish!!")
