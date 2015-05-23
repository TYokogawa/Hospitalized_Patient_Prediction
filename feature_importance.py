## Feature importance

from sklearn.ensemble import ExtraTreesClassifier

# Build a forest and compute the feature importances
forest = ExtraTreesClassifier(n_estimators=500, random_state=0)
forest.fit(X_train, y_train)
importances = forest.feature_importances_

importances = pd.DataFrame(importances)
importances.sort_index(by=[0], ascending=[False])


for f in range(len(importances)):
    feature = X_train.columns[f]
    print( "%d: "  % (f+1)+ feature + ": " + str(importances[f]))