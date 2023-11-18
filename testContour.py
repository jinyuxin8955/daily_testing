import numpy as np
import matplotlib.pyplot as plt

# 生成示例数据
theta0_values = np.linspace(-10, 10, 100)
theta1_values = np.linspace(-10, 10, 100)

# 生成网格点
theta0_mesh, theta1_mesh = np.meshgrid(theta0_values, theta1_values)

# 代价函数，这里假设是一个简单的二次函数
def cost_function(theta0, theta1):
    return 0.5 * (theta0**2 + 10*theta1**2)  # 注意特征1的系数更大

# 计算代价函数值
cost_values = cost_function(theta0_mesh, theta1_mesh)

# 绘制等值线图
plt.contour(theta0_mesh, theta1_mesh, cost_values, levels=np.logspace(-2, 3, 20))
plt.xlabel('Theta0')
plt.ylabel('Theta1')
plt.title('Cost Function Contours (Unscaled Features)')
plt.colorbar(label='Cost')
plt.show()
