# TODO: implement quick sort

def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        left = [x for x in list[1:] if x < pivot]
        right = [x for x in list[1:] if x >= pivot]

        return quick_sort(left) + [pivot] + quick_sort(right)

list = [1, 3, 6, 24, 6, 7, 3, 2, 4, 6, 2,]
sorted = quick_sort(list)
print(sorted)