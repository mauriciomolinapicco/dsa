class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        result, stack = [0]*n, []
        for i in range(n):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j
            stack.append(i) 
        return result