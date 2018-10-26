from Sudoku import *

sudoku = Sudoku()
sudoku.read_sudoku_in_line("0.txt",0)
sudoku.printSudoku()

sudoku.init_Constraint()
print(sudoku.sudokuToSolve[0][0].possibleValues)
print(sudoku.sudokuToSolve[0][2].possibleValues)
