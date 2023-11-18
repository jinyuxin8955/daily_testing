class VirtualWorker:
    def __init__(self, hook, id):
        self.hook = hook
        self.id = id

# virtual_worker = VirtualWorkerClient(hook=hook, name='virtual_worker')
worker_1st = VirtualWorker(hook='hook', id='worker_1st')
worker_2nd = VirtualWorker(hook='hook', id='worker_2nd')
worker_3rd = VirtualWorker(hook='hook', id='worker_3rd')

worker_list = (worker_1st, worker_2nd)
print(worker_list)

worker_list = list(worker_list)
worker_list.append(worker_3rd)
worker_list = tuple(worker_list)

print(worker_list)

# print(tuple(list(worker_list).append(worker_3rd)))

worker_list = worker_2nd 
print(worker_list)

def add_worker(tuple_list, worker):
    tuple_list = list(tuple_list)
    tuple_list.append(worker)
    tuple_list = tuple(tuple_list)
    return tuple_list
add_worker(worker_list, worker_3rd)
print(worker_list)
add_worker(worker_list, worker_1st)
print(worker_list)