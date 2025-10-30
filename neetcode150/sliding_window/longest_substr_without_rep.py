class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j,longest,n = 0,0,0,len(s)
        seen = set()
        while j<n:
            if s[j] not in seen:
                seen.add(s[j])
                j += 1
                if len(seen) > longest: longest = len(seen)
            else:
                seen.remove(s[j])
                while s[i] in seen:
                    seen.remove(s[i])
                    i += 1
                seen.add(s[i])
                i += 1
                j += 1
        return longest