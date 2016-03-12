from Data_Structures.Array import Array


# Implementation of the Queue ADT using a Python list.
class QueueByList:
    def __init__(self):
        self.__q_list = list()

    def __len__(self):
        return len(self.__q_list)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, item):
        self.__q_list.append(item)

    def dequeue(self):
        assert not self.is_empty(), "Cannot dequeue from an empty queue."
        return self.__q_list.pop(0)


# Implementation of the Queue ADT using a circular array.
class QueueByCArray:
    def __init__(self, max_size):
        self.__count = 0
        self.__front = 0
        self.__back = max_size - 1
        self.__q_array = Array(max_size)

    def is_empty(self):
        return self.__count == 0

    def is_full(self):
        return self.__count == len(self.__q_array)

    def __len__(self):
        return self.__count

    def enqueue(self, item):
        assert not self.is_full(), "Cannot enqueue to a full queue."
        max_size = len(self.__q_array)
        self.__back = (self.__back + 1) % max_size
        self.__q_array[self.__back] = item
        self.__count += 1

    def dequeue(self):
        assert not self.is_empty(), "Cannot dequeue from an empty queue."
        item = self.__q_array[self.__front]
        max_size = len(self.__q_array)
        self.__front = (self.__front + 1) % max_size
        self.__count -= 1
        return item


# Implementation of the Queue ADT using a linked list.
class QueueByLList:
    def __init__(self):
        self.__q_head = None
        self.__q_tail = None
        self.__count = 0

    def is_empty(self):
        return self.__q_head is None

    def __len__(self):
        return self.__count

    def enqueue(self, item):
        node = _QueueNode(item)
        if self.is_empty():
            self.__q_head = node
        else:
            self.__q_tail.next_node = node

        self.__q_tail = node
        self.__count += 1

    def dequeue(self):
        assert not self.is_empty(), "Cannot dequeue from an empty queue."
        node = self.__q_head
        if self.__q_head is self.__q_tail:
            self.__q_tail = None
        self.__q_head = self.__q_head.next_node
        self.__count -= 1
        return node.item


# Private storage class for creating the linked list nodes.
class _QueueNode(object):
    def __init__(self, item):
        self.item = item
        self.next_node = None


# Implementation of the unbounded Priority Queue ADT using a Python list with new items appended to the end.
class UBPriorityQueue:
    def __init__(self):
        self.__q_list = list()

    def __len__(self):
        return len(self.__q_list)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, item, priority):
        entry = _PriorityQEntry(item, priority)
        self.__q_list.append(entry)

    def dequeue(self):
        assert not self.is_empty(), "Cannot dequeue from an empty queue."
        highest = self.__q_list[0].priority
        index = 0
        for i in range(1, len(self)):
            if self.__q_list[i].priority < highest:
                highest = self.__q_list[i].priority
                index = i
        entry = self.__q_list.pop(index)
        return entry.item


# Private storage class for associating queue items with their priority.
class _PriorityQEntry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority


# Implementation of the bounded Priority Queue ADT using an array of queues
# in which the queues are implemented using a linked list.
class BPriorityQueue:
    def __init__(self, num_levels):
        self.__q_size = 0
        self.__q_levels = Array(num_levels)
        for i in range(num_levels):
            self.__q_levels[i] = QueueByLList()

    def __len__(self):
        return self.__q_size

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, item, priority):
        assert 0 <= priority < len(self.__q_levels), "Invalid priority level."
        self.__q_levels[priority].enqueue(item)
        self.__q_size += 1

    def dequeue(self):
        assert not self.is_empty(), "Cannot dequeue from an empty queue."
        i = 0
        while i < len(self.__q_levels) and self.__q_levels[i].is_empty():
            i += 1
        return self.__q_levels[i].dequeue()

if __name__ == '__main__':
    # # a = QueueByList()
    # # a = QueueByCArray(5)
    # a = QueueByLList()
    # print "Is Empty: ", a.is_empty()
    # for i in range(3):
    #     print "Enqueue: ", i
    #     a.enqueue(i)
    # print "Is Empty: ", a.is_empty()
    # for i in range(3):
    #     print "Dequeue: ", a.dequeue()
    # print "Is Empty: ", a.is_empty()
    q = UBPriorityQueue()
    q.enqueue("purple", 5)
    q.enqueue("black", 1)
    q.enqueue("orange", 3)
    q.enqueue("white", 0)
    q.enqueue("green", 1)
    q.enqueue("yellow", 5)

    for i in range(6):
        print q.dequeue(),

    print "\n"

    q2 = BPriorityQueue(6)
    q2.enqueue("purple", 5)
    q2.enqueue("black", 1)
    q2.enqueue("orange", 3)
    q2.enqueue("white", 0)
    q2.enqueue("green", 1)
    q2.enqueue("yellow", 5)
    for i in range(6):
        print q2.dequeue(),


