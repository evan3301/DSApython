# TODO: implement single ended queue from scratch

import unittest

class Queue:
    def __init__(self):
        self.values = []


    def enqueue(self, value):
        # Add items to end of queue
        self.values.append(value)


    def dequeue(self, value):
        # Remove and return item from beginning of queue
        return self.values.pop(value)


    def peek(self):
        # Return value without changing
        return self.values[0]


    def is_empty(self):
        # Checks if queue is empty
        # True if empty, False if not
        return len(self.values) == 0


    def size(self):
        # Checks size of queue
        return len(self.values)


class TestQueue(unittest.TestCase):
    def test_enqueue_dequeue(self):
        q = Queue()

        q.enqueue(1)
        q.enqueue('apple')

        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 'apple')


    def test_peek(self):
        q = Queue()

        q.enqueue(1)
        q.enqueue('apple')

        self.assertEqual(q.peek(), 1)

    def test_is_empty(self):
        q = Queue()

        self.assertTrue(q.is_empty())
        q.enqueue(3)
        self.assertTrue(q.is_empty())


if __name__ == '__main__':
    unittest.main()