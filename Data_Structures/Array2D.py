"""
    Implementation of the Array2D ADT using an array of arrays.
"""
from Data_Structures.Array import Array


class Array2D:
    # Creates a 2-D array of size numRows * numCols.
    def __init__(self, num_rows, num_cols):
        # Create a 1-D array to store an array reference for each row.
        self.__the_rows = Array(num_rows)

        # Create the 1-D arrays for each row of the 2-D array.
        for i in range(num_rows):
            self.__the_rows[i] = Array(num_cols)

    # Returns the number of rows in the 2-D array
    def num_rows(self):
        return len(self.__the_rows)

    # Returns the number of columns in the 2-D array.
    def num_cols(self):
        return len(self.__the_rows[0])

    # Clears the array by setting every element to the given value.
    def clear(self, value):
        for row in range(self.num_rows()):
            self.__the_rows[row].clear(value)

    # Gets the contents of the element at position [i, j]
    def __getitem__(self, item):
        assert len(item) == 2, "Invalid number of array subscripts"
        row = item[0]
        col = item[1]
        assert 0 <= row < self.num_rows() and 0 <= col < self.num_cols(), "Array subscript out of range"
        return self.__the_rows[row][col]

    # Sets the contents of the element at position [i, j] to value.
    def __setitem__(self, key, value):
        assert len(key) == 2, "Invalid number of array subscripts"
        row = key[0]
        col = key[1]
        assert 0 <= row < self.num_rows() and 0 <= col < self.num_cols(), "Array subscript out of range"
        self.__the_rows[row][col] = value

if __name__ == '__main__':
    a = Array2D(2, 3)
    for i in range(2):
        for j in range(3):
            a[i, j] = i + j

    print '[',
    for i in range(2):
        print '\n ',
        for j in range(3):
            print '%d ' % a[i, j],
    print '\n]'
