class Solution(object):
    """
    two sum but array is sorted. Use two pointer
    """
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l < r:
            suma = numbers[l] + numbers[r]
            if suma > target:
                r -= 1
            elif suma < target:
                l += 1
            else:
                #the +1 are only cause the answer requires a 1-indexed array
                return [l+1,r+1]