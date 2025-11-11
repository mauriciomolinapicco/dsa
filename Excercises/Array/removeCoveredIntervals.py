class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        s = set()
        for i in range(n-1):
            for j in range(i+1, n):
                if intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]:
                    s.add(j)
                if intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                    s.add(i)
        return n - len(s)
