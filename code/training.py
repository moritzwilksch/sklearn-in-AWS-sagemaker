import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("data/titanic.csv")


def drop_useless(data: pd.DataFrame) -> pd.DataFrame:
    data = data["Survived Pclass Sex Age SibSp Parch Fare Embarked".split()]
    data.columns = [c.lower() for c in data.columns]
    return data


def fix(data: pd.DataFrame) -> pd.DataFrame:
    catcols = "embarked sex".split()
    data[catcols] = data[catcols].astype("category")
    
    data["sex"] = data["sex"].cat.codes
    data["embarked"] = data["embarked"].cat.codes

    data['age'] = data["age"].fillna(data.age.mean())
    data['embarked'] = data["embarked"].fillna(data.embarked.mode())
    return data


clean = df.copy().pipe(drop_useless).pipe(fix)

lr = LogisticRegression(max_iter=250)
lr.fit(clean.drop('survived', axis=1), clean.survived)

print("Done with model fitting!")

joblib.dump(lr, "data/lr_model.joblib")
print("Saved model!")