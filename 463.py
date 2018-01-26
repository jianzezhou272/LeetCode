class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lon = len(grid)
        lat = len(grid[0])

        ver = sum(grid[0]) + sum(grid[lon - 1])
        for i in range(lon - 1):
            for j in range(lat):
                ver += abs(grid[i + 1][j] - grid[i][j])

        hon = 0
        for k in range(lon):
            hon += grid[k][0]
            for l in range(lat - 1):
                hon += abs(grid[k][l + 1] - grid[k][l])
            hon += grid[k][lat - 1]

        return hon + ver