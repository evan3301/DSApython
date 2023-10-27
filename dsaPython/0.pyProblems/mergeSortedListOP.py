'''
Proposed solution:
    create new list
    start with heads of old lists
        compare each node of old lists
            sort them into new list
            return head of new list
'''

'''
class Solution:
    def mergeTwoLists(self, list1, list2):
        list3 = []
        while list1.next and list2.next is not None:
            for i in range(len(list1 and list2)):
                if list1.val[i] < list2.val[i]:
                    list3.append[list1.val[i]]
                    list1 = list1.next
                elif list1.val[i] > list2.val[i]:
                    list3.append[list2.val[i]]
                    list2 = list2.next
                else:
                    list3.append[list1.val[i]]
                    list1 = list1.next
            return list3
'''

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Dummy node to handle edge case of empty list
        dummy = ListNode()
        # Tail initially set to dummy node
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                # Add to output list
                tail.next = l1
                # Update pointer
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            # Update tail pointer at the end
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        # return .next traversal
        return dummy.next