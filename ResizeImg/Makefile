help:
	@echo 一枚の画像をリサイズする
	@echo " $$ make Resize"
	@echo ディレクトリの中の画像をリサイズする
	@echo " $$ make Resizes"
	@echo resize_imageの削除
	@echo " $$ make rm"
	@echo テスト用
	@echo " $$ make test"

Resize:
	python3 resize_img.py height(int) width(int) --file 画像パス
Resizes:
	python3 resize_img.py height(int) width(int) --directory ディレクトリパス

test:
	python3 resize_img.py 50 60 --file test_img.png
	python3 resize_img.py 50 60 --file test_img.png --save_file resize_test_img.png
	python3 resize_img.py 50 60 --directory test_data 
	python3 resize_img.py 50 60 --directory test_data --save_directory resize_test_data
	rm -rf resize_image
	rm -rf resize_test_data

rm:
	rm -rf resize_image