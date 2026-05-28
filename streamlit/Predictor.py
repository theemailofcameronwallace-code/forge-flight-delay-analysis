import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

predictor = pd.read_csv("Delay_predictor.csv")

predictor["Delayed"] = (predictor["ARRIVAL_DELAY"] > 5).astype(int)

df_encoded = pd.get_dummies(predictor, columns=['AIRLINE'])
x = predictor = pd.read_csv("Delay_predictor.csv")

predictor["Delayed"] = (predictor["ARRIVAL_DELAY"] > 5).astype(int)

df_encoded = pd.get_dummies(predictor, columns=['AIRLINE'])
x = df_encoded.drop(columns=["ARRIVAL_DELAY", "Delayed"])

y = df_encoded['Delayed']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=42)