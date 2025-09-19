class Solution(object):
    def pivotArray(self, nums, pivot):
        less = []
        greater = []
        con = 0 # count how many times the pivot appears
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                con += 1
        eq = [pivot] * con #having the number of times the pivot appears we create the subarray
        return less + eq + greater #append the array back together