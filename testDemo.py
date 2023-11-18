from collections import deque

max_size = 3
my_queue = deque(maxlen=max_size)

my_queue.append(1)
my_queue.append(2)
my_queue.append(3)
my_queue.append(4)  # 这里会自动弹出前面的元素

print(my_queue)  # 输出: deque([2, 3, 4], maxlen=3)