from Box import *
class Sudoku:

    def __init__(self):
        self.sudokuList    = []
        self.sudokuToSolve = []


    def read_sudoku_in_line(self, txtPath, sudokuNumber):
        #open sudoku txt file
        file = open(txtPath, "r")
        #Read all lines of this file
        self.sudokuList = file.readlines()

        #Get the disired sudoku
        sudokuInLine    = self.sudokuList[sudokuNumber]
        i = 0
        while(i < len(sudokuInLine)-1):
            sudokuTmp = []
            for j in range(0, 9):
                if(sudokuInLine[i+j] != ""):
                    box = Box(((int)(sudokuInLine[i+j])))
                    #box.val
                    sudokuTmp.append(box)
            self.sudokuToSolve.append(sudokuTmp)
            i = i + 9
        file.close()
        return self.sudokuToSolve

    def init_Possible_Value_Line(self, posX, posY):#Position I(ligne) compris entre 0 et 8 # Position J(Column) compris entre 0 et 8
        if( len(self.sudokuToSolve[posX][posY].possibleValues) == 1 ):
            return
        for j in range(0, 9):
            if(j != posY):
                if( len(self.sudokuToSolve[posX][j].possibleValues) == 1):
                    if( self.sudokuToSolve[posX][j].value in self.sudokuToSolve[posX][posY].possibleValues ):
                        self.sudokuToSolve[posX][posY].possibleValues.remove(self.sudokuToSolve[posX][j].value)

    def init_Possible_Value_Column(self, posX, posY):#Position I(ligne) compris entre 0 et 8 # Position J(colonne) compris entre 0 et 8
        if(len(self.sudokuToSolve[posX][posY].possibleValues) == 1):
            return
        for i in range(0, 9):
            if i!=posX :
                if(len(self.sudokuToSolve[i][posY].possibleValues) == 1):
                    if(self.sudokuToSolve[i][posY].value in self.sudokuToSolve[posX][posY].possibleValues):
                        self.sudokuToSolve[posX][posY].possibleValues.remove(self.sudokuToSolve[i][posY].value)

    def init_Possible_Value_Case(self, posX, posY):
        if(len(self.sudokuToSolve[posX][posY].possibleValues) == 1):
            return
        numberCaseLine   = posX%3
        numberCaseColumn = posY%3
        for i in range(numberCaseLine, numberCaseLine+3):
            for j in range(numberCaseColumn, numberCaseColumn+3):
                if(i != posX):
                    if(len(self.sudokuToSolve[i][j].possibleValues) == 1):
                        if(self.sudokuToSolve[i][j].value in self.sudokuToSolve[posX][posY].possibleValues):
                            self.sudokuToSolve[posX][posY].possibleValues.remove(self.sudokuToSolve[i][j].value)

    def init_Constraint(self):
        for i in range(0, 9):
            for j in range(0, 9):
                self.init_Possible_Value_Line(i, j)
                self.init_Possible_Value_Column(i, j)
                self.init_Possible_Value_Case(i, j)

    def printSudoku(self):
        for i in self.sudokuToSolve:
            print('|', end='')
            for j in i:
                if(j.value == 0):
                    print(' ', end='|')
                else:
                    print(j.value, end='|')
            print('')
