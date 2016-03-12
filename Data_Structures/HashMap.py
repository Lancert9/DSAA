"""
    Implementation of the Map ADT using closed hashing and a probe with double hashing.
"""
from Data_Structures.Array import Array


class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap:
    UNUSED = None
    EMPTY = _MapEntry(None, None)

    def __init__(self):
        self.__table = Array(7)
        self.__count = 0
        self.__maxCount = len(self.__table) * 2 // 3

    def __len__(self):
        return self.__count

    def __contains__(self, key):
        slot = self.__find_slot(key, False)
        return slot is not None

    def add(self, key, value):
        if key in self:
            slot = self.__find_slot(key, False)
            self.__table[slot].value = value
            return False
        else:
            slot = self.__find_slot(key, True)
            self.__table[slot] = _MapEntry(key, value)
            self.__count += 1
            if self.__count == self.__maxCount:
                self.__rehash()
            return True

    def value_of(self, key):
        slot = self.__find_slot(key, False)
        assert slot is not None, "Invalid map key."
        return self.__table[slot].value

    def remove(self, key):
        slot = self.__find_slot(key, False)
        assert slot is not None, "Invalid map key."
        self.__table[slot] = HashMap.EMPTY

    def __iter__(self):
        return _HashMapIterator(self.__table)

    def __find_slot(self, key, for_insert):
        slot = self.__hash1(key)
        step = self.__hash2(key)
        M = len(self.__table)

        if for_insert:
            while not (self.__table[slot] is HashMap.UNUSED or self.__table[slot] is HashMap.EMPTY):
                slot = (slot + step) % M
            return slot
        else:
            while self.__table[slot] is not HashMap.UNUSED:
                if self.__table[slot].key == key:
                    return slot
                else:
                    slot = (slot + step) % M
            return None

    # The main hash function for mapping keys to table entries.
    def __hash1(self, key):
        return abs(hash(key)) % len(self.__table)

    # The second hash function used with double hashing probes.
    def __hash2(self, key):
        return 1 + abs(hash(key)) % (len(self.__table) - 2)

    # Rebuilds the hash table.
    def __rehash(self):
        orig_table = self.__table
        new_size = len(self.__table) * 2 + 1
        self.__table = Array(new_size)

        self.__count = 0
        self.__maxCount = new_size * 2 // 3

        for entry in orig_table:
            if entry is not HashMap.UNUSED and entry is not HashMap.EMPTY:
                slot = self.__find_slot(entry.key, True)
                self.__table[slot] = entry
                self.__count += 1


class _HashMapIterator:
    def __init__(self, the_table):
        self.__table = the_table
        self.__cur_Ndx = 0

    def __iter__(self):
        return self

    def next(self):
        while self.__cur_Ndx < len(self.__table):
            entry = self.__table[self.__cur_Ndx]
            self.__cur_Ndx += 1
            if not (entry is HashMap.UNUSED or entry is HashMap.EMPTY):
                return entry.value
        raise StopIteration

if __name__ == "__main__":
    m = HashMap()
    numbers = [0, 7, 1, 2, 8, 3, 4, 9]
    for index, num in zip(numbers, range(8)):
        m.add(index, num)

    for item in m:
        print item,

    print "\nRemove 5"
    m.remove(3)
    for item in m:
        print item,
    try:
        m.value_of(3)
    except Exception:
        print "\n\t5 is not here."

    print m.value_of(4)




