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
    try:
        for i in matrix:
            for j in i:
                counter += 1
            if counter not in verify and len(verify) > 0:
                raise TypeError
            else:
                verify.append(counter)
                counter = 0
    except TypeError:
        print("Each row of the matrix must have the same size")
    for i in matrix:
        for j in i:
            try:
                if type(j) not in [int, float]:
                    raise TypeError
            except TypeError:
                print("matrix must be a matrix (list of lists) of " +
                      "integers/floats")
                break
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
        return [[round(j/div, 2) for j in i] for i in matrix]
    except (TypeError, ZeroDivisionError):
        return


print(matrix_divided([[2, 3, 4, 5, 7, 7], [2, 4, 6, 7, 4], [3, 4, 5, 6, 7], [4, 5, 3, 4, 5]], 2))
print(matrix_divided([[2, 4], [6, 6, "f"]], 0))
