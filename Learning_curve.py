## Learning curve (number of training examples)

from sklearn.learning_curve import learning_curve

from sklearn.naive_bayes import GaussianNB
nbmodel = GaussianNB()

from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier()

from sklearn.naive_bayes import MultinomialNB
mnb = MultinomialNB()

from sklearn.svm import SVC
svmodel = SVC()

from sklearn.ensemble import GradientBoostingClassifier
gbm = GradientBoostingClassifier(learning_rate=0.4, n_estimators=100)

from sklearn.ensemble import RandomForestClassifier
rfo = RandomForestClassifier(n_estimators=100)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=9)

plot_learning_curve(nbmodel, "Gaussian Naive Bayes", X_train, y_train, cv=5)
plot_learning_curve(dtree, "Decision Tree", X_train, y_train, cv=5)
plot_learning_curve(mnb, "Multinomial Naive Bayes", X_train, y_train, cv=5)
plot_learning_curve(svmodel, "Support_vector_machine", X_train, y_train, cv=5)
plot_learning_curve(gbm, "Gradient_Boosting", X_train, y_train, cv=5)
plot_learning_curve(rfo, "Random_Forest", X_train, y_train, cv=5)
plot_learning_curve(neigh, "k-neighbors", X_train, y_train, cv=5)
plot_learning_curve(model, "logistic regression", X_train, y_train, cv=5)

plt.show()