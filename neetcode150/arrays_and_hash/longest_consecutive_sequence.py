import heapq

class Solution(object):
    def longestConsecutive(self, nums):
        if nums == []:
            return 0 

        heapq.heapify(nums)
        anterior = heapq.heappop(nums)
        longest = 0
        candidate = 0

        for i in range(len(nums)):
            minimo = heapq.heappop(nums)
            if anterior == minimo:
                continue
            elif (minimo - anterior) == 1:
                candidate += 1
                if candidate > longest:
                    longest = candidate
            else:
                candidate = 0
            anterior = minimo
        
        return longest + 1
