# TODO: create a double ended queue from scratch

class Dequeue:
    def __init__(self):
        self.queue = []
        self.count = 0


    # Creates readable queue
    def __repr__(self):
        return str(self.queue)


    def add_to_front(self, value):
        # Insert adds value to position 0 (front) of list
        self.queue.insert(0, value)
        # Extend list by one
        self.count += 1


    def add_to_rear(self, value):
        # Append adds value to end of list
        self.queue.append(value)
        # Extend list by one
        self.count += 1


    def remove_from_front(self):
        if self.count > 0:
            self.count -= 1
            # Remove from position 0 (front of list)
            return self.queue.pop(0)
        else:
            return ValueError ('Dequeue is empty')


    def remove_from_rear(self):
        if self.count > 0:
            self.count -= 1
            # Remove from end of list
            return self.queue.pop()
        else:
            return ValueError ('Dequeue is empty')


    def size(self):
        return self.count

# Time complexity: O(1)