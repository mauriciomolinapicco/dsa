class Solution(object):
    def lengthOfLastWord(self, s):
        res = 0
        started = False
        for i in range(1, len(s)+1):
            c = s[-i]
            if c == " ":
                if started:
                    return res
            else:
                res += 1
                if not started:
                    started = True       
        return res