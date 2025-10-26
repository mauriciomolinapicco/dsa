class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def classic_bs(nums, target,l,r):
            while l <= r:
                m = (l+r) // 2
                if nums[m] == target: 
                    return m
                elif nums[m] > target:
                    r = m-1
                else:
                    l = m+1
            return -1

        l,r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[l] <= target and target <= nums[r]:
                return classic_bs(nums, target,l,r)
            
            
            if nums[l] <= nums[m]:
                if target <= nums[m] and target >= nums[l]: 
                    return classic_bs(nums,target,l,m)
                else:
                    l = m+1

            if nums[m] <= nums[r]: 
                if target <= nums[r] and target >= nums[m]: 
                    return classic_bs(nums,target,m,r)
                else:
                    r = m-1
        return -1