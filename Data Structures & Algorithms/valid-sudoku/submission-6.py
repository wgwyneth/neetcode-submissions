class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            rowUnique = {}
            for element in row:
                if element in rowUnique and element != ".":
                    return False
                else:
                    rowUnique[element] = 1
        
        for columnI in range(len(board) - 1):
            columnUnique = {}
            for elementI in range(len(board) - 1):
                element = board[elementI][columnI]
                if element in columnUnique and element != ".":
                    return False
                else:
                    columnUnique[element] = 1
        
        for square in range(9):
            squareUnique = {}
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j

                    element = board[row][col]
                    if element in squareUnique and element != ".":
                        return False
                    else:
                        squareUnique[element] = 1
        

        return True

