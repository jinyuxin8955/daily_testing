import datetime


class Example:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


obj = Example(1, 'hello', [1, 2, 3], name='ALice', age=30)
print(obj.kwargs, "====", obj.args)

class Server:
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def get_data(self):
        return self.name

class Client(Server):
    def __init__(self, time):
        self.time = time
        self.args = {"arg1": "value3", "arg2": "value4"}
        self.name = "Server"

    def get_args(self):
        return self.args

    def get_time(self):
        return self.time

client_instance = Client(time=datetime.datetime.now().time())

print(client_instance.get_data())
print(client_instance.get_args())
print(client_instance.get_time())

client_instance.name = "Client"

print(client_instance.get_data())

