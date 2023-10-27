'''
Proposed solution:
    if target 4:
        current value - target value
            check if in list
'''
'''
class solution:
    def twoSum(self, nums, target):
        for i, x in enumerate(range(len(nums))):
            diff = target - x
            if diff in nums:
                return(i, diff)
'''

class solution:
    def twoSum(self, nums, target):
        # Empty hashmap to store already-processed elements
        prevMap = {} # mapping value : index

        # Iterate through every index in array
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            # if diff not in prevMap, add to prevMap hashmap
            prevMap[n] = i