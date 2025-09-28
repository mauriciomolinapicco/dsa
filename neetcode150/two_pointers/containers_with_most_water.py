"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints 
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
"""
"""
La CLAVE de la solucion esta en 
"""
class Solution:
    def maxArea(self, heights):
        i = 0
        j = len(heights) - 1

        maximo = 0
        while(i < j):
            base = j - i
            altura = min(heights[i], heights[j])
            current = base * altura
            maximo = max(current, maximo)

            if(heights[i] > heights[j]):
                j -= 1
            else:
                i += 1
        
        return maximo
