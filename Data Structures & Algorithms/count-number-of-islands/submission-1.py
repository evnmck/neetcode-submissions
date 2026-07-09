from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = deque()
        count = 0

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == "1":
                    count += 1
                    queue.append((x,y))
        
                    while queue:
                        curr_x, curr_y = queue.popleft()

                        if grid[curr_x][curr_y] == "1":
                            grid[curr_x][curr_y] = "0"
                        
                            neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                            for dx, dy in neighbors:
                                next_x = curr_x + dx
                                next_y = curr_y + dy

                                if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and grid[next_x][next_y] == "1":
                                    queue.append((next_x, next_y))
        return count


        