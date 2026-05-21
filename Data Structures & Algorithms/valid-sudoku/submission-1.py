class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        boxes = [set() for i in range(9)] 

        for x in range(9):
            for y in range(9):
                num = board[x][y]
                if num != ".":
                    boxNum = (x // 3) * 3 + (y // 3)
                    if num in rows[x] or num in columns[y] or num in boxes[boxNum]:
                        return False
                    rows[x].add(num)
                    columns[y].add(num)
                    boxes[boxNum].add(num)

        return True