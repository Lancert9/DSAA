# Implementation of the Set ADT container using a Python list.
class Set:
    # Creates an empty set instance.
    def __init__(self):
        self._the_elements = list()

    # Returns the number of items in the set.
    def __len__(self):
        return len(self._the_elements)

    # Determines if an element is in the set.
    def __contains__(self, element):
        return element in self._the_elements

    # Adds a new unique element to the set.
    def add(self, element):
        if element not in self:
            self._the_elements.append(element)

    # Removes an element from the set.
    def remove(self, element):
        assert element in self, "The element must be in the set."
        self._the_elements.remove(element)

    # Determine if two sets are equal.
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        else:
            return self.is_subset_of(other)

    # Determines if this set is a subset of set B.
    def is_subset_of(self, other):
        for element in self:
            if element not in other:
                return False
        return True

    # Creates a new set from the union of this set and set B.
    def difference(self, other):
        new_set = Set()
        for element in self:
            if element not in other:
                new_set._the_elements.append(element)
        return new_set

    # Returns an iterator for traversing the list of items.
    def __iter__(self):
        return _SetIterator(self._the_elements)


class _SetIterator:
    def __init__(self, the_set):
        self.__set_ref = the_set
        self.__cur_Ndx = 0

    def __iter__(self):
        return self

    def next(self):
        if self.__cur_Ndx < len(self.__set_ref):
            entry = self.__set_ref[self.__cur_Ndx]
            self.__cur_Ndx += 1
            return entry
        else:
            raise StopIteration


# Implementation of the Set ADT using a sorted list.
class SortedSet(Set):
    def __init__(self):
        Set.__init__(self)

    def __contains__(self, element):
        ndx = self.__find_position(element)
        return ndx < len(self) and self._the_elements[ndx] == element

    def add(self, element):
        if element not in self:
            ndx = self.__find_position(element)
            self._the_elements.insert(ndx, element)

    def remove(self, element):
        assert element in self, "The element must be in the set."
        ndx = self.__find_position(element)
        self._the_elements.pop(ndx)

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        else:
            for i in range(len(self)):
                if self._the_elements[i] != other._the_elements[i]:
                    return False
            return True

    def is_subset_of(self, other):
        i = 0
        j = 0
        while i < len(self):
            entry = self._the_elements[i]
            flag = False
            while j < len(other):
                if other._the_elements[j] == entry:
                    i += 1
                    j += 1
                    flag = True
                    break
                j += 1
            if flag is False:
                return False
        return True

    def union(self, other):
        result_set = SortedSet()
        result = []
        index_a = 0
        index_b = 0
        length_a = len(self._the_elements)
        length_b = len(other._the_elements)
        while index_a < length_a and index_b < length_b:
            entry_a = self._the_elements[index_a]
            entry_b = other._the_elements[index_b]
            if entry_a < entry_b:
                result.append(entry_a)
                index_a += 1
            elif entry_a > entry_b:
                result.append(entry_b)
                index_b += 1
            else:
                result.append(entry_a)
                index_a += 1
                index_b += 1
        if index_a < length_a:
            result.extend(self._the_elements[index_a:])
        else:
            result.extend(other._the_elements[index_b:])
        result_set._the_elements = result
        return result_set

    # Finds the position of the element within the ordered list.
    def __find_position(self, target):
        the_list = self._the_elements
        low = 0
        high = len(the_list) - 1
        while low <= high:
            mid = (low + high) / 2
            if the_list[mid] == target:
                return mid
            elif target < the_list[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low


if __name__ == '__main__':
    # a = Set()
    a = SortedSet()
    a.add(1)
    a.add(2)
    print "A:",
    for ele in a:
        print ele,
    # b = Set()
    b = SortedSet()
    b.add(2)
    b.add(3)
    print "\nB:",
    for ele in b:
        print ele,

    c = a.difference(b)
    print "\nA - B:",
    for ele in c:
        print ele,

    print "\nA is subset of B: ",
    print a.is_subset_of(b)
    print "A is subset of A: ",
    print a.is_subset_of(a)

    print "A | B:",
    d = a.union(b)
    for ele in d:
        print ele,

    a.remove(1)
    print "\nAfter remove 1, Set A:",
    for ele in a:
        print ele,


