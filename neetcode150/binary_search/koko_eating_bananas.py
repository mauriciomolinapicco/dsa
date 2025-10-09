"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k 
bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any 
more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.
"""
# Brute force approach
class Solution(object):
    def minEatingSpeed(self, piles, h):
        max_k, n = max(piles), len(piles)
        for k in range(1,max_k+1):
            hours_taken = 0
            for j in range(n):
                hj = piles[j]/k
                hj = int(hj) + (1 if piles[j] % k != 0 else 0)
                hours_taken += hj

            if hours_taken <= h: 
                return k

#fixed py2.7 bug of math.ceil
import math
class Solution:
    def minEatingSpeed(self,piles, h):
        max_k, n = max(piles), len(piles)
        possible_ks = [k for k in range(1,max_k+1)]
        for k in range(1,max_k+1):
            hours_taken = 0
            for j in range(n):
                hours_taken += math.ceil(piles[j]/k)

            if hours_taken <= h: 
                return k 

# binary search upgrade
