
import pickle
with open('diabetes_newdiag_data3.pkl', 'r') as f:
    df = pickle.load(f)


#Replace 'y's with 1s, 'n's with 0s.
d = {'Yes': 1, 'Ch': 1, 'No': 0, 'NO': 0, '>30': 1, '<30': 2, '?': None}
df = df.replace(d)


#Create training set and test set
import numpy as np
rows = np.random.choice(df.index.values, 50883)
df_training = df.ix[rows]
df_testset = df.drop(rows)



race_dummies = pd.get_dummies(dt.race, prefix='Race').iloc[:, 1:]
gender_dummies = pd.get_dummies(dt.gender, prefix='gender').iloc[:, 1:]
payer_code_dummies = pd.get_dummies(dt.payer_code, prefix='payer_code').iloc[:, 1:]
diag1_dummies = pd.get_dummies(dt.diag1, prefix='diag1').iloc[:, 1:]
diag2_dummies = pd.get_dummies(dt.diag2, prefix='diag2').iloc[:, 1:]
diag3_dummies = pd.get_dummies(dt.diag3, prefix='diag3').iloc[:, 1:]
max_glu_serum_dummies = pd.get_dummies(dt.max_glu_serum, prefix='max_glu_serum').iloc[:, 1:]
A1Cresult_dummies = pd.get_dummies(dt.A1Cresult, prefix='A1Cresult').iloc[:, 1:]
insulin_dummies = pd.get_dummies(dt.insulin, prefix='insulin').iloc[:, 1:]
data = pd.concat([dt, race_dummies, gender_dummies,payer_code_dummies,diag1_dummies, diag2_dummies,diag3_dummies, max_glu_serum_dummies, A1Cresult_dummies, insulin_dummies, diag1_dummies], axis=1)


data = data.drop('race', 1)
data = data.drop('gender', 1)
data = data.drop('payer_code', 1)
data = data.drop('diag1', 1)
data = data.drop('diag2', 1)
data = data.drop('diag3', 1)
data = data.drop('max_glu_serum', 1)
data = data.drop('A1Cresult', 1)
data = data.drop('insulin', 1)


from sklearn.cross_validation import train_test_split
y = data.iloc[:,12:13]
X = data.drop('readmitted', 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

print len(y_train)
print len(X_train)
print len(y_test)
print len(X_test)
