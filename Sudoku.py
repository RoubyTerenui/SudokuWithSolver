from Box import *
#Methode equivalente a l'exploration Backtracking Search
#Heuristique qui doivent etre combiné MRV DEGREE LCV
#Methode qui permet de verifier que l'on utilise une branche qui va aboutir ARC CONSISTENCY
class Sudoku:

    def __init__(self):#Constructor
        self.sudokuList    = []
        self.sudokuToSolve = []

    def read_sudoku_in_line(self, txtPath, sudokuNumber):#Method that read a file where each line is a sudoku and save them in a list
        #open sudoku txt file
        file = open(txtPath, "r")
        #Read all lines of this file
        self.sudokuList = file.readlines()

        #Get the desired sudoku
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

    def printSudoku(self):#A Method that display a sudoku
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
    def init_Possible_Value_Line(self, posX, posY):#Init the constraints  on the line according to the box selected
        if(len(self.sudokuToSolve[posX][posY].possibleValues) == 1):
            return
        for j in range(0, 9):
            if(j != posY):
                if(len(self.sudokuToSolve[posX][j].possibleValues) == 1):
                    #Contraintes Binaires
                    if( self.sudokuToSolve[posX][j].value in self.sudokuToSolve[posX][posY].possibleValues ):#binary constraint
                        self.sudokuToSolve[posX][posY].possibleValues.remove(self.sudokuToSolve[posX][j].value)

        #Position I(ligne) compris entre 0 et 8
        # Position J(colonne) compris entre 0 et 8
    def init_Possible_Value_Column(self, posX, posY):#Init the constraints  on the column according to the box selected
        if(len(self.sudokuToSolve[posX][posY].possibleValues) == 1):
            return
        for i in range(0, 9):
            if(i != posX):
                if(len(self.sudokuToSolve[i][posY].possibleValues) == 1):
                    #Contraintes Binaires
                    if(self.sudokuToSolve[i][posY].value in self.sudokuToSolve[posX][posY].possibleValues):#binary constraint
                        self.sudokuToSolve[posX][posY].possibleValues.remove(self.sudokuToSolve[i][posY].value)

    def init_Possible_Value_Case(self, posX, posY):#Init the constraints  on a 3*3 set of box that depends of the box selected
        if(len(self.sudokuToSolve[posX][posY].possibleValues) == 1):
            return
        numberCaseLine   = (posX // 3)*3#Get the number of the box on a line
        numberCaseColumn = (posY // 3)*3#Get the number of the box on a column
        for i in range(numberCaseLine, numberCaseLine + 3):
            for j in range(numberCaseColumn, numberCaseColumn + 3):
                if(i != posX) or (j != posY):
                    if(len(self.sudokuToSolve[i][j].possibleValues) == 1):
                        #Contraintes Binaires
                        if(self.sudokuToSolve[i][j].value in self.sudokuToSolve[posX][posY].possibleValues):#binary constraint
                            self.sudokuToSolve[posX][posY].possibleValues.remove(self.sudokuToSolve[i][j].value)

    def init_Constraint(self):#Init the constraints on all the box of the sudoku (on creation of the sudoku)
        for i in range(0, 9):
            for j in range(0, 9):
                self.init_Possible_Value_Line(i, j)
                self.init_Possible_Value_Column(i, j)
                self.init_Possible_Value_Case(i, j)

    #Contraintes
    def test_Assignement_Complete(self):#Test if all the box have been assigned
        res = True;
        for i in range(0, 9):
            for j in range(0, 9):
                if (self.sudokuToSolve[i][j].value == 0) :
                    res = False
        return res

    #Heuristiques
        #count the number of possible value for the box X
    def countRemainingValue(self, posX, posY):
        return len(self.sudokuToSolve[posX][posY].possibleValues);

        #count the number of box that will be compelled
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

        #Count the number of constraint that will be created by the assignment of value to the box X
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
    #Method that sort the list possibleValues of the box X using the method Count_Constraint_Created to compare them
    def order_Domain_Values(self, posX, posY):
        # Ordonne les contraintes selon les contraintes qu'elles imposent aux autres
        for i in range(0, len(self.sudokuToSolve[posX][posY].possibleValues)):
            min = i
            for j in range(i, len(self.sudokuToSolve[posX][posY].possibleValues)):
                x = self.count_Constraint_Created(posX,posY,self.sudokuToSolve[posX][posY].possibleValues[j])
                y = self.count_Constraint_Created(posX,posY,self.sudokuToSolve[posX][posY].possibleValues[i])
                if(x<y):
                    min = j
            if(min != i):
                temp=self.sudokuToSolve[posX][posY].possibleValues[min]
                self.sudokuToSolve[posX][posY].possibleValues[min]=self.sudokuToSolve[posX][posY].possibleValues[i]
                self.sudokuToSolve[posX][posY].possibleValues[i]=temp

    #Method backtracking_Search
    def backtracking_Search(self):
        return self.recursive_Backtracking_Search()
    #Method recursive Backtracking_Search
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
                self.aC3()
                result = self.recursive_Backtracking_Search()
                if(result != False):
                    return result
                self.sudokuToSolve[var[1]][var[2]].value = 0
                self.sudokuToSolve[var[1]][var[2]].possibleValues = temp
        return False

    #Method that test if an assignement is consistant or not
    def is_Consistant(self, posX, posY, value):
        numberCaseLine = (posX // 3)*3
        numberCaseColumn = (posY // 3)*3
        for i in range(numberCaseLine, numberCaseLine + 3):
            for j in range(numberCaseColumn, numberCaseColumn + 3):
                if (i != posX) or (j != posY):
                    if (value == self.sudokuToSolve[i][j].value):#binary constraint
                        return False
        for i in range(0, 9):
            if (i != posX):
                if (value == self.sudokuToSolve[i][posY].value):#binary constraint
                    return False
        for j in range(0, 9):
            if (j != posY):
                if (value == self.sudokuToSolve[posX][j].value):#binary constraint
                    return False
        return True

    #Method that select among the unassigned box the "best" choice according to countRemainingValue and countDegreeHeur
    def get_Best_Choice(self):
        heuristiqueList = []
        h = 1
        for i in range(0, 9):
            for j in range(0, 9):
                if(self.sudokuToSolve[i][j].value == 0):
                    heuristiqueList.append([self.countRemainingValue(i, j),i,j])
        self.sort_Heuristique(heuristiqueList)
        tmp = heuristiqueList[0][0]
        if(tmp in heuristiqueList[1:len(heuristiqueList)]):
            while(heuristiqueList[h][0] == tmp):
                h = h + 1
        heuristiqueList2 = heuristiqueList[0:h]
        if(h > 1):
            for i in range(0, len(heuristiqueList2)):
                heuristiqueList2[i][0] = self.countDegreeHeur(heuristiqueList2[i][1],heuristiqueList2[i][2])
            self.sortHeuristique(heuristiqueList2)
            return heuristiqueList2[len(heuristiqueList2) - 1]
        return heuristiqueList2[0]

    #A method that sort a list of the form [[h1,b1,c1][h2,b2,c2]] using the first element of each object (h1)
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
    #A method that remove inconsistent Values
    def remove_Inconsistent_Values(self, box1, box2):
        removed = False
        for x in box1.possibleValues:
            value = False
            for y in box2.possibleValues :
                if(x != y):#binary constraint
                    value = True
            if(value != True):
                removed = True
                box1.possibleValues.remove(x)
        return removed
    #A method that initialize all the arc of a sudoku
    def initialize_queue(self):
        queue = []
        for i in range(0, 9):
            for j in range(0, 9):
                if self.sudokuToSolve[i][j].value == 0:
                    for k in range(0, 9):
                        if i != k:
                            if self.sudokuToSolve[k][j].value == 0:
                                queue.append([i, j, k, j])
                    for h in range(0, 9):
                        if j != h:
                            if self.sudokuToSolve[i][h].value == 0:
                                queue.append([i, j, i, h])
                    numberCaseLine = (i // 3) * 3
                    numberCaseColumn = (j // 3) * 3
                    for k in range(numberCaseLine, numberCaseLine + 3):
                        for h in range(numberCaseColumn, numberCaseColumn + 3):
                            if i != k or j != h:
                                if self.sudokuToSolve[k][h].value == 0:
                                    queue.append([i, j, k, h])
        return queue
    #The AC3 method
    def aC3(self):
        queue=self.initialize_queue()
        while len(queue)!=0:
            [posX1,posY1,posX2,posY2]=queue.pop(0)
            numberCaseLine = (posX1 // 3) * 3
            numberCaseColumn = (posY1 // 3) * 3
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
