# TODO: create a dynamic array via classes

class DynamicArray:
    def __init__(self):
        self.list = []

    def add(self, item):
        self.list.append(item)

    def remove(self, item):
        self.list.remove(item)

# Use __str__ method for string representation of object
    def __str__(self):
        return str(self.list)

# Create instance of class
d1 = DynamicArray()

# Use class methods to add or remove
d1.add(1)
d1.add(2)
d1.add(3)

print(d1)

d1.remove(2)

print(d1)