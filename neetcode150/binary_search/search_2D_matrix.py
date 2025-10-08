class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])
        #search row
        l, r = 0, rows - 1
        while l <= r:
            m = (l+r) // 2
            m1, m2 = matrix[m][0], matrix[m][cols-1]
            if target >= m1 and target <= m2:
                break
            elif target < m1:
                r = m-1
            else:
                l = m+1
        row = m
        #search index
        l, r = 0, cols-1
        i = None
        while l <= r:
            m = (l+r) // 2
            if matrix[row][m] == target: 
                return True
            elif matrix[row][m] > target:
                r = m-1
            else:
                l = m+1
        return False