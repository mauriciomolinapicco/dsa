class Solution(object):
    def numIdenticalPairs(self, nums):
        sum = 0
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    sum += 1
        return sum
        
"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j."""