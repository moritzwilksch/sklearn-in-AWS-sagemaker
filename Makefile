create-s3-bucket:
	aws s3 mb s3://moritz-sklearn-sagemaker

sync-data:
	aws s3 cp data/titanic.csv s3://moritz-sklearn-sagemaker/titanic.csv
	
install:
	pip install -r requirements.txt