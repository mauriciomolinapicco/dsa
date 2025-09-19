class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        for i in range(len(strs[0])):
            for c in strs:
                if i == len(c) or c[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix