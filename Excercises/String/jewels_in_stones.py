class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        con = 0 
        for char in stones:
            if char in jewels:
                con += 1
        return con