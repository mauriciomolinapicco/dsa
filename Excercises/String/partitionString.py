class Solution(object):
    """ leetcode 2405 
    Encontrar particion optima de string para particiones sin characters repetidos
    """
    def partitionString(self, s):
        con = 1
        seen = set()
        for char in s:
            if char in seen:
                con += 1
                seen = set()
            seen.add(char)
        return con
        