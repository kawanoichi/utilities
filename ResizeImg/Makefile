help:
	@echo 一枚の画像をリサイズする
	@echo " $$ make Resize"
	@echo ディレクトリの中の画像をリサイズする
	@echo " $$ make Resizes"
	@echo resize_imageの削除
	@echo " $$ make rm"

Resize:
	python3 resize_img.py height(int) width(int) --file 画像パス
Resizes:
	python3 resize_img.py height(int) width(int) --directory ディレクトリパス

rm:
	rm -rf resize_image