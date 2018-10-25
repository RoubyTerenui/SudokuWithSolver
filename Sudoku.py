def readSudoku(txtPath, sudokuNumber):
    file = open(txtPath, "r")
    sudokuList = file.readlines()
    sudokuInLine = sudokuList[sudokuNumber]
    sudokuToSolve = [];
    for i in range(0,9):
        sudokuTmp = []
        for j in range (0,9):
            sudokuTmp.append(sudokuInLine[j])
            sudokuToSolve.append(sudokuTmp)
    print(sudokuToSolve)
    print(len(sudokuToSolve))
    file.close()

readSudoku("0.txt",0)
