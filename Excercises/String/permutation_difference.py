#encontrar la suma de las diferencias absolutas
class Solution(object):
    def findPermutationDifference(self, s, t):
        con = 0
        for char in s:
            a = s.index(char)
            b = t.index(char)
            con += abs(a-b)
        return con
