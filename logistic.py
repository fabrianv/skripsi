#logistic accuracy+f1score
from re import X
from sklearn.datasets import make_classification
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn import ensemble
import pandas as pd
import numpy as np
import math
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
# import seaborn as sns

phish_data = pd.read_csv("dataset.csv")

print(phish_data.head(150))

# sns.countplot(x="Phishing", data=phish_data)


X=phish_data.drop("Phishing",axis=1)
y=phish_data["Phishing"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2)

### LOGISTIC REGRESSION ####
# logmodel=LogisticRegression()
# logmodel.fit(X_train, y_train)

# prediction = logmodel.predict(X_test)

## SVM ####
# classifier = svm.SVC(kernel="linear", gamma="auto", C=2)
# classifier.fit(X_train, y_train)

# prediction = classifier.predict(X_test)


#### Random Forest ####
classifier = ensemble.RandomForestClassifier(n_estimators=100)
classifier.fit(X_train, y_train)

prediction = classifier.predict(X_test)

#### NAIVE BAYES ####
# classifier = GaussianNB()
# classifier.fit(X_train, y_train)

# prediction = classifier.predict(X_test)

print(classification_report(y_test,prediction))
# print(accuracy_score(y_test,prediction))
print('confusion matrix = ')
print(confusion_matrix(y_test,prediction))
# print(f1_score(y_test, prediction,average='micro'))
matrix = plot_confusion_matrix(classifier, X_test, y_test, cmap=plt.cm.Reds)
matrix.ax_.set_title("Confusion Matrix", color ="Black")
plt.xlabel('Predicted Label', color="Black")
plt.ylabel('Actual Label', color="Black")
# plt.gcf().axes[0],tick_params(colors='white')
# plt.gcf().axes[1],tick_params(colors='white')
print(plt.show())

# FP = confusion_matrix.sum(axis=0) - np.diag(confusion_matrix)
# FN = confusion_matrix.sum(axis=1) - np.diag(confusion_matrix)
# TP = np.diag(confusion_matrix)
# TN = confusion_matrix.values.sum() - (FP + FN +TP)

# TPR = TP/(TP+FN)
# TNR = TN/(TN+FP)
# FPR = FP/(FP+TN)
# FNR = FN/(TP+FN)

# ACC = (TP+TN)/(TP+FP+FN+TN)

# print("false positive = " +str(FP))
# print("false negative = " +str(FN))
# print("true positive = " + str(TP))
# print("true negative = " + str(TN))
# print("TPR = " +str(TPR))
# print("FPR = " + str(FPR))
# print("accuracy = " + str(ACC))


# x, y = make_classification(
#     n_samples=100,
#     n_features=12,
#     n_classes=2,
#     n_clusters_per_class=1,
#     flip_y=0.03,
#     n_informative=1,
#     n_redundant=0,
#     n_repeated=0
# )

# print(y)