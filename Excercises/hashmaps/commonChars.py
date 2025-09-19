"""
Given an array of strings return the duplicates including duplicates
Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]

"""


from collections import Counter

class Solution(object):
    def commonChars(self, words):
        count = Counter(words[0])
        for word in words:
            count2 = Counter(word)
            for char, cnt in count.items():
                # if count2[char] != cnt:   #->i was using this  if but i can save it actually
                count[char] = min(count2[char], count[char])
        
        res = []
        for char, cnt in count.items():
            for i in range(cnt):
                res.append(char)
        return res