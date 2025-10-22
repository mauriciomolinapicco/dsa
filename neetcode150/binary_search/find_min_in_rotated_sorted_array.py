class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[l] <= nums[r]: return nums[l]
            if nums[m] > nums[l]:
                if nums[m] > nums[r]:
                    l = m+1
                else:
                    r = m-1
            else:
                if nums[m] < nums[r]:
                    r = m
                else:
                    l = m+1
                    
        return nums[r]