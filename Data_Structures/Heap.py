from Data_Structures.Array import Array


# An array-base implementation of the max-heap
class MaxHeapByArray:
    def __init__(self, max_size):
        self._elements = Array(max_size)
        self.__count = 0

    def __len__(self):
        return self.__count

    def capacity(self):
        return len(self._elements)

    def add(self, value):
        assert self.__count < self.capacity(), "Cannot add to a full heap."
        self._elements[self.__count] = value
        self.__sift_up(self.__count)
        self.__count += 1

    def extract(self):
        assert self.__count > 0, "Cannot extract from an empty heap."
        value = self._elements[0]
        self.__count -= 1
        self._elements[0] = self._elements[self.__count]
        self.__sift_down(0)
        return value

    def __sift_up(self, ndx):
        if ndx > 0:
            parent = (ndx - 1) // 2
            if self._elements[ndx] > self._elements[parent]:
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
                self.__sift_up(parent)

    def __sift_down(self, ndx):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        if left < self.__count:
            if right < self.__count:
                if self._elements[left] >= self._elements[right]:
                    children = left
                else:
                    children = right
            else:
                children = left
            if self._elements[children] > self._elements[ndx]:
                self._elements[ndx], self._elements[children] = self._elements[children], self._elements[ndx]
                self.__sift_down(children)


if __name__ == '__main__':
    t_heap = MaxHeapByArray(11)
    numbers = [100, 84, 60, 1, 37, 4, 23, 12, 71, 12, 29]
    for num in numbers:
        t_heap.add(num)
    print "In the array:"
    for i in t_heap._elements:
        print i,
    print "\nIn the heap:"
    for i in range(len(numbers)):
        print t_heap.extract(),
