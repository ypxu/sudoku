"""
Sudoku Solver Module

Using backtracking to solve sudoku.

rowChecker, columnChecker and sudokuChecker for validating
each row, column and sub-sudoku.

"""

class SudokuSolver(object):

    sudokuSize = 9
    rowChecker = columnChecker = sudokuChecker = None

    def __init__(self, sudoku):
        self.rowChecker = []
        self.columnChecker = []
        self.sudokuChecker = []

        for s in xrange(self.sudokuSize):
            self.rowChecker.append([False] * 10)
            self.columnChecker.append([False] * 10)
            self.sudokuChecker.append([False] * 10)

        self.sudoku = sudoku

    def solve(self):

        for i in xrange(self.sudokuSize):
            for j in xrange(self.sudokuSize):
                self.fillChecker(i, j, self.sudoku[i][j])

        self._solve(0)
        return self.sudoku

    def _solve(self, index):
        if index >= self.sudokuSize ** 2:
            return True

        i, j = index / 9, index % 9

        if self.sudoku[i][j] != '0':
            return self._solve(index + 1)

        for val in xrange(1, 10):
            val = str(val)
            if self.isValid(i, j, val):
                self.sudoku[i][j] = val
                self.fillChecker(i, j, val)
                if self._solve(index + 1):
                    return True
                self.clearChecker(i, j, val)
        # Reset when can't find valid solutions
        self.sudoku[i][j] = '0'
        return False

    def isValid(self, i, j, val):
        if val == '0':
            return False
        if (not self.rowChecker[i][int(val)] and
            not self.columnChecker[j][int(val)] and
            not self.sudokuChecker[3 * (i / 3) + j / 3][int(val)]):
            return True
        return False

    def fillChecker(self, i, j, val):
        if val == '0':
            return
        self.rowChecker[i][int(val)] = True
        self.columnChecker[j][int(val)] = True
        self.sudokuChecker[3 * (i / 3) + j / 3][int(val)] = True

    def clearChecker(self, i, j, val):
        if val == '0':
            return
        self.rowChecker[i][int(val)] = False
        self.columnChecker[j][int(val)] = False
        self.sudokuChecker[3 * (i / 3) + j / 3][int(val)] = False
