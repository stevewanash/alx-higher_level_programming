#!/usr/bin/python3
"""rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """class with rectangle dimensions

    Args:
        Base (class): parent class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes rectangle attributes

        Args:
            width (int): rectangle width
            height (int): rectangle height
            x (int, optional): x displacement. Defaults to 0.
            y (int, optional): y displacement. Defaults to 0.
            id (int, optional): rectangle id. Defaults to None.
        """
        all_var = locals()

        def get_key(val):
            for key, value in all_var.items():
                if val == value:
                    return key

        for i in [width, height, x, y]:
            if not type(i) == int:
                raise TypeError("{} must be an integer".format(get_key(i)))

        for i in [x, y]:
            if i < 0:
                raise ValueError("{} must be >= 0".format(get_key(i)))

        for i in [width, height]:
            if i <= 0:
                raise ValueError("{} must be > 0".format(get_key(i)))

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter

        Returns:
            int: width
        """
        return self.__width

    @property
    def height(self):
        """height getter

        Returns:
            int: height
        """
        return self.__height

    @property
    def x(self):
        """x getter

        Returns:
            int: x
        """
        return self.__x

    @property
    def y(self):
        """y getter

        Returns:
            int: y
        """
        return self.__y

    @width.setter
    def width(self, width):
        """width setter
        """
        if not type(width) == int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """height setter
        """
        if not type(height) == int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """x setter
        """
        if not type(x) == int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be > 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """y setter
        """
        if not type(y) == int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be > 0")
        self.__y = y

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints out the rectangle using # symbols"""
        if self.__y:
            for i in range(self.__y):
                print("")
        for i in range(self.__height):
            if self.__x:
                for j in range(self.__x):
                    print("", end=' ')
            for k in range(self.__width):
                print("#", end='')
            print("")

    def __str__(self):
        """returns formated information on the rectangle"""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """updates values of an instance"""
        inst_name = ["id", "_Rectangle__width", "_Rectangle__height",
                     "_Rectangle__x", "_Rectangle__y"]
        usual_name = ["id", "width", "height", "x", "y"]
        c = 0

        if args:
            for i in range(len(args)):
                self.__dict__[inst_name[c]] = args[c]
                c += 1
        elif kwargs:
            for i in kwargs:
                if i in usual_name:
                    for j in usual_name:
                        if j == i:
                            break
                        c += 1
                    self.__dict__[inst_name[c]] = kwargs[i]
                    c = 0
                elif i in inst_name:
                    self.__dict__[i] = kwargs[i]

    def to_dictionary(self):
        """returns dictionary containing instance attributes"""
        return self.__dict__
