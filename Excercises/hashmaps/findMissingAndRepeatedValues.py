""""
You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

 

Example 1:

Input: grid = [[1,3],[2,2]]
Output: [2,4]
Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].
"""
class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        numbers = {i:0 for i in range(1, (n*n) + 1)}
        for i in range(n):
            for j in range(n):
                num = grid[i][j]
                numbers[num] = numbers.get(num,0) + 1
        
        for num in numbers:
            if numbers[num] == 0:
                ans2 = num
            elif numbers[num] == 2:
                ans1 = num
        return [ans1,ans2]