# TODO: implement linked list in python (do not use a library)

import unittest

# Create object Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Create object LinkedList, initialize head to none
class LinkedList:
    def __init__(self):
        self.head = None


    def add_node(self, value):
        # Initialize new_node to object Node
        new_node = Node(value)

        # Create new head
        if self.head is None:
            self.head = new_node
            return

        # Start traversal creating new nodes as you go
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node


    def delete_node(self, value):
        # If list is empty, return
        if self.head is None:
            return

        # If deleting head value, initialize next node as head
        if self.head.value == value:
            self.head = self.head.next
            return

        # Traverse tree looking for first node with matching value
        # If next node is the value, delete it and move to next.next node
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next


    def print_list(self):
        # Traverse tree and print each node until None
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next


class TestLinkedList(unittest.TestCase):
    def test_linked_list_operations(self):
        # Initialize empty linked list
        linked_list = LinkedList()

        # Add nodes
        linked_list.add_node(1)
        linked_list.add_node(2)
        linked_list.add_node(3)
        linked_list.add_node(4)

        self.assertEqual(linked_list.print_list(), None)

        linked_list.delete_node(3)

        self.assertEqual(linked_list.print_list(), None)

if __name__ == '__main__':
    unittest.main()

# Time complexity: O(n) where n = # of nodes