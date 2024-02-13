import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

glass =pd.read_csv ('glass.csv')

X = glass.iloc[:, :-1]
y = glass.iloc[:, -1]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

nb_classifier = GaussianNB()
nb_classifier.fit(X_train, y_train)

y_pred = nb_classifier.predict(X_test)

accuracy = nb_classifier.score(X_test, y_test)
classification_rep =  classification_report(y_test, y_pred, target_names=[f"Class {i}" for i in range(1,7)])
print("Accuracy:", accuracy)
print("\nClassification Report:\n", classification_rep)