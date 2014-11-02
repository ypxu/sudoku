#!/usr/bin/env python
"""
Sudoku Solver in Python

Usage:
    solver.py solve [--input=<input>] [--output=<output>]
    solver.py print [--input=<input>]

Options:
    -h --help       Show help message
    -v --version    Show version
"""

from __future__ import print_function
from docopt import docopt
from sudoku_py import __version__
from sudoku_py import utils
from sudoku_py.solver import SudokuSolver


if __name__ == '__main__':

    args = docopt(__doc__, version = __version__)

    print_cmd = args['print']
    solve_cmd = args['solve']
    input_file = args['--input'] or 'sudoku.csv'
    output_file = args['--output'] or 'solution.csv'

    sudoku = utils.read_sudoku(input_file)

    if not sudoku:
        print("Can't read input file for Sudoku Solver")
        sys.exit(1)

    if print_cmd:
        for r in sudoku:
            print(','.join(r))
    elif solve_cmd:
        SudokuSolver(sudoku).solve()
        utils.write_sudoku(sudoku, output_file)
