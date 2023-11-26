import tkinter as tk
from PIL import Image, ImageTk
import os


def get_pixel_value(image, x, y):
    # 画像の(x, y)座標のピクセル値を取得
    pixel = image.getpixel((x, y))
    # RGBを平均して輝度値を計算
    brightness = sum(pixel) / len(pixel)
    return brightness


def on_click(event):
    # クリックされた座標を取得
    x, y = event.x, event.y
    # 輝度値を取得
    brightness = get_pixel_value(image, x, y)
    # 座標と輝度値を表示
    result_label.config(text=f"座標: ({x}, {y}), 輝度値: {brightness:.2f}")


if __name__ == "__main__":
    # 保存用フォルダの作成
    current_dir_path = os.path.dirname(os.path.abspath(__file__))
    print("current_dir_path", current_dir_path)
    folder_path = os.path.join(current_dir_path, "image_data")
    print("folder_path", folder_path)

    image_name = "test.png"
    image_path = os.path.join(folder_path, image_name)
    # save_path = os.path.join(folder_path, "changed_"+image_name)

    if not os.path.exists(image_path):
        print("画像がありません")
        print("image_path:", image_path)
        exit()

    # 画像の読み込み
    image = Image.open(image_path)

    # GUIウィンドウの作成
    root = tk.Tk()
    root.title("Image Click Analyzer")

    # 画像を表示するキャンバス
    canvas = tk.Canvas(root, width=image.width, height=image.height)
    canvas.pack()
    tk_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

    # クリックした座標と輝度値を表示するラベル
    result_label = tk.Label(root, text="クリックしてください")
    result_label.pack()

    # クリックイベントのバインド
    canvas.bind("<Button-1>", on_click)

    # GUIループの開始
    root.mainloop()

    print("完了！")
