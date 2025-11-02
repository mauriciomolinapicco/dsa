# brute force approach
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        c = Counter(s1)
        i,j = 0,len(s1)
        while j <= n:
            c1 = Counter(s2[i:j])
            if c == c1: return True
            i += 1
            j += 1
        return False

# better approach
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,n1 = len(s2), len(s1)
        c = Counter(s1)
        c1 = Counter()
        i,j = 0,0
        while i < (n - n1 + 1):
            while abs(j - i) < n1:
                c1[s2[j]] += 1
                if c1[s2[j]] > c[s2[j]]:
                    break
                j += 1
            if c1 == c: return True
            i += 1
            j = i 
            c1 = Counter()
        return False

#pending
#optimize to O(n) 
