class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        cur_dis = float('inf')
        for i in range(n):
            if nums[i] == 1:
                if cur_dis < k: return False
                cur_dis = 0
                continue
            cur_dis += 1
            
        return True
    

#faster solution
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_index = -1
        for i, n in enumerate(nums):
            if n == 1:
                if last_index < 0:
                    last_index = i 
                    continue
                d = i - last_index
                if d <= k: 
                    return False
                last_index = i
        return True