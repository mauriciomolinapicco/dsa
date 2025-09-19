class Solution(object):
    def transformArray(self, nums):
        n = len(nums)
        res = [0] * n

        for i in range(n):
            if nums[i] % 2 != 0:
                res[i] = 1
        return sorted(res)
        