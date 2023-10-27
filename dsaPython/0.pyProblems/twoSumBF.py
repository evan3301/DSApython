# TODO: given list of num, find which two nums sum to target num
# Desired time complexity: O(n^2) or faster

'''
Proposed solution:
    add each number to number beside it
        check if sum == taget True
            return index of summed nums
    Time complexity: O(n^2) because you are checking n values + n other values -> n*n
'''
'''
class Solution:
    def twoSum(self, nums, target):
        nums = []

        while sum != target:
            for i in nums:
                sum = nums[i] + nums[i+1]
                return sum

    target = int(input("Target: "))


twoSum = [1, 2, 3, 4, 5, 6, 7,]
'''

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

