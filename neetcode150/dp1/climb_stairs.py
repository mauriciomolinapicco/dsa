"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
RESULT = basically a fibonacci sequence starting at 
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        self.mem = [-1] * (n+1)
        def fibo(n: int) -> int:
            if n == 0: return 0
            if n == 1: return 1
            if self.mem[n-1] >= 0: return self.mem[n-1]
            self.mem[n-1] = fibo(n-1) + fibo(n-2)
            return self.mem[n-1]
        return fibo(n+1)