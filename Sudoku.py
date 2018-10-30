from Box import *
#Methode equivalente a l'exploration Backtracking Search
#Heuristique qui doivent etre combiné MRV DEGREE LCV
#Methode qui permet de verifier que l'on utilise une branche qui va aboutir ARC CONSISTENCY
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
                    if( self.sudokuToSolve[posX][j].value in self.sudokuToSolve[posX][posY].possibleValues ):#Contraintes Binaires
                        self.sudokuToSolve[posX][posY].possibleValues.remove(self.sudokuToSolve[posX][j].value)

    def init_Possible_Value_Column(self, posX, posY):#Position I(ligne) compris entre 0 et 8 # Position J(colonne) compris entre 0 et 8
        if(len(self.sudokuToSolve[posX][posY].possibleValues) == 1):
            return
        for i in range(0, 9):
            if i!=posX :
                if(len(self.sudokuToSolve[i][posY].possibleValues) == 1):
                    if(self.sudokuToSolve[i][posY].value in self.sudokuToSolve[posX][posY].possibleValues):#Contraintes Binaires
                        self.sudokuToSolve[posX][posY].possibleValues.remove(self.sudokuToSolve[i][posY].value)

    def init_Possible_Value_Case(self, posX, posY):
        if(len(self.sudokuToSolve[posX][posY].possibleValues) == 1):
            return
        numberCaseLine   = posX%3
        numberCaseColumn = posY%3
        for i in range(numberCaseLine, numberCaseLine+3):
            for j in range(numberCaseColumn, numberCaseColumn+3):
                if(i != posX) or (j != posY):
                    if(len(self.sudokuToSolve[i][j].possibleValues) == 1):
                        if(self.sudokuToSolve[i][j].value in self.sudokuToSolve[posX][posY].possibleValues):#Contraintes Binaires
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


    #Contraintes
    def test_Assignement_Complete(self, assignment):
        res = False;
        if(len(assignment) == len(self.sudokuToSolve)):
            res = True
            for i in range(0, len(assignment)):
                if(len(assignment[0]) != len(self.sudokuToSolve[0])):
                    res = False
        return res

    #Heuristiques
    def countRemainingValue(self, posX, posY):#compte le nombre de valeurs restantes pour X
        return len(self.sudokuToSolve[posX][posY].possibleValues);

    def countDegreeHeur(self, posX, posY):#compte le nombre de case contrainte par l'assignement de X
        res              = 0
        numberCaseLine   = posX % 3
        numberCaseColumn = posY % 3
        for i in range(numberCaseLine, numberCaseLine + 3):
            for j in range(numberCaseColumn, numberCaseColumn + 3):
                if(i != posX) or (j != posY):
                    if(len(self.sudokuToSolve[i][j].possibleValues) != 1):
                        res = res + 1
        for i in range(0, 9):
            if(i != posX):
                if(len(self.sudokuToSolve[i][posY].possibleValues) != 1):
                    res = res + 1
        for j in range(0, 9):
            if(j != posY):
                if(len(self.sudokuToSolve[posX][j].possibleValues) == 1):
                    res = res + 1
        return res

    def countConstraintCreated(self, posX, posY, value):#Compte combien de contraintes vont être crée si l'on assigne une valeur value à X
        res              = 0
        numberCaseLine   = posX % 3
        numberCaseColumn = posY % 3
        for i in range(numberCaseLine, numberCaseLine + 3):
            for j in range(numberCaseColumn, numberCaseColumn + 3):
                if(i != posX) or(j != posY):
                    if (len(self.sudokuToSolve[i][j].possibleValues) != 1):
                        res = res + len(self.sudokuToSolve[i][j].possibleValues)
                        if (value in self.sudokuToSolve[i][j].possibleValues):
                            res = res - 1
                    else:
                        if (value in self.sudokuToSolve[i][j].possibleValues):
                            return 0
        for i in range(0, 9):
            if(i != posX):
                if(len(self.sudokuToSolve[i][posY].possibleValues) != 1):
                    res = res + len(self.sudokuToSolve[i][j].possibleValues)
                    if (value in self.sudokuToSolve[i][posY].possibleValues):
                        res = res - 1
                else:
                    if (value in self.sudokuToSolve[i][j].possibleValues):
                        return 0
        for j in range(0, 9):
            if(j != posY):
                if(len(self.sudokuToSolve[posX][j].possibleValues) == 1):
                    res = res + len(self.sudokuToSolve[i][j].possibleValues)
                    if (value in self.sudokuToSolve[posX][j].possibleValues):
                        res = res - 1
                else:
                    if(value in self.sudokuToSolve[i][j].possibleValues):
                        return 0
        return res

    def OrderDomainValues(self,posX,posY):# Ordonne les contraintes selon les contraintes qu'elles imposent aux autres
        for i in range(0, len(self.sudokuToSolve[posX][posY].possibleValues)):
            min = i
            for j in range(i, len(self.sudokuToSolve[posX][posY].possibleValues)):
                x = self.countConstraintCreated(self,posX,posY,self.sudokuToSolve[posX][posY].possibleValues[j])
                y = self.countConstraintCreated(self,posX,posY,self.sudokuToSolve[posX][posY].possibleValues[i])
                if(x<y):
                    min = j
            if(min != i):
                temp=self.sudokuToSolve[posX][posY].possibleValues[min]
                self.sudokuToSolve[posX][posY].possibleValues[min]=self.sudokuToSolve[posX][posY].possibleValues[i]
                self.sudokuToSolve[posX][posY].possibleValues[i]=temp

    #Backtracking Search
        #def recursive_Backtracking_Search(self,assignement):
            #if assignement is complete :
                #return assignement
            #var=Select_UnassignedVariable(Variable(self),assignement,self)
            #for each value in in Order Domain Values(var,assignement,self) faire:
                #if value is consistent with assigment selon les contraintes(self) alors:
                    #add var a assigment
                    #result=recursiveBacktracking(assignement,csp)
                    #if result != failure :#
                        # return result
                    #remove value from assignement
            #return failure


        #def backtracking_Search(self):
         #   return recursive_Backtracking_Search(self,[])

#AC-3
    def remove_Inconsistent_Values(self, box1, box2):
        removed = False
        for x in box1.possibleValues:
            value = False
            for y in box2.possibleValues :
                if(x != y):
                    value = True
            if(value != True):
                removed = True
                box1.possibleValues.remove(x)
        return removed

    def aC3(self):
        queue=[]
