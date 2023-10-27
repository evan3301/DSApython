# TODO: implement insertion sort

'''
Initialize empty list for sorted elements

Iterate over original list

For each item:
    compare with items in sorted list

For items in sorted list greater than current item:
    shift sorted items one space to the right
    insert current item in correct position

Repeat until sorted
'''

def insertion_sort(list):
    n = len(list)
    # Iterate from first item to length of list
    for i in range(1, n):
        '''
        key variable:
            current item being considered for insertion
                starts with second item "i in range(1)"
                ends with last item "i in range end"
        '''
        key = list[i]
        '''
        j variable:
            j of key variable
                starts with last "item i-1"
        '''
        j = i-1
        '''
        while:
            j is not at position -1
            key is less than position j in list

                decrement j by 1 until key = j
        '''
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key


list = [1, 6, 4, 3, 7, 4, 9, 2, 1,]
insertion_sort(list)
print(list)