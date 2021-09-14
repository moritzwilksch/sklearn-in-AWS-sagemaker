create-s3-bucket:
	aws s3 mb s3://moritz-sklearn-sagemaker

sync-data:
	aws s3 cp data/titanic.csv s3://moritz-sklearn-sagemaker/titanic.csv
	
install:
	pip install -r requirements.txt
	
train:
	python3 code/training.py

download-data:
	aws s3 cp s3://moritz-sklearn-sagemaker/titanic.csv data/titanic.csv
	
build-image:
	docker build -t moritz-img .