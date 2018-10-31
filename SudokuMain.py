from Sudoku import *

sudoku = Sudoku()
sudoku.read_sudoku_in_line("0.txt",0)
sudoku.printSudoku()

print('')
L = [[2,3,4],[1,4,3],[3,4,4],[0,3,5]]
sudoku.sort_Heuristique(L)
print(L)
print('')
sudoku.init_Constraint()
print(sudoku.countRemainingValue(0,0))
print('')
print(sudoku.sudokuToSolve[0][1].possibleValues)
print(sudoku.sudokuToSolve[2][1].possibleValues)
print(sudoku.sudokuToSolve[2][2].possibleValues)
print(sudoku.sudokuToSolve[4][0].possibleValues)
print(sudoku.sudokuToSolve[7][0].possibleValues)
print(sudoku.sudokuToSolve[0][4].possibleValues)
print(sudoku.sudokuToSolve[0][5].possibleValues)
print(sudoku.sudokuToSolve[0][7].possibleValues)
print('')
print(sudoku.count_Constraint_Created(0,0,))
