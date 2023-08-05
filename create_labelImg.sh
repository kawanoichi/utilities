# 参考: Yolov5をカスタムデータで学習させる(Python) https://onl.bz/CLXM6VU
git clone -b v1.8.6 https://github.com/heartexlabs/labelImg.git
pip3 install pyqt5 lxml
cd labelImg
pyrcc5 -o libs/resources.py resources.qrc