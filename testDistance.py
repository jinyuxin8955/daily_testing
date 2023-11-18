import numpy as np

x = [1, 2, 3, 4, 5]  # 一个 Python 列表
x_numpy = np.array(x)  # 将列表转换为 NumPy 数组

print(x_numpy)  # 输出 NumPy 数组

print(np.sum(x_numpy), np.sqrt(x_numpy))

def EuclideanDistance(x_vector, y_vector):
    x = np.array(x_vector)
    y = np.array(y_vector)
    return np.sqrt(np.sum(np.square(x-y)))

distance = EuclideanDistance(x, y_vector=[2, 3, 4, 5, 6])
print(distance)
