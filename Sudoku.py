from Box import *
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
        sudokuInLine   = self.sudokuList[sudokuNumber]
        i = 0
        while(i < len(sudokuInLine)-1):
            sudokuTmp = []
            for j in range(0,9):
                if (sudokuInLine[i+j])!="":
                    box = Box(((int)(sudokuInLine[i+j])))
                    #box.val
                    sudokuTmp.append(box)
            #sudokuTmp.append(sudokuInLine[i:i+9])
            self.sudokuToSolve.append(sudokuTmp)
            i = i + 9
        #delete the last element
        #del self.sudokuToSolve[len(self.sudokuToSolve) - 1]
        file.close()
        return self.sudokuToSolve

    def init_Possible_Value_Box(self,positionI,positionJ):#Position I(ligne) compris entre 0 et 8 # Position J(colonne) compris entre 0 et 8
        if self.sudokuToSolve[positionI][positionJ].possibleValues.length()==1:
            return
        for j in range (0,9):
            if j!=positionJ :
                if  self.sudokuToSolve[positionI][j].possibleValues.length()==1:
                    if self.sudokuToSolve[positionI][j].values in self.sudokuToSolve[positionI][positionJ].possibleValues :
                        self.sudokuToSolve[positionI][positionJ].possibleValues.remove(self.sudokuToSolve[positionI][j].values)

    def printSudoku(self):
        for i in self.sudokuToSolve:
            for j in i:
                print(j.value)
