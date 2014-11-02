#!/usr/bin/env python
"""
utils functions to read and write of sudoku file

sample sudoku:

0,3,5,2,9,0,8,6,4
0,8,2,4,1,0,7,0,3
7,6,4,3,8,0,0,9,0
2,1,8,7,3,9,0,4,0
0,0,0,8,0,4,2,3,0
0,4,3,0,5,2,9,7,0
4,0,6,5,7,1,0,0,9
3,5,9,0,2,8,4,1,7
8,0,0,9,0,0,5,2,6

"""

import os


def read_sudoku(sudoku_file):
    """
    assume sudoku is stored in a file. sudoku_file is a
    path or filename to that file.

    """
    sudoku = []

    if not sudoku_file or not os.path.exists(sudoku_file):
        raise Exception('Invalid Sudoku file')

    with open(sudoku_file, 'rb') as file:
        for sudoku_line in file:
            if sudoku_file:
                sudoku_line = sudoku_line.strip()
                sudoku_line = sudoku_line.split(',')
                sudoku.append(sudoku_line)

    return sudoku


def write_sudoku(sudoku, sudoku_file):
    """
    write 2D array of sudoku into a file, named from sudoku_file

    """
    with open(sudoku_file, 'wb') as file:
        for r in sudoku:
            file.write('%s\n' % ','.join(r))
