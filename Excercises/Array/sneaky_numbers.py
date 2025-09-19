class Solution(object):
    def getSneakyNumbers(self, nums):
        ans = []
        for i in range(len(nums)):
            if nums[i] in nums[:i]:
                ans.append(nums[i])
        return ans
    
# return the two repeated numbers
