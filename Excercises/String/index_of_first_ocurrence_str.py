class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1
    

    def fasterSolution(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if needle == haystack[i, i + len(needle)]: 
                return i
        return -1