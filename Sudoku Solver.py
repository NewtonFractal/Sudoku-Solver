import time
import numpy

def Cell_Solver(Sudoku,Cell_Number):
    Number_list = []
    y_coordinate = []
    x_coordinate = []
    for x in range(1*Cell_Number-1,3*Cell_Number):
        for y in range(1*Cell_Number-1,3*Cell_Number):
            if Sudoku[y,x] != 0:
                Number_list.append(Sudoku[y,x])
                x_coordinate.append(x)
                y_coordinate.append(y)
    for z in range(1,10):
        if z not in Number_list:
            for x in range(1 * Cell_Number - 1, 3 * Cell_Number):
                for y in range(1 * Cell_Number - 1, 3 * Cell_Number):
                    if Sudoku[y, x] == 0:
                        for x in range(x,10):
                            if Sudoku[y,x] != z:

def Sudoku_solver(Sudoku):
    Cell_Number = 1
    for x in range(0,3):
        for y in range(0,3):
            Cell_Solver(Sudoku,Cell_Number)

matrix = numpy.array([[0,0,3,0,2,0,6,0,0],
                      [9,0,0,3,0,5,0,0,1],
                      [0,0,1,8,0,6,4,0,0],
                      [0,0,8,1,0,2,9,0,0],
                      [7,0,0,0,0,0,0,0,8],
                      [0,0,6,7,0,8,2,0,0],
                      [0,0,2,6,0,9,5,0,0],
                      [8,0,0,2,0,3,0,0,9],
                      [0,0,5,0,1,0,3,0,0],])

Sudoku_solver(matrix)

print(matrix)