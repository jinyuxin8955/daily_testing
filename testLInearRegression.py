import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = 'ex1data1'
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])
data.head()

# print(data.head(), data.iloc[1]['Profit'])

data.plot(kind='scatter', x='Population', y='Profit', figsize=(12, 8))
plt.show()

data.insert(0, 'Ones', 1)        # 新增一列 x0

cols = data.shape[1]        # 计算列数
X = data.iloc[:, 0:cols-1]
Y = data.iloc[:, cols-1:cols]

X = np.matrix(X.values).A
Y = np.matrix(Y.values).A
# theta = np.matrix(np.array([0, 0]))

from sklearn import linear_model
model = linear_model.LinearRegression()
model.fit(X, Y)

x = np.array(X[:, 1])
y = model.predict(X).flatten()

fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(x, y, 'r', label='Prediction')
ax.scatter(data.Population, data.Profit, label='Training Data')
ax.legend(loc=2)
ax.set_xlabel('Population')
ax.set_ylabel('Profit')
ax.set_title('Predicted Profit vs. Population Size')
plt.show()


