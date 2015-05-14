
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from patsy import dmatrices
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score


## dummy vairables

race_dummies = pd.get_dummies(dt.race, prefix='Race').iloc[:, 1:]
gender_dummies = pd.get_dummies(dt.gender, prefix='gender').iloc[:, 1:]
admission_dummies = pd.get_dummies(dt.admission, prefix='admission').iloc[:, 1:]
discharge_dummies = pd.get_dummies(dt.discharge, prefix='discharge').iloc[:, 1:]
admsource_dummies = pd.get_dummies(dt.admsource, prefix='admsource').iloc[:, 1:]
payer_code_dummies = pd.get_dummies(dt.payer_code, prefix='payer_code').iloc[:, 1:]
diag1_dummies = pd.get_dummies(dt.diag1, prefix='diag1').iloc[:, 1:]
diag2_dummies = pd.get_dummies(dt.diag2, prefix='diag2').iloc[:, 1:]
diag3_dummies = pd.get_dummies(dt.diag3, prefix='diag3').iloc[:, 1:]
max_glu_serum_dummies = pd.get_dummies(dt.max_glu_serum, prefix='max_glu_serum').iloc[:, 1:]
A1Cresult_dummies = pd.get_dummies(dt.A1Cresult, prefix='A1Cresult').iloc[:, 1:]
insulin_dummies = pd.get_dummies(dt.insulin, prefix='insulin').iloc[:, 1:]


data = pd.concat([dt, race_dummies, gender_dummies, admission_dummies, admsource_dummies, payer_code_dummies,diag1_dummies, diag2_dummies,diag3_dummies, max_glu_serum_dummies, A1Cresult_dummies, insulin_dummies], axis=1)


data = data.drop('race', 1)
data = data.drop('gender', 1)
data = data.drop('payer_code', 1)
data = data.drop('diag1', 1)
data = data.drop('diag2', 1)
data = data.drop('diag3', 1)
data = data.drop('max_glu_serum', 1)
data = data.drop('A1Cresult', 1)
data = data.drop('insulin', 1)
data = data.drop('admission', 1)
data = data.drop('discharge', 1)
data = data.drop('admsource', 1)


## generate training and test data set

from sklearn.cross_validation import train_test_split
y = data.iloc[:,11:12]
X = data.drop('readmitted', 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)



## Machine learning basic settings

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors= 10)
model = model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_rpred = model.predict(X_rtest)


from sklearn.linear_model import LogisticRegression
modell = LogisticRegression(penalty='l1')
modell = modell.fit(X_train, y_train)
y_pred = modell.predict(X_test)
y_rpred = model.predict(X_rtest)


from sklearn.linear_model import LogisticRegression
modell = LogisticRegression(penalty='l2', C=0.1)
modell = modell.fit(X_train, y_train)
y_pred = modell.predict(X_test)
y_rpred = model.predict(X_rtest)


from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model = model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_rpred = model.predict(X_rtest)


from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model = model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_rpred = model.predict(X_rtest)


from sklearn.svm import SVC
model = SVC()
model = model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_rpred = model.predict(X_rtest)


from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100)
model = model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_rpred = model.predict(X_rtest)


from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier(learning_rate=0.04, n_estimators=100)
model = model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_rpred = model.predict(X_rtest)



## test model on testing data set

y_ans = y_test.copy()
y_predic = y_pred.copy()
y_rans = y_rtest.copy()
y_rpredic = y_rpred.copy()
from sklearn import metrics

print "accuracy:", metrics.accuracy_score(y_ans, y_predic)
print "precision:", metrics.precision_score(y_ans, y_predic, average='micro')
print "recall:", metrics.recall_score(y_ans, y_predic, average='micro')
print "f1 score:", metrics.f1_score(y_ans, y_predic, average='micro')
print   metrics.confusion_matrix(y_ans, y_predic)


