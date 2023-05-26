#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes all square instances"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets the size value"""
        return super().width

    @size.setter
    def size(self, size):
        """sets the size attribute"""
        super(Square, Square).width.__set__(self, size)
        super(Square, Square).height.__set__(self, size)

    def update(self, *args, **kwargs):
        """updates values of an instance
        """
        inst_name = ["id", "_Rectangle__width", "_Rectangle__height",
                     "_Rectangle__x", "_Rectangle__y"]
        usual_name = ["id", "size", "x", "y"]
        c = 0
        b = 0

        if args:
            for i in range(len(args)):
                if c == 1:
                    self.__dict__[inst_name[b]] = args[c]
                    self.__dict__[inst_name[b + 1]] = args[c]
                    b += 2
                    c += 1
                else:
                    self.__dict__[inst_name[b]] = args[c]
                    c += 1
                    b += 1
        elif kwargs:
            for i in kwargs:
                if i in usual_name:
                    for j in usual_name:
                        if j == i:
                            break
                        c += 1
                    if c == 1:
                        self.__dict__[inst_name[c]] = kwargs[i]
                        self.__dict__[inst_name[c + 1]] = kwargs[i]
                    elif c > 1:
                        self.__dict__[inst_name[c + 1]] = kwargs[i]
                    else:
                        self.__dict__[inst_name[c]] = kwargs[i]
                    c = 0
                elif i in inst_name:
                    self.__dict__[i] = kwargs[i]

    def to_dictionary(self):
        """returns a dictionary of instance attributes
        """
        return self.__dict__
