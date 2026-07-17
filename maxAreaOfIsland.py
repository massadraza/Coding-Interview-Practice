class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxArea = 0

        def bfs(r, c):
            area = 0
            q = deque()
            visit.add((r, c))
            q.append((r, c))
            while q: 
                row, col = q.popleft()
                area += 1
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = bfs(r, c)
                    maxArea = max(maxArea, area)
        
        return maxArea
