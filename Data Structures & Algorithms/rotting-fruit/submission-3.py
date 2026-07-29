from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        distances = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque()
        fresh = 0
        minutes = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))

        while queue and fresh > 0:

            minutes += 1
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()

                for dr, dc in distances:
                    r2 = r + dr
                    c2 = c + dc

                    if 0 <= r2 < len(grid) and 0 <= c2 < len(grid[0]):
                        if grid[r2][c2] == 1:
                            grid[r2][c2] = 2
                            fresh -= 1
                            queue.append((r2,c2))

        return minutes if fresh == 0 else -1


