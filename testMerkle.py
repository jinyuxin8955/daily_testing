import hashlib


def calculate_hash(data):
    # 使用 SHA-256 哈希函数计算数据的哈希值
    hash_object = hashlib.sha256(data.encode())
    return hash_object.hexdigest()


def make_length_even(data):
    # 如果数据不是偶数个，复制最后一个数据
    if len(data) % 2 != 0:
        data.append(data[-1])

    return data


def construct_merkle_tree(data):
    if len(data) == 0:
        return None

    # 如果数据不是偶数个，复制最后一个数据
    if len(data) % 2 != 0:
        data.append(data[-1])

    merkle_tree = []

    # 计算数据块的哈希值并添加到默克尔树中
    for item in data:
        merkle_tree.append(calculate_hash(item))

    # 逐级构建默克尔树
    while len(merkle_tree) > 1:
        next_level = []

        for i in range(0, len(merkle_tree), 2):
            # 将相邻的两个哈希值拼接并计算其哈希值
            combined_hash = merkle_tree[i] + merkle_tree[i + 1]
            next_level.append(calculate_hash(combined_hash))

        merkle_tree = next_level

    return merkle_tree[0]  # 返回根哈希


def construct_merkle(merkle_tree):
    print("start")

    if len(merkle_tree) == 0:
        return None

    # 逐级构建默克尔树
    while len(merkle_tree) > 1:
        next_level = []

        merkle_tree = make_length_even(merkle_tree)
        for i in range(0, len(merkle_tree), 2):
            print(i)
            # 将相邻的两个哈希值拼接并计算其哈希值
            combined_hash = merkle_tree[i] + merkle_tree[i + 1]
            next_level.append(calculate_hash(combined_hash))

        if len(next_level) > 1:
            merkle_tree = make_length_even(next_level)
        else:
            merkle_tree = next_level

        print(len(merkle_tree))

    return merkle_tree[0]  # 返回根哈希


if __name__ == '__main__':
    # 数据块
    data_blocks = ["A", "B", "C", "D", "E", "F", "G"]

    merkle_tree = []

    for item in data_blocks:
        merkle_tree.append(calculate_hash(item))

    print(merkle_tree)

    make_length_even(merkle_tree)

    print(len(merkle_tree))

    i = construct_merkle(merkle_tree)
    print(i)

    # 构建默克尔树
    merkle_root = construct_merkle_tree(data_blocks)

    print("默克尔树的根哈希:", merkle_root)

    print(i == merkle_root)