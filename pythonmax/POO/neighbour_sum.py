class NeighborSum(object):

    def __init__(self, grid):
        self.grid = grid
        

    def adjacentSum(self, value):
        row,col = self.get_position(value)
        if row is None or col is None:
            return 0
            
        sum = 0
        n = len(self.grid)
        if row < n-1:
            sum += self.grid[row+1][col]
        if row != 0:
            sum += self.grid[row-1][col]
        if col < n-1:
            sum += self.grid[row][col+1]
        if col != 0:
            sum += self.grid[row][col-1]
        return sum

        
    def diagonalSum(self, value):
        row,col = self.get_position(value)
        if row is None or col is None:
            return 0
            
        sum = 0
        n = len(self.grid)
        if row < n-1:
            if col < n-1:
                print(col, row, n)
                sum += self.grid[row+1][col+1]
            if col != 0:
                sum += self.grid[row+1][col-1]
        if row != 0:
            if col < n-1:
                sum += self.grid[row-1][col+1]
            if col != 0:
                sum += self.grid[row-1][col-1]

        return sum

    def get_position(self, value):
        n = len(self.grid)
        for i in range(n):
            for j in range(n):
                if self.grid[i][j] == value:
                    return (i,j)
        return None


#much better way of doing it
class NeighborSum(object):

    def __init__(self, grid):
        self.grid = grid
        

    def adjacentSum(self, value):
        row,col = self.get_position(value)
        if row is None or col is None:
            return 0
        sum = 0
        for i in range(len(self.grid)):
            if i != row and i in range(row-1,row+2):
                sum += self.grid[i][col]
            if i != col and i in range(col-1,col+2):
                sum += self.grid[row][i]
        return sum

        
    def diagonalSum(self, value):
        row,col = self.get_position(value)
        if row is None or col is None:
            return 0
        sum = 0
        n = len(self.grid)
        for i in range(row - 1, row + 2):  
            for j in range(col - 1, col + 2):  
                if 0 <= i < n and 0 <= j < n:
                    if abs(i - row) == abs(j - col): 
                        if i != row or j != col:
                            sum += self.grid[i][j]
        return sum
        

    def get_position(self, value):
        n = len(self.grid)
        for i in range(n):
            for j in range(n):
                if self.grid[i][j] == value:
                    return (i,j)
        return None
        