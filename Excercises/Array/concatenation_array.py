class Solution(object):
    def getConcatenation(self, nums):
        ans = [0] * len(nums) * 2
        n = len(nums)
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans
    
