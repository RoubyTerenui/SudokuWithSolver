def read_sudoku_in_line(txtPath, sudokuNumber):
    #open sudoku txt file
    file = open(txtPath, "r")

    #Read all lines of this file
    sudokuList = file.readlines()

    #Get the disired sudoku
    sudokuInLine    = sudokuList[sudokuNumber]
    sudokuToSolve   = []
    i = 0
    while(i < len(sudokuInLine)):
        sudokuTmp = []
        sudokuTmp.append(sudokuInLine[i:i+9])
        sudokuToSolve.append(sudokuTmp)
        i = i + 9

    #delete the last element
    del sudokuToSolve[len(sudokuToSolve) - 1]
    print(sudokuToSolve)
    file.close()
    return sudokuToSolve

def is_line_valide(sudoku):
    response = False


List = read_sudoku_in_line("0.txt",0)
