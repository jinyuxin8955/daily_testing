similarities = [0.85, 0.92, 0.76, 0.95, 0.88]

# 使用内置的 sorted 函数对相似度值进行降序排序
sorted_similarities = sorted(similarities, reverse=True)

# 选择前几个相似度值
num_top_similarities = 3  # 假设选择前三个相似度值
top_similarities = sorted_similarities[:num_top_similarities]

# 输出排序后的相似度值和选择的前几个相似度值
print("Sorted similarities:", sorted_similarities)
print("Top similarities:", top_similarities)