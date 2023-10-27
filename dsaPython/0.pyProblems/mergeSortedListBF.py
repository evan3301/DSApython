# TODO: Given two sorted lists, merge them into one sorted list
# Sort in ascending order

'''
Proposed solution:
    create new list
    start with heads of old lists
        compare each node of old lists
            sort them into new list
            return head of new list
'''

class Solution:
    def mergeTwoLists(self, list1, list2):
        list3 = []

        list1 = ListNode
        while ListNode is not None:
            list3.append(list1.val)
            list1 = list1.next

        list2 = ListNode
        while ListNode is not None:
            list3.append(list2.val)
            list2 = list2.next

        list3.sort()
        return list3