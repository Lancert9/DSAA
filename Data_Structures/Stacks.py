# Implementation of the Stack ADT using a Python list.
class StackByList:
    def __init__(self):
        self.__items = list()

    def __len__(self):
        return len(self.__items)

    def is_empty(self):
        return len(self) == 0

    def peek(self):
        assert not self.is_empty(), "Cannot peek at an empty stack"
        return self.__items[-1]

    def pop(self):
        assert not self.is_empty(), "Cannot pop from an empty stack"
        return self.__items.pop()

    def push(self, item):
        self.__items.append(item)


# Implementation of the Stack ADT using a singly linked list.
class StackByLList:
    def __init__(self):
        self.__top = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def is_empty(self):
        return self.__top is None

    def peek(self):
        assert not self.is_empty(), "Cannot peek at an empty stack"
        return self.__top.item

    def pop(self):
        assert not self.is_empty(), "Cannot pop from an empty stack"
        node = self.__top
        self.__top = self.__top.next_node
        self.__size -= 1
        return node.item

    def push(self, item):
        self.__top = _StackNode(item, self.__top)
        self.__size += 1


# The private storage class fot creating stack nodes.
class _StackNode:
    def __init__(self, item, link):
        self.item = item
        self.next_node = link

if __name__ == '__main__':
    # a = StackByList()
    a = StackByLList()
    print "Is empty: ",
    print a.is_empty()
    for i in range(3):
        a.push(i)
        print "PUSH", a.peek()

    print "Is empty: ",
    print a.is_empty()

    for i in range(3):
        print "POP: ", a.peek()
        a.pop()
