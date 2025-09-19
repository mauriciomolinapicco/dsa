class Solution(object):
    def removeDuplicates(self, nums):
        # i will do two pointers, l and r.
        # r will iterate through the array while l will be in the position of the next unique number
        l = 1
        for r in range(1, len(nums)):
            if nums[r - 1] != nums[r]:
                nums[l] = nums[r]
                l += 1
        return l
