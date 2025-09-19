# number of operations to make every number on the array divisible by 3 (simple cause its one operation max per number)
class Solution(object):
    def minimumOperations(self, nums):
        ans = 0
        for i in range(len(nums)):
            if nums[i] % 3 == 0:
                continue
            ans += 1
        return ans