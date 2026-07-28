from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    queue.append((r,c))

        while queue:
            curr_r, curr_c = queue.popleft()

            for dr, dc in directions:
                next_r, next_c = curr_r + dr, curr_c + dc
                if 0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]):
                    if grid[next_r][next_c] == 2147483647:
                        grid[next_r][next_c] = grid[curr_r][curr_c] + 1
                        queue.append((next_r, next_c))