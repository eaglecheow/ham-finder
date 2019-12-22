import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm

from sklearn.preprocessing import LabelEncoder, StandardScaler

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

dataset = pd.read_csv(".\\dataset\\iris\\iris.csv")
dataset.head()

feature_columns = ["sepal-length", "sepal-width", "petal-length", "petal-width"]
X = dataset[feature_columns].values
Y = dataset["species"].values

le = LabelEncoder()
Y = le.fit_transform(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20)

scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

SVM =svm.LinearSVC()
SVM.fit(X_train, Y_train)
y_pred = SVM.predict(X_test)

print(confusion_matrix(Y_test, y_pred.round()))
print(classification_report(Y_test, y_pred.round()))
print(accuracy_score(Y_test, y_pred.round()))