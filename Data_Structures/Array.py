"""
Implements the Array ADT using array capabilities of the ctypes module.
"""

import ctypes


class Array:
    # Creates an array with size elements.
    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self.__size = size
        # Create the array structure using the ctypes module.
        py_array_type = ctypes.py_object * size
        self.__elements = py_array_type()
        # Initialize each element.
        self.clear(None)

    # Returns the size of the array.
    def __len__(self):
        return self.__size

    # Gets the contents of the index element.
    def __getitem__(self, index):
        assert 0 <= index < len(self), "Array subscript out of range"
        return self.__elements[index]

    # Puts the value in the array element at index position.
    def __setitem__(self, index, value):
        assert 0 <= index < len(self), "Array subscript out of range"
        self.__elements[index] = value

    # Clears the array by setting each element to the given value.
    def clear(self, value):
        for i in range(self.__size):
            self.__elements[i] = value

    # Returns the array's iterator for traversing the elements.
    def __iter__(self):
        return _ArrayIterator(self.__elements)


# An iterator for the Array ADT.
class _ArrayIterator:
    def __init__(self, the_array):
        self.__array_ref = the_array
        self.__cur_Ndx = 0

    def __iter__(self):
        return self

    def next(self):
        if self.__cur_Ndx < len(self.__array_ref):
            entry = self.__array_ref[self.__cur_Ndx]
            self.__cur_Ndx += 1
            return entry
        else:
            raise StopIteration


if __name__ == '__main__':
    A = Array(5)
    for i in range(len(A)):
        A[i] = i
    for i in A:
        print i


