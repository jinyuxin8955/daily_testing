class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __init__(self, name):
        self.name = name




people = []

for i in range(1, 11):
    person = Person(name=f"Person{i}")
    people.append(person)

print(people[0].name)
print(people[9].name)

p = Person(name="p")
q = Person(name="q")
print(p)
print(q)

