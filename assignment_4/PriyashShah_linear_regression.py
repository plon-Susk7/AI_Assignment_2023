import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"

columns = ['sex', 'length', 'diameter', 'height', 'wholeweight', 'shuckedweight', 'visceraweight', 'shellweight', 'rings']

df = pd.read_csv(url,names=columns)

X = df.drop('rings', axis=1)
y = df['rings']

X = pd.get_dummies(X, columns=['sex'], drop_first=True)

model = make_pipeline(PolynomialFeatures(2), LinearRegression())

model.fit(X, y)

y_pred= model.predict(X)
r2 = r2_score(y, y_pred)
print(f"Full dataset train and eval R2 score: {r2:.2f}")

def f(X, y):

    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5)

    model = make_pipeline(PolynomialFeatures(2), LinearRegression())

    model.fit(X_train, y_train)

    y_pred = model.predict(X_val)
    r2 = r2_score(y_val, y_pred)
    return r2

scores = [f(X, y) for _ in range(100)]
scores = np.array(scores)

mean_r2 = np.mean(scores)
std_r2 = np.std(scores)

print(f"70-15-15 Cross validation boxplot: mean={mean_r2:.2f}, std={std_r2:.2f}")