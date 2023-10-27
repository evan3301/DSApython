# TODO: implement heap via heapq import

'''
Heapq functions:
    Heapify(iterable)       Transform list into heap
    Heappush(heap, item)    Push value into heap
    Heappop(item)           Pop and return smallest item in heap
'''

import heapq

list = [1, 2, 3, 4, 5, 6,]

heapq.heapify(list)
print(list)

heapq.heappush(list, 13)
print(list)

heapq.heappop(list)
print(list)

print(heapq.nlargest(1, list))

print(heapq.nsmallest(2, list))