from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows, cols, boxes = self.calculateBitmasks(board)
        self.solveRecursion(board, rows, cols, boxes)

    def solveRecursion(
        self, board: List[List[str]], rows: List[int], cols: List[int], boxes: List[int]
    ) -> bool:
        row, col = self.findMostConstained(board, rows, cols, boxes)
        if row == -1:
            return True

        for n in range(1, 10):
            bit = 1 << n
            index = (row // 3) * 3 + (col // 3)

            if not (rows[row] & bit or cols[col] & bit or boxes[index] & bit):
                board[row][col] = str(n)
                rows[row] |= bit
                cols[col] |= bit
                boxes[index] |= bit

                if self.solveRecursion(board, rows, cols, boxes):
                    return True

                board[row][col] = "."
                rows[row] &= ~bit
                cols[col] &= ~bit
                boxes[index] &= ~bit

        return False

    def findMostConstained(
        self, board: List[List[str]], rows: List[int], cols: List[int], boxes: List[int]
    ) -> (int, int):
        minNumbers = 10
        minCell = (-1, -1)
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    continue

                count = 0
                for n in range(1, 10):
                    bit = 1 << n
                    index = (row // 3) * 3 + (col // 3)

                    if not (rows[row] & bit or cols[col] & bit or boxes[index] & bit):
                        count += 1

                if minNumbers > count:
                    minNumbers = count
                    minCell = (row, col)
        return minCell

    def calculateBitmasks(
        self, board: List[List[str]]
    ) -> (List[int], List[int], List[int]):
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    n = 1 << int(board[row][col])
                    index = (row // 3) * 3 + (col // 3)
                    rows[row] |= n
                    cols[col] |= n
                    boxes[index] |= n

        return (rows, cols, boxes)


def main():
    board = [
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "9", ".", ".", "1", ".", ".", "3", "."],
        [".", ".", "6", ".", "2", ".", "7", ".", "."],
        [".", ".", ".", "3", ".", "4", ".", ".", "."],
        ["2", "1", ".", ".", ".", ".", ".", "9", "8"],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "2", "5", ".", "6", "4", ".", "."],
        [".", "8", ".", ".", ".", ".", ".", "1", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]
    # board = [
    #     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    #     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #     [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #     [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    # ]

    solution = Solution()
    solution.solveSudoku(board)
    print(board)


if __name__ == "__main__":
    main()
