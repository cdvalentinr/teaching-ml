import pandas as pd

x = pd.read_csv("datasets/Guangren_table34.txt")
x.info()

# Linear regression (finding best fit model)
b = 2
x = pd.Series([0, 1, 2])
y = pd.Series([0.1, 0.9, 4.1]) + b
m = -b * (x.sum() / (y**2).sum())

import matplotlib.pyplot as plt
import seaborn as sns
iris = sns.load_dataset('iris')
iris.plot(kind = 'scatter', x = 'petal_length', y = 'petal_width')
# sns.pairplot(iris)
plt.show()

import numpy as np
from sklearn import linear_model
model = linear_model.LinearRegression()
model.fit(np.c_[iris.petal_length], iris.petal_width.values)
t0, t1 = model.intercept_, model.coef_[0]
t0, t1
iris.plot(kind='scatter', x = 'petal_length', y = 'petal_width')
X=np.linspace(1, 7, num=7)
plt.plot(X, t0 + t1*X, "b")
plt.show()