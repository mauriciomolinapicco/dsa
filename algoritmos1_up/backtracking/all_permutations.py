class Solution:
    def __init__(self):
        self.l = []

    def bt(self, l_provisoria, ya_los_vi, nums):
        if len(l_provisoria) == len(nums):
            self.l.append(l_provisoria[:]) # [:] hace una shallow copy
            return

        for i in range(len(nums)):
            if i not in ya_los_vi:
                l_provisoria.append(nums[i])
                ya_los_vi.add(i)
                self.bt(l_provisoria, ya_los_vi, nums)
                ya_los_vi.remove(i)
                l_provisoria.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.bt([], set(), nums)

        return self.l
