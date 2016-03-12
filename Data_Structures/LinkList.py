# Implements the Bag ADT using a singly linked list.
class LinkList:
    def __init__(self):
        self._head = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def __contains__(self, item):
        cur_node = self._head
        while cur_node is not None and cur_node.item != item:
            cur_node = cur_node.next_node
        return cur_node is not None

    def add(self, item):
        new_node = LinkListNode(item)
        new_node.next_node = self._head
        self._head = new_node
        self.__size += 1

    def remove(self, item):
        pre_node = None
        cur_node = self._head
        while cur_node is not None and cur_node.item != item:
            pre_node = cur_node
            cur_node = cur_node.next_node

        # The item has to be in the bag to remove it.
        assert cur_node is not None, "The item must be in the bag."

        self.__size -= 1
        if cur_node is self._head:
            self._head = cur_node.next_node
        else:
            pre_node.next_node = cur_node.next_node
        return cur_node.item

    def __iter__(self):
        return _LinkListIterator(self._head)


class _LinkListIterator(object):
    def __init__(self, head):
        self.__curNode = head

    def __iter__(self):
        return self

    def next(self):
        if self.__curNode is not None:
            item = self.__curNode.item
            self.__curNode = self.__curNode.next_node
            return item
        else:
            raise StopIteration


# Defines a private storage class for creating list nodes.
class LinkListNode(object):
    def __init__(self, item):
        self.item = item
        self.next_node = None


def sorted_search(head, target):
    cur_node = head
    while cur_node is not None and cur_node.item <= target:
        if cur_node.item == target:
            return True
        else:
            cur_node = cur_node.next_node
    return False


def insert(llink, value):
    # Find the insertion point for the new value.
    pred_node = None
    cur_node = llink._head
    while cur_node is not None and value > cur_node.item:
        pred_node = cur_node
        cur_node = cur_node.next_node

    # Create the new node for the new value.
    new_node = LinkListNode(value)
    new_node.next_node = cur_node
    if cur_node is llink._head:
        llink._head = new_node
    else:
        pred_node.next_node = new_node

if __name__ == '__main__':
    a = link_list()
    for i in range(5, 0, -1):
        a.add(i)
    for i in a:
        print i
    print sorted_search(a._head, 4)
    insert(a, 6)
    insert(a, 3)
    for i in a:
        print i