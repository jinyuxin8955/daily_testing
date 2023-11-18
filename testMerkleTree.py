
import hashlib


def calculate_hash(data):

    hash_object = hashlib.sha256(data.encode())
    return hash_object.hexdigest()

def make_length_even(data):

    if len(data) % 2 != 0:
        data.append(data[-1])

    return data

def construct_merkle(merkle_tree):
    print("start")

    if len(merkle_tree) == 0:
        return None

    while len(merkle_tree) > 1:
        next_level = []

        merkle_tree = make_length_even(merkle_tree)
        for i in range(0, len(merkle_tree), 2):
            combined_hash = merkle_tree[i] + merkle_tree[i + 1]
            next_level.append(calculate_hash(combined_hash))

        if len(next_level) > 1:
            merkle_tree = make_length_even(next_level)
        else:
            merkle_tree = next_level

    return merkle_tree[0]




if __name__ == '__main__':

    data_blocks = ["A", "B", "C", "D", "E"]
    merkle_tree = []
    for item in data_blocks:
        merkle_tree.append(calculate_hash(item))
    make_length_even(merkle_tree)

    root_hash = construct_merkle(merkle_tree)
    print(root_hash)