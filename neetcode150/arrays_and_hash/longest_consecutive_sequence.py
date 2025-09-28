# forma O(n) usando DFS aprovechando el tiempo de busqueda O(1) de los sets
class Solution(object):
    def seq_dfs(self, s, num):
        if num not in s:
            return 0

        s.remove(num)
        return 1 + self.seq_dfs(s, num+1) + self.seq_dfs(s, num-1)

    def longestConsecutive(self, nums):   
        s = set(nums)
        maximo = 0

        while len(s) > 0:
            seq = self.seq_dfs(s, next(iter(s)))
            maximo = max(maximo, seq)
        return maximo


# forma O(n*log(n)) usando heaps
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
