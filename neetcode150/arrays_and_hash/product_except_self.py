class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        pos_cero = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                if pos_cero != -1:
                    return [0] * len(nums)
                pos_cero = i
                
            else:
                total_prod *= nums[i]

        result = []
        for i in range(len(nums)):
            if pos_cero != -1:
                if i == pos_cero:
                    element = total_prod
                else:
                    element = 0
            else:
                element = total_prod / nums[i]
            result.append(int(element))
        return result