import numpy as np

# 模拟模型预测概率
# 以二分类为例，每个样本有两个类被的预测概率
# 每一行表示一个样本的预测概率分布
# 模拟的数据为10个样本，每个样本有2个类别

predictions = np.random.rand(10, 2)

print(predictions)

# 计算样本的熵
def calculate_entropy(probabilities):
    return -np.sum(probabilities * np.log2(probabilities + 1e-10), axis=1)

print(calculate_entropy(predictions))

# 计算样本最大类别概率
def calculate_max_class_probability(probabilities):
    return np.max(probabilities, axis=1)

# 计算样本最小边缘
def calculate_min_margin(probabilities):
    sorted_probs = np.sort(probabilities, axis=1)
    return sorted_probs[:, -1] - sorted_probs[:, -2]

def select_uncertain_samples(prediction, method='entropy'):
    if method == 'entropy':
        uncertainty_scores = calculate_entropy(prediction)
    elif method == 'max_class_probability':
        uncertainty_scores = 1 - calculate_max_class_probability(prediction)
    elif method == 'min_margin':
        uncertainty_scores = calculate_min_margin(prediction)
    else:
        raise ValueError('Invalid uncertainty sampling method.')

    return np.argsort(uncertainty_scores)[::-1]

selected_samples_entropy = select_uncertain_samples(predictions, method='entropy')
print("Samples selected using entropy:", selected_samples_entropy)

# 使用最大类别概率作为不确定性度量选择样本
selected_samples_max_class_prob = select_uncertain_samples(predictions, method='max_class_probability')
print("Samples selected using max class probability:", selected_samples_max_class_prob)

# 使用最小边缘作为不确定性度量选择样本
selected_samples_min_margin = select_uncertain_samples(predictions, method='min_margin')
print("Samples selected using min margin:", selected_samples_min_margin)
