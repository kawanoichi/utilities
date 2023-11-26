help:
	@echo 画像をリサイズする
	@echo " $$ make shapeing"
	@echo ディレクトリ内の画像をリサイズする
	@echo " $$ make shapeings"
	@echo 画像を鮮明化する
	@echo " $$ make resize"
	@echo ディレクトリ内の画像を鮮明化する
	@echo " $$ make resizes"
	@echo 出力データの削除
	@echo " $$ make rm"
	@echo エラーが発生しないかの確認
	@echo " $$ make test"


test:
	make resize
	make resizes
	make shapeing
	make shapeings
	make rm
	@echo make all is complite!!

resize:
	python work_image_processing.py --file test_image.png --resize 640

resizes:
	python work_image_processing.py --file test_dir --resize 640

shapeing:
	python work_image_processing.py --file test_image.png -shape 

shapeings:
	python work_image_processing.py --file test_dir -shape

rm:
	rm -rf resized_test_dir shaped_test_dir resized_test_image.png shaped_test_image.png

coodinate:
	python search_coodinate.py