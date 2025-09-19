class Solution(object):
    def kthDistinct(self, arr, k):
        appearances = {}
        for s in arr:
            appearances[s] = appearances.get(s, 0) + 1
        
        distinct = [item for item in arr if appearances[item] == 1]

        if len(distinct) >= k:
            return distinct[k - 1]
        else:
            return ""