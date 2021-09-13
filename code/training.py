import pandas as pd

df = pd.read_csv("s3://moritz-sklearn-sagemaker")
print(df.head())