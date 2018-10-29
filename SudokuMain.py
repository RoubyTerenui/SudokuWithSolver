from Sudoku import *
from CSP import *
sudoku = Sudoku()
sudoku.read_sudoku_in_line("0.txt",0)
sudoku.printSudoku()

sudoku.init_Constraint()
