# TODO: implement merge sort

def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left_half = list[:mid]
        right_half = list[mid:]
        # Keep recursively diving left & right half
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            # Compare smallest element in each half
            if left_half[i] < right_half[j]:
                # smallest element is added to list at position k = 0 (start of list)
                list[k] = left_half[i]
                i += 1
            else:
                list[k] = right_half[j]
                j += 1
            # Merge restarts for k = 1 (second position in list)
            k += 1

        # Any unmerged elements in left_half are sorted and merged again
        while i < len(left_half):
            list[k] = left_half[i]
            i += 1
            k += 1

        # Any unmerged elements in right_half are sorted and merged again
        while j < len(right_half):
            list[k] = right_half[j]
            j += 1
            k += 1

        return list


num = [3, 4, 2 ,1 ,3 ,4, 5, 3, 6, 6, 2, 4,]
merge_sort(num)
print(num)