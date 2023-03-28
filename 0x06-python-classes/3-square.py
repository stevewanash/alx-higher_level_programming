
class Square:
    """This class defines a square"""
    def __init__(self, size=0):
        """This function creates instances for the attribute size

        Args:
            size: size of the square's sides, without units
            it is initialized to zero

        Raises:
            TypeError: if size type is not int

            ValueError: if size is less than zero

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Area function returns the area of the square
        """
        return self.__size**2
