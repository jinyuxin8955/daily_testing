a = [1, 2, 3]
b = ['a', 'b', 'c']
c = [4, 5, 6]
w = [0.1, 0.2]
lists = [a, c]
l = list(zip(*lists))
print(l)
d = [sum(ws * s for ws, s in zip(w, elements)) for elements in zip(*lists)]
new = []
for elements in zip(*lists):
    j = 0
    for ws, s in zip(w, elements):
        j += ws * s
    new.append(j)

print(d)

import copy

original_list = [[1, 2], [3, 4]]
copied_list = copy.deepcopy(original_list)

print(copied_list)
cp = original_list.copy()
print(cp)