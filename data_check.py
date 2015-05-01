import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.DataFrame.from_csv('dataset_diabetes/diabetic_data.csv', header=0)


## check dataframe

df.columns

df.shape

df.dia

df.describe()





## finding NAN position

inds = pd.isnull(df).any(1).nonzero()[0]


test2 = df[df['admission_type_id'] != '?']
test2.shape


## convert diagnosis_1 (string to float)

diagno = df.iloc[:,17]
ddiagno = diagno.convert_objects(convert_numeric=True)


## histogram

ddiagno.plot(kind='hist', alpha=0.5, bins = 20)

