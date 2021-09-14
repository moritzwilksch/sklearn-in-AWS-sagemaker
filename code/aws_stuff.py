import sagemaker
from sagemaker.sklearn import SKLearn

role = sagemaker.get_execution_role()

print(role)




print(role)

sklearn_estimator = SKLearn('code/training.py',
                            role='SageMakerRole',
                            instance_type='ml.m4.xlarge',
                            framework_version='0.23-1',
                            hyperparameters = None)
sklearn_estimator.fit({'train': 's3://moritz-sklearn-sagemaker/titanic.csv',
                        'test': 's3://moritz-sklearn-sagemaker/titanic.csv'})