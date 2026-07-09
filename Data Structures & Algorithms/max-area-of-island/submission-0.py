from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        queue = deque()
        neighbors = [(1,0),(-1,0),(0,1),(0,-1)]

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                curr_area = 0
                if grid[x][y] == 1:
                    grid[x][y] = 0
                    queue.append((x,y))

                    while queue:
                        
                        curr_area += 1
                        curr_x, curr_y = queue.popleft()

                        for dx, dy in neighbors:

                            next_x = curr_x + dx
                            next_y = curr_y + dy

                            if (
                                0 <= next_x < len(grid) 
                                and 0 <= next_y < len(grid[next_x])
                                and grid[next_x][next_y] == 1
                            ):
                                grid[next_x][next_y] = 0
                                queue.append((next_x, next_y))
                        


                max_area = max(max_area, curr_area)

        return max_area
