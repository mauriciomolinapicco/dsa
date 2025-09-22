class Solution(object):
    def isValid(self, s):
        dic = {")":"(", "]":"[", "}":"{"}
        stack = []

        for char in s:
            if char in dic.values():
                stack.append(char)
            else:
                if (stack == [] or stack.pop() != dic[char]): return False
        return True if stack == [] else False