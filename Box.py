class Box : #Class that defines a box of a sudoku
    def __init__(self,value):
        self.value = value
        if value==0 :
            self.possibleValues=[1,2,3,4,5,6,7,8,9]
        else:
            self.possibleValues=[value]
