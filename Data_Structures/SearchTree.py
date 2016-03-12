from Stacks import StackByLList as Stack


class BSTMap:
    def __init__(self):
        self.__root = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def __iter__(self):
        return _BSTMapIterator(self.__root)

    def __contains__(self, key):
        return self._search(self.__root, key) is not None

    def value_of(self, key):
        node = self._search(self.__root, key)
        assert node is not None, "Invalid map key."
        return node.value

    def _search(self, subtree, target):
        if subtree is None:
            return None
        elif target < subtree.key:
            return self._search(subtree.left, target)
        elif target > subtree.key:
            return self._search(subtree.right, target)
        else:
            return subtree

    def _minimum(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._minimum(subtree.left)

    def _maximum(self, subtree):
        if subtree is None:
            return None
        elif subtree.right is None:
            return subtree
        else:
            return self._maximum(subtree.right)

    def add(self, key, value):
        node = self._search(self.__root, key)
        if node is not None:
            node.value = value
            return False
        else:
            self.__root = self._insert(self.__root, key, value)
            self.__size += 1
            return True

    def _insert(self, subtree, key, value):
        if subtree is None:
            subtree = _BSTMapNode(key, value)
        elif key < subtree.key:
            subtree.left = self._insert(subtree.left, key, value)
        elif key > subtree.key:
            subtree.right = self._insert(subtree.right, key, value)
        return subtree

    def remove(self, key):
        assert key in self, "Invalid map key."
        self.__root = self.__bst_remove(self.__root, key)
        self.__size -= 1

    def __bst_remove(self, subtree, target):
        if subtree is None:
            return subtree
        elif target < subtree.key:
            subtree.left = self.__bst_remove(subtree.left, target)
            return subtree
        elif target > subtree.key:
            subtree.right = self.__bst_remove(subtree.right, target)
            return subtree
        else:
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree.right is None:
                if subtree.left is not None:
                    return subtree.left
                else:
                    return subtree.right
            else:
                successor = self._minimum(subtree.right)
                subtree.key = successor.key
                subtree.value = successor.value
                subtree.right = self.__bst_remove(subtree.right, successor.key)
                return subtree


class _BSTMapIterator:
        def __init__(self, root):
            self.__theStack = Stack()
            self.__traverse_to_min_node(root)

        def __iter__(self):
            return self

        def next(self):
            if self.__theStack.is_empty():
                raise StopIteration
            else:
                node = self.__theStack.pop()
                key = node.key
                if node.right is not None:
                    self.__traverse_to_min_node(node.right)
                return key

        def __traverse_to_min_node(self, subtree):
            if subtree is not None:
                self.__theStack.push(subtree)
                self.__traverse_to_min_node(subtree.left)


class _BSTMapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


if __name__ == "__main__":
    t_st = BSTMap()
    t_st.add(3, 'c')
    t_st.add(1, 'a')
    t_st.add(4, 'd')
    t_st.add(2, 'b')
    t_st.add(5, 'e')
    t_st.add(0, 'z')
    print "Original Tree:"
    for t_node in t_st:
        print t_node,
    t_st.remove(4)
    print "\nAfter remove 4:"
    for t_node in t_st:
        print t_node,
    print ''
    print "key 0 map to: ", t_st.value_of(0)
    print "key 5 map to: ", t_st.value_of(5)
