import cv2
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
# from typing import List, Tuple


class CameraCoordinateCalibrator:
    """カメラ画像から座標とHSV値を取得するクラス."""

    def __init__(self, img_path: str) -> None:
        """CameraCoordinateCalibratorのコンストラクタ.

        Args:
            img (cv2.Mat): 画像データ
        """
        # メンバを初期化する
        self.img = cv2.imread(img_path)
        self.img_height = self.img.shape[0]  # 画像の高さ
        self.img_width = self.img.shape[1]  # 画像の横幅

    def __set_coordinate(self, event) -> None:
        """マウス操作で取得した座標を各座標リストにセットするコールバック関数.

        Args:
            event: マウスイベント
        """
        hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        point_hsv = hsv[event.y, event.x]

        self.__message["text"] += "座標:(%d,%d)\nHSV[%d,%d,%d]\n\n"\
            % (event.x, event.y, point_hsv[0], point_hsv[1], point_hsv[2])

    def __complete_input_coordinate(self, event) -> None:
        """OKボタンで画面を閉じるためのコールバック関数.

        Args:
            event: マウスイベント(引数に記述する必要あり)
        """
        # ウィンドウを閉じる
        self.__window.destroy()

    def __reset_previous_coordinate(self, event) -> None:
        """リセットのコールバック関数.

        Args:
            event: マウスイベント(引数に記述する必要あり)
        """
        self.__message["text"] = []

    def show_window(self) -> None:
        """画像取得ツールを起動する関数."""
        # ウィンドウを定義する
        self.__window = tk.Tk()
        self.__window.title("Camera Coordinate Calibrator")
        # ウィンドウサイズ: (画像の横幅 + UIの横幅) x 画像の高さ
        self.__window.geometry(f"{self.img_width+400}x{self.img_height}")

        # 取得状況を表示するMessageを定義する
        self.__message = tk.Message(
            self.__window, text="", font=("", 10), bg="#ddd", aspect=500)
        # Messageを配置する
        self.__message.place(x=self.img_width+10, y=150, width=180)

        # OpenCVで取得した画像を変換する
        img_rgb = cv2.cvtColor(self.img,
                               cv2.COLOR_BGR2RGB)  # imreadはBGRなのでRGBに変換
        img_pil = Image.fromarray(img_rgb)    # RGBからPILフォーマットへ変換
        img_tk = ImageTk.PhotoImage(img_pil)  # ImageTkフォーマットへ変換

        # ウィジェットを定義する
        # 画像を表示するCanvasを定義する
        canvas = tk.Canvas(self.__window, width=self.img_width,
                           height=self.img_height)
        # コールバック関数を指定する ("<Button-1>"は左クリックボタン)
        canvas.bind("<Button-1>", self.__set_coordinate)
        # Canvasを配置する
        canvas.pack(side=tk.LEFT)
        # Canvasに画像を設置する
        canvas.create_image(0, 0, image=img_tk, anchor=tk.NW)

        # Reset
        reset_prev_button = tk.Button(self.__window, text="Reset Prev")
        # コールバック関数を指定する ("<Button-1>"は左クリックボタン)
        reset_prev_button.bind("<Button-1>", self.__reset_previous_coordinate)
        # 直前の操作を取り消すButtonを配置する
        reset_prev_button.place(x=self.img_width+10,
                                y=80, width=180, height=50)

        # OK用のButtonを定義する
        ok_button = tk.Button(self.__window, text="OK")
        # コールバック関数を指定する ("<Button-1>"は左クリックボタン)
        ok_button.bind("<Button-1>", self.__complete_input_coordinate)
        # OKボタンを配置する
        ok_button.place(x=self.img_width+10, y=20, width=180, height=50)

        # ウィンドウを表示する
        self.__window.mainloop()


if __name__ == "__main__":
    img_path = "image_data/test.png"
    coord = CameraCoordinateCalibrator(img_path)
    coord.show_window()
