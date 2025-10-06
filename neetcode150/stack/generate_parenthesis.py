class Solution(object):
    def generateParenthesis(self, n):
        result = []
        def rec(st, left, right):
            if right > left: return
            if left > n or right > n: return

            if left+right == n*2: 
                result.append(st)
                return

            rec(st + "(", left+1, right)
            rec(st + ")", left, right+1)

        rec("(", 1, 0)
        return result