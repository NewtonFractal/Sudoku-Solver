import time
import numpy


def Cell_Solver(Sudoku, numbers, y_coordinates, x_coordinates):
    for z in range(0, len(y_coordinates)):
        for x in numbers:
            change = True
            a = Sudoku[x_coordinates[z], y_coordinates[z]]
            for a in range(x_coordinates[z], 9):
                if Sudoku[a, y_coordinates[z]] == x:
                    change = False
                    break
                print(Sudoku[a, y_coordinates[z]])
            for a in range(x_coordinates[z], 0, -1):
                if Sudoku[a, y_coordinates[z]] == x:
                    change = False
                    break
            for a in range(y_coordinates[z], 9):
                if Sudoku[x_coordinates[z], a] == x:
                    change = False
                    print("Nope")
                    break
                print(Sudoku[x_coordinates[z], a])
            if change == True:
                Sudoku[x_coordinates[z],y_coordinates[z]] = x
                numbers.remove(x)
                break


def number_generator(numbers_left, zero_coordinates_y, zero_coordinates_x):
    for x in range(0, 3):
        for y in range(0, 3):
            if matrix[x, y] != 0:
                numbers_left.remove(matrix[x, y])
            else:
                zero_coordinates_x.append(x)
                zero_coordinates_y.append(y)
    return numbers_left, zero_coordinates_y, zero_coordinates_x


def Sudoku_solver(Sudoku):
    numbers_left = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    zero_coordinates_y = []
    zero_coordinates_x = []
    numbers_left, zero_coordinates_y, zero_coordinates_x = number_generator(numbers_left, zero_coordinates_y,
                                                                            zero_coordinates_x)
    Cell_Solver(Sudoku, numbers_left, zero_coordinates_y, zero_coordinates_x)


matrix = numpy.array([[0, 0, 3, 0, 2, 0, 6, 0, 0],
                      [9, 0, 0, 3, 0, 5, 0, 0, 1],
                      [0, 0, 1, 8, 0, 6, 4, 0, 0],
                      [0, 0, 8, 1, 0, 2, 9, 0, 0],
                      [7, 0, 0, 0, 0, 0, 0, 0, 8],
                      [0, 0, 6, 7, 0, 8, 2, 0, 0],
                      [0, 0, 2, 6, 0, 9, 5, 0, 0],
                      [8, 0, 0, 2, 0, 3, 0, 0, 9],
                      [0, 0, 5, 0, 1, 0, 3, 0, 0], ])

Sudoku_solver(matrix)
