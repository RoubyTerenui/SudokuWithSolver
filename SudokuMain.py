from Sudoku import *

sudoku = Sudoku()
sudoku.read_sudoku_in_line("0.txt",0)
sudoku.printSudoku()
sudoku.init_Constraint()

print(sudoku.countDegreeHeur(0,1))
print(sudoku.countDegreeHeur(8,6))
print(sudoku.countDegreeHeur(7,0))
print(sudoku.countDegreeHeur(3,2))
