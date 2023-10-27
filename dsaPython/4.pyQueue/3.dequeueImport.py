# TODO: implement dequeue via dequeue library
### Also doubles as Stack

from collections import deque

d1 = deque([1, 2, 3, 4,])
print(d1)

# Appends from the left
d1.append(5)
print(d1)

# Appends from the right
d1.appendleft(0)
print(d1)

# Pops from the right
d1.pop()
print(d1)

# Pops from the left
d1.popleft()
print(d1)

# Extends list by however-many-elements from the right
d1.extend([5, 6, 7, 8])
print(d1)

# Extends list by however-many-elements from the right
d1.extendleft([-3, -2, -1, 0])
print(d1)

# Reverses list via reverse()
d1.reverse()
print(d1)

# Rotates list to the left by 1
d1.rotate(-1)
print(d1)

# Prints length of list
print(len(d1))