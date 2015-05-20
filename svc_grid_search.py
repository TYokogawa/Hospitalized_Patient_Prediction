#y_train = training set output
#y_test  = validation set output
#y_rtest = testing set output

from sklearn.svm import SVC
from sklearn import svm, grid_search
parameters = {'kernel':('linear', 'rbf'), 'C':[0.1, 1, 10, 100]}
svr = svm.SVC()
model = grid_search.GridSearchCV(svr, parameters)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_rpred = model.predict(X_rtest)


y_ans = y_test.copy()
y_predic = y_pred.copy()
y_rans = y_rtest.copy()
y_rpredic = y_rpred.copy()
from sklearn import metrics

print "val-accuracy:", metrics.accuracy_score(y_ans, y_predic)
print "val-precision:", metrics.precision_score(y_ans, y_predic, average='micro')
print "val-recall:", metrics.recall_score(y_ans, y_predic, average='micro')
print "val-f1 score:", metrics.f1_score(y_ans, y_predic, average='micro')
print   metrics.confusion_matrix(y_ans, y_predic)

print "accuracy:", metrics.accuracy_score(y_rans, y_rpredic)
print "precision:", metrics.precision_score(y_rans, y_rpredic, average='micro')
print "recall:", metrics.recall_score(y_rans, y_rpredic, average='micro')
print "f1 score:", metrics.f1_score(y_rans, y_rpredic, average='micro')
print   metrics.confusion_matrix(y_rans, y_rpredic)

