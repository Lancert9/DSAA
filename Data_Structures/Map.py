"""
    Implementation of Map ADT using a single list.
"""


class Map:
    # Creates an empty map instance.
    def __init__(self):
        self.__entryList = list()

    # Returns the number of entries in the map.
    def __len__(self):
        return len(self.__entryList)

    # Determines if the map contains the given key.
    def __contains__(self, key):
        ndx = self.__find_position(key)
        return ndx is not None

    # Adds a new entry to the map if the key does exist.
    # Otherwise, the new value replaces the current value assosiated with key.
    def add(self, key, value):
        ndx = self.__find_position(key)
        # if the key was found
        if ndx is not None:
            self.__entryList[ndx].value = value
            return False
        else:
            entry = _MapEntry(key, value)
            self.__entryList.append(entry)
            return True

    # Returns the value associated with the key.
    def value_of(self, key):
        ndx = self.__find_position(key)
        assert ndx is not None, "Invalid map key"
        return self.__entryList[ndx].value

    # Returns the value associated with the key.
    def remove(self, key):
        ndx = self.__find_position(key)
        assert ndx is not None, "Invalid map key"
        self.__entryList.pop(ndx)

    # Returns an iterator for traversing the keys in the map
    def __iter__(self):
        return _MapIterator(self.__entryList)

    # Helper method used to find the inde position of a category.
    # If the key is not found, None is returned.
    def __find_position(self, key):
        for i in range(len(self)):
            if self.__entryList[i].key == key:
                return i
        return None


# Storage class for holding the key/value pairs.
class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class _MapIterator:
    def __init__(self, the_map):
        self.__map_ref = the_map
        self.__cur_Ndx = 0

    def __iter__(self):
        return self

    def next(self):
        if self.__cur_Ndx < len(self.__map_ref):
            entry = self.__map_ref[self.__cur_Ndx]
            self.__cur_Ndx += 1
            return entry
        else:
            raise StopIteration


if __name__ == '__main__':
    a = Map()
    a.add('a', 1)
    a.add('b', 2)
    print a.value_of('a')
    for element in a:
        print "key: %s. value: %s." % (element.key, element.value)
    a.remove('a')
    for element in a:
        print "key: %s. value: %s." % (element.key, element.value)
