import numpy as np
import matplotlib.pyplot as plt

def cosine_similarity(v1, v2):
    """计算两个向量的夹角余弦"""
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_product / (norm_v1 * norm_v2)

def add_gaussian_noise(vector, mean=0, std=1):
    """向向量添加高斯噪声"""
    noise = np.random.normal(mean, std, vector.shape)
    return vector + noise

# 模拟两个梯度向量
g1 = np.array([3, 2, 5, 7, 8])
g2 = np.array([0, 7, 2, 0, 1])

# 计算原始夹角余弦
cos_theta_original = cosine_similarity(g1, g2)
print("原始夹角余弦:", cos_theta_original)

# 模拟多次实验，分别给 g1 和 g2 添加高斯噪声并计算夹角余弦
num_experiments = 1000
cos_theta_samples = []

for _ in range(num_experiments):
    g1_noisy = add_gaussian_noise(g1)
    g2_noisy = add_gaussian_noise(g2)
    cos_theta_noisy = cosine_similarity(g1_noisy, g2_noisy)
    cos_theta_samples.append(cos_theta_noisy)

# 绘制夹角余弦分布图
plt.hist(cos_theta_samples, bins=30, edgecolor='black')
plt.show()

# 计算夹角余弦的均值和标准差
mean_cos_theta_noisy = np.mean(cos_theta_samples)
std_cos_theta_noisy = np.std(cos_theta_samples)

print("模拟实验后夹角余弦的均值:", mean_cos_theta_noisy)
print("模拟实验后夹角余弦的标准差:", std_cos_theta_noisy)
