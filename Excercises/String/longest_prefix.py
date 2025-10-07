class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ""
        for i in range(len(strs[0])):
            flag = True
            char = strs[0][i]
            for j in range(len(strs)):
                if len(strs[j]) <= i:
                    flag = False
                elif strs[j][i] != char: 
                    flag = False
            if flag:
                result += char  
            else:
                break
        
        return result