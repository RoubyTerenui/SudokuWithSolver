class Box : #Class that defines a box of a sudoku
    def __init__(self,value):
        self.value = value
        if value==0 :
            self.possibleValues=[1,2,3,4,5,6,7,8,9]#if the box is unassigned all the possible values for the box(without the constraints)
        else:
            self.possibleValues=[value]#if the box is alread assigned only 1 possible value
