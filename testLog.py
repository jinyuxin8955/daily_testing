import matplotlib.pyplot as plt

accuracies = [0.45, 0.90, 0.85, 0.88, 0.92, 0.91, 0.89, 0.93, 0.94, 0.95]

with open('accuracy_log', 'w') as file:
    for accuracy in accuracies:
        file.write(f'{accuracy}\n')

with open('accuracy_log', 'r') as file:
    accuracies = [float(line.strip()) for line in file]

epochs = list(range(1, len(accuracies)+1))

plt.plot(epochs, accuracies, linestyle='-')
plt.title("Accuracy Curve")
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.grid(True)
plt.show()


import matplotlib.pyplot as plt

# 生成两列示例数据
data = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 10)]

# 将数据写入文本文件
with open('datum', 'w') as file:
    for x, y in data:
        file.write(f'{x} {y}\n')

# 从文本文件中读取两列数据
x_values = []
y_values = []

with open('datum', 'r') as file:
    for line in file:
        x, y = map(float, line.strip().split())
        x_values.append(x)
        y_values.append(y)

# 绘制折线图
plt.plot(x_values, y_values, marker='o', linestyle='-')
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

accuracies = [0.45, 0.90, 0.85, 0.88, 0.92, 0.91, 0.89, 0.93, 0.94, 0.95]

with open('accuracy_logs', 'w') as file:
    i = 0
    for accuracy in accuracies:
        i += 1
        file.write(f'{i} {accuracy}\n')

# 从文本文件中读取两列数据
x_values = []
y_values = []

with open('accuracy_logs', 'r') as file:
    print(len(line.strip().split()), "====")
    for line in file:
        x, y = map(float, line.strip().split())
        x_values.append(x)
        y_values.append(y)

plt.plot(x_values, y_values, marker='o', linestyle='-')
plt.title('Accuracy Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

with open('accuracy_logs', 'r') as old_file, open('accuracy_logs_1', 'w') as new_file:
    for line in old_file:
        # 假设第三列数据为3.14，你可以根据你的需求替换这个值
        third_column_data = '3.14'
        # 去除行尾的换行符
        line = line.rstrip()
        # 在行末尾添加第三列数据并写入新文件
        new_line = f'{line} {third_column_data}\n'
        new_file.write(new_line)



