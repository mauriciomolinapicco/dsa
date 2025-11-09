#leet 2038
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        h = {}
        h["A"] = 0
        h["B"] = 0
        for i in range(1, n-1):
            c = colors[i]
            if colors[i-1] == c and colors[i+1] == c:
                h[c] += 1
        return h["A"] > h["B"]