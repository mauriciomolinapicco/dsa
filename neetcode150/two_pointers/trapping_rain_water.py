""" LEETCODE HARD
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

"""
class Solution(object):
    def trap(self, height):
        # left to right
        i = 0

        max_h = 0
        agua = []
        for i in range(len(height)):
            agua.append(max(max_h - height[i], 0))
            max_h = max(max_h, height[i])
        
        max_h = 0
        for i in range(len(height) - 1, -1, -1):
            current_agua = max(max_h - height[i], 0)
            agua[i] = min(current_agua, agua[i])
            max_h = max(max_h, height[i])
        
        return sum(agua)
