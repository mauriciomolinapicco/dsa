"""
En base a nums[i] = -(nums[j]+nums[k])
Recorremos el array con i y para el "resto" del array (a la derecha de i) usamos TWO POINTERS
"""
class Solution(object):
    def threeSum(self, nums):
        nums.sort()

        k = len(nums) - 1
        result = []
        for i in range(len(nums)):
            target = -nums[i]
            j = i + 1
            while(j < k):
                current = nums[j] + nums[k]
                if(current == target):
                    result.append((nums[i], nums[j], nums[k]))
                    j += 1
                elif(current < target):
                    j += 1
                else:
                    k -= 1
            k = len(nums) - 1

        return list(set(result))