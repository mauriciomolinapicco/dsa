"""
You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the following values:

answer1 : the number of indices i such that nums1[i] exists in nums2.
answer2 : the number of indices i such that nums2[i] exists in nums1.
Return [answer1,answer2].
"""

class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        ans1, ans2 = 0, 0
        set_nums_1 = set(nums1)
        set_nums_2 = set(nums2)

        for num in nums1:
            if num in set_nums_2:
                ans1 += 1
        
        for num in nums2:
            if num in set_nums_1:
                ans2 += 1
        
        return [ans1, ans2]
        