class Solution(object):
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])

        def bfs_islands(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols: return
            if grid[r][c] == '0': return

            #hundir el pedazo de tierra para que no se tome en consideracion en las otras busquedas
            # pq quedaria en ciclo infinito
            grid[r][c] = '0'

            bfs_islands(r,c+1)
            bfs_islands(r,c-1)
            bfs_islands(r+1,c)
            bfs_islands(r-1,c)

        result = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    result += 1
                    bfs_islands(r,c)
        return result