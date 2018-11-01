from Sudoku import *

sudoku = Sudoku()
sudoku.read_sudoku_in_line("0.txt",2)
sudoku.printSudoku()
sudoku.backtracking_Search()
print("______________________________________________________________________________________")
sudoku.printSudoku()