class Sudoku:

    def __init__(self):
        self.sudokuList = []
        self.sudokuToSolve = []

    def read_sudoku_in_line(self, txtPath, sudokuNumber):
        #open sudoku txt file
        file = open(txtPath, "r")

        #Read all lines of this file
        self.sudokuList = file.readlines()

        #Get the disired sudoku
        sudokuInLine    = self.sudokuList[sudokuNumber]
        i = 0
        while(i < len(sudokuInLine)):
            sudokuTmp = []
            sudokuTmp.append(sudokuInLine[i:i+9])
            self.sudokuToSolve.append(sudokuTmp)
            i = i + 9

        #delete the last element
        del self.sudokuToSolve[len(self.sudokuToSolve) - 1]
        file.close()
        return self.sudokuToSolve
