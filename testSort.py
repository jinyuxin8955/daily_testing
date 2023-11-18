# 假设你有一个包含用户ID和准确率的列表
user_accuracy_data = [
    {"user_id": 1, "accuracy": 0.85},
    {"user_id": 2, "accuracy": 0.92},
    {"user_id": 3, "accuracy": 0.78},
    # 其他用户的数据
]

# 1. 根据准确率降序排列用户
sorted_users = sorted(user_accuracy_data, key=lambda x: x["accuracy"], reverse=True)
print(sorted_users)

# 2. 选择合适的用户ID
threshold_accuracy = 0.8  # 设置一个准确率阈值，用于筛选用户
selected_users = [user["user_id"] for user in sorted_users if user["accuracy"] >= threshold_accuracy]

# 现在selected_users包含了那些准确率高于阈值的用户ID

print(selected_users)