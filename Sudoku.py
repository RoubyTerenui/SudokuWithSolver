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

    def printSudoku(self):
        for i in self.sudokuToSolve:
            print('|', end='')
            for j in i:
                if(j.value == 0):
                    print(' ', end='|')
                else:
                    print(j.value, end='|')
            print('')

        #Position I(ligne) compris entre 0 et 8
        #Position J(Column) compris entre 0 et 8
    def init_Possible_Value_Line(self, posX, posY):
        if(len(self.sudokuToSolve[posX][posY].possibleValues) == 1):
            return
        for j in range(0, 9):
            if(j != posY):
                if(len(self.sudokuToSolve[posX][j].possibleValues) == 1):
                    #Contraintes Binaires
                    if( self.sudokuToSolve[posX][j].value in self.sudokuToSolve[posX][posY].possibleValues ):
                        self.sudokuToSolve[posX][posY].possibleValues.remove(self.sudokuToSolve[posX][j].value)

        #Position I(ligne) compris entre 0 et 8
        # Position J(colonne) compris entre 0 et 8
    def init_Possible_Value_Column(self, posX, posY):
        if(len(self.sudokuToSolve[posX][posY].possibleValues) == 1):
            return
        for i in range(0, 9):
            if(i != posX):
                if(len(self.sudokuToSolve[i][posY].possibleValues) == 1):
                    #Contraintes Binaires
                    if(self.sudokuToSolve[i][posY].value in self.sudokuToSolve[posX][posY].possibleValues):
                        self.sudokuToSolve[posX][posY].possibleValues.remove(self.sudokuToSolve[i][posY].value)

    def init_Possible_Value_Case(self, posX, posY):
        if(len(self.sudokuToSolve[posX][posY].possibleValues) == 1):
            return
        numberCaseLine   = (posX // 3)*3
        numberCaseColumn = (posY // 3)*3
        for i in range(numberCaseLine, numberCaseLine + 3):
            for j in range(numberCaseColumn, numberCaseColumn + 3):
                if(i != posX) or (j != posY):
                    if(len(self.sudokuToSolve[i][j].possibleValues) == 1):
                        #Contraintes Binaires
                        if(self.sudokuToSolve[i][j].value in self.sudokuToSolve[posX][posY].possibleValues):
                            self.sudokuToSolve[posX][posY].possibleValues.remove(self.sudokuToSolve[i][j].value)

    def init_Constraint(self):
        for i in range(0, 9):
            for j in range(0, 9):
                self.init_Possible_Value_Line(i, j)
                self.init_Possible_Value_Column(i, j)
                self.init_Possible_Value_Case(i, j)

    #Contraintes
    def test_Assignement_Complete(self):
        res = True;
        for i in range(0, 9):
            for j in range(0, 9):
                if (self.sudokuToSolve[i][j].value == 0) :
                    res = False
        return res

    #Heuristiques
        #compte le nombre de valeurs restantes pour X
    def countRemainingValue(self, posX, posY):
        return len(self.sudokuToSolve[posX][posY].possibleValues);

        #compte le nombre de case contrainte par l'assignement de X
    def countDegreeHeur(self, posX, posY):
        res              = 0
        numberCaseLine   = (posX // 3)*3
        numberCaseColumn = (posY // 3)*3
        for i in range(numberCaseLine, numberCaseLine + 3):
            for j in range(numberCaseColumn, numberCaseColumn + 3):
                if(i != posX) or (j != posY):
                    if(self.sudokuToSolve[i][j].value != 0):
                        res = res + 1
        for k in range(0, 9):
            if(k != posX):
                if(self.sudokuToSolve[k][posY].value != 0):
                    res = res + 1
        for h in range(0, 9):
            if(h != posY):
                if(self.sudokuToSolve[posX][h].value != 0):
                    res = res + 1
        return res

        #Compte combien de contraintes vont être crée si l'on assigne une valeur value à X
    def count_Constraint_Created(self, posX, posY, value):
        res              = 0
        numberCaseLine   = (posX // 3)*3
        numberCaseColumn = (posY // 3)*3
        for i in range(numberCaseLine, numberCaseLine + 3):
            for j in range(numberCaseColumn, numberCaseColumn + 3):
                if(i != posX) or(j != posY):
                    if(self.sudokuToSolve[i][j].value == 0):
                        res = res + len(self.sudokuToSolve[i][j].possibleValues)
                        if(value in self.sudokuToSolve[i][j].possibleValues):
                            res = res - 1
                    else:
                        if(value in self.sudokuToSolve[i][j].possibleValues):
                            return 0
        for i in range(0, 9):
            if(i != posX):
                if(self.sudokuToSolve[i][posY].value == 0):
                    res = res + len(self.sudokuToSolve[i][posY].possibleValues)
                    if(value in self.sudokuToSolve[i][posY].possibleValues):
                        res = res - 1
                else:
                    if(value in self.sudokuToSolve[i][posY].possibleValues):
                        return 0
        for j in range(0, 9):
            if(j != posY):
                if(self.sudokuToSolve[posX][j].value == 0):
                    res = res + len(self.sudokuToSolve[posX][j].possibleValues)
                    if(value in self.sudokuToSolve[posX][j].possibleValues):
                        res = res - 1
                else:
                    if(value in self.sudokuToSolve[posX][j].possibleValues):
                        return 0
        return res

    def order_Domain_Values(self, posX, posY):
        # Ordonne les contraintes selon les contraintes qu'elles imposent aux autres
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

    def backtracking_Search(self):
        return recursive_Backtracking_Search([])

    def recursive_Backtracking_Search(self):
        if(self.test_Assignement_Complete()):
            return True
        var = self.get_Best_Choice()
        self.order_Domain_Values(var[1], var[2])
        for value in self.sudokuToSolve[var[1]][var[2]].possibleValues:
            if(self.is_Consistant(var[1], var[2], value)):
                temp = self.sudokuToSolve[var[1]][var[2]].possibleValues
                self.sudokuToSolve[var[1]][var[2]].value = value
                self.sudokuToSolve[var[1]][var[2]].possibleValues = [value]
                result = self.recursive_Backtracking_Search()
                if(result != False):
                    return result
                self.sudokuToSolve[var[1]][var[2]].value = 0
                self.sudokuToSolve[var[1]][var[2]].possibleValues = temp
        return False


    def is_Consistant(self, posX, posY, value):
        numberCaseLine = (posX // 3)*3
        numberCaseColumn = (posY // 3)*3
        for i in range(numberCaseLine, numberCaseLine + 3):
            for j in range(numberCaseColumn, numberCaseColumn + 3):
                if (i != posX) or (j != posY):
                    if (value == self.sudokuToSolve[i][j].value):
                        return False
        for i in range(0, 9):
            if (i != posX):
                if (value == self.sudokuToSolve[i][posY].value):
                    return False
        for j in range(0, 9):
            if (j != posY):
                if (value == self.sudokuToSolve[posX][j].value):
                    return False
        return True

    def get_Best_Choice(self):
        heuristiqueList = []
        h = 1
        for i in range(0, 9):
            for j in range(0, 9):
                if(self.sudokuToSolve[i][j].value == 0):
                    heuristiqueList.append(self.countRemainingValue(i, j))
        self.sortHeuristique(heuristiqueList)
        tmp = heuristiqueList[0][0]
        while(heuristiqueList[h][0] == tmp):
            h = h + 1
        heuristiqueList2 = heuristiqueList[0:h]
        if(h > 1):
            for i in range(0, len(heuristiqueList2)):
                heuristiqueList2[i][0] = self.countDegreeHeur(heuristiqueList2[i][1],heuristiqueList2[i][2])
            self.sortHeuristique(heuristiqueList2)
            return heuristiqueList2[len(heuristiqueList2) - 1]
        return heuristiqueList2

    def sort_Heuristique(self, list):
        for i in range(0, len(list)):
            min = i
            for j in range(i, len(list)):
                x = list[j][0]
                y = list[i][0]
                if(x<y):
                    min = j
            if(min != i):
                temp = list[min][0]
                list[min][0] = list[i][0]
                list[i][0] = temp

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
        queue = []
        for i in range(0, 9):
            for j in range(0, 9):
                if self.sudokuToSolve[i][j].value==0:
                    for k in range(0, 9):
                        if i != k:
                            if self.sudokuToSolve[k][j].value == 0:
                                queue.append([i, j, k, j])
                    for h in range(0, 9):
                        if j != h:
                            if self.sudokuToSolve[i][h].value == 0:
                                queue.append([i, j, i, h])
                    numberCaseLine = (i // 3)*3
                    numberCaseColumn = (j // 3)*3
                    for k in range(numberCaseLine, numberCaseLine + 3):
                        for h in range(numberCaseColumn, numberCaseColumn + 3):
                            if i!=k or j!=h :
                                 if self.sudokuToSolve[k][h].value==0:
                                      queue.append([i,j,k,h])
        while len(queue)!=0:
            [posX1,posY1,posX2,posY2]=queue.pop(0)
            if self.remove_Inconsistent_Values(self.sudokuToSolve[posX1][posY1],self.sudokuToSolve[posX2][posY2]):
                #neighbors
                for k in range(0, 9):
                    if posX1 != k:
                        if self.sudokuToSolve[k][posY1].value == 0:
                            queue.append([k, posY1, posX1, posY1])
                for h in range(0, 9):
                    if posY1 != h:
                        if self.sudokuToSolve[posX1][h].value == 0:
                            queue.append([posX1, h, posX1, posY1])
                for k in range(numberCaseLine, numberCaseLine + 3):
                    for h in range(numberCaseColumn, numberCaseColumn + 3):
                        if posX1 != k or posY1 != h:
                            if self.sudokuToSolve[k][h].value == 0:
                                queue.append([k, h, posX1, posY1])
