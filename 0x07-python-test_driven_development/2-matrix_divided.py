"""
Module does various operations on matrices
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of matrice
    by a value div
    """
    counter = 0
    verify = []
    for i in matrix:
        for j in i:
            try:
                counter += 1
                if type(j) not in [int, float]:
                    raise TypeError
            except TypeError:
                print("matrix must be a matrix (list of lists) of " +
                      "integers/floats")
        try:
            if counter not in verify and len(verify) > 0:
                raise TypeError
            else:
                verify.append(counter)
            counter = 0
        except TypeError:
            print("Each row of the matrix must have the same size")
    try:
        if type(div) not in [int, float]:
            raise TypeError
        if div == 0:
            raise ZeroDivisionError
    except TypeError:
        print("div must be a number")
    except ZeroDivisionError:
        print("division by zero")
    try:
        return [[int(j/2) for j in i] for i in matrix]
    except (TypeError, ZeroDivisionError):
        return
