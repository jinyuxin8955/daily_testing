import torch

my_list = [1, 2, 3, 4, 5]

my_tensor = torch.tensor(my_list, dtype=torch.float)

print(my_tensor, type(my_list), type(my_tensor))

weights = torch.tensor([0.1, 0.2, 0.3, 0.4, 0.5], dtype=torch.float)

result = torch.dot(my_tensor, weights)

print(result.item)


tensor1 = torch.tensor([1, 2, 3], dtype=torch.float)
tensor2 = torch.tensor([4, 5, 6], dtype=torch.float)
tensor3 = torch.tensor([7, 8, 9], dtype=torch.float)

vector_list = [tensor1, tensor2, tensor3]

print(vector_list)

weights_3 = [0.3, 0.5, 0.2]

def combineVectors(*vectors):

    vector_list = list(vectors)

    return vector_list

vl1 = combineVectors(tensor1, tensor2, tensor3)
vl2 = combineVectors(tensor1, tensor3)

print(vl1, "++++", vl2, "====", len(vl1), "----", len(vl2))

new_vector = sum(w * v for w, v in zip(weights_3, vl1))

print(new_vector)