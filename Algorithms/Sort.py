from Data_Structures.Array import Array
from Data_Structures.Queues import QueueByLList as Queue
from Data_Structures.LinkList import LinkList
from Data_Structures.LinkList import insert as add_to_sorted_list
from Data_Structures.LinkList import LinkListNode
from Data_Structures.Heap import MaxHeapByArray as MaxHeap

# Sort a sequence in ascending order.
def bubble_sort(seq):
    n = len(seq)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]


# Sort a sequence in ascending order.
def revised_bubble_sort(seq):
    n = len(seq)
    for i in range(n - 1):
        flag = True
        for j in range(n - i - 1):
            if seq[j] > seq[j + 1]:
                flag = False
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
        if flag:
            break


# Sorts a sequence in ascending order.
def selection_sort(seq):
    n = len(seq)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if seq[j] < seq[min_index]:
                min_index = j
        if min_index != i:
            seq[i], seq[min_index] = seq[min_index], seq[i]


# Sorts a sequence in ascending order.
def insertion_sort(seq):
    n = len(seq)
    for i in range(1, n):
        value = seq[i]
        while i > 0 and value < seq[i - 1]:
            seq[i] = seq[i - 1]
            i -= 1
        seq[i] = value


def merge_sorted_lists(list_a, list_b):
    result = []
    index_a = 0
    index_b = 0
    length_a = len(list_a)
    length_b = len(list_b)
    while index_a < length_a and index_b < length_b:
        entry_a = list_a[index_a]
        entry_b = list_b[index_b]
        if entry_a <= entry_b:
            result.append(entry_a)
            index_a += 1
        else:
            result.append(entry_b)
            index_b += 1
    if index_a < length_a:
        result.extend(list_a[index_a:])
    else:
        result.extend(list_b[index_b:])
    return result


# Sorts a Python list in ascending order using the merge sort algorithm.
def merge_sort(a_list):
    if len(a_list) <= 1:
        return a_list
    else:
        mid = len(a_list) // 2

    left = merge_sort(a_list[: mid])
    right = merge_sort(a_list[mid:])

    new_list = merge_sorted_lists(left, right)
    return new_list


# Improved merge sort algorithm.
def rec_merge_sort(a_list, left, right, tmp_array):
    if left == right:
        return
    else:
        mid = (left + right) // 2

    rec_merge_sort(a_list, left, mid, tmp_array)
    rec_merge_sort(a_list, mid + 1, right, tmp_array)
    merge_virtual_seq(a_list, left, mid + 1, right + 1, tmp_array)
    return a_list


def merge_virtual_seq(a_list, left, mid, right, tmp_array):
    left_index = left
    right_index = mid
    tmp_index = 0
    while left_index < mid and right_index < right:
        if a_list[left_index] < a_list[right_index]:
            tmp_array[tmp_index] = a_list[left_index]
            left_index += 1
        else:
            tmp_array[tmp_index] = a_list[right_index]
            right_index += 1
        tmp_index += 1

    while left_index < mid:
        tmp_array[tmp_index] = a_list[left_index]
        left_index += 1
        tmp_index += 1
    while right_index < right:
        tmp_array[tmp_index] = a_list[right_index]
        right_index += 1
        tmp_index += 1

    for i in range(right - left):
        a_list[i + left] = tmp_array[i]


def new_merge_sort(a_array):
    tmp_array = Array(len(a_array))
    rec_merge_sort(a_array, 0, len(a_array) - 1, tmp_array)


# Sorts an array or list using the recursive quick sort algorithm.
def quick_sort(a_seq):
    rec_quick_sort(a_seq, 0, len(a_seq) - 1)


def rec_quick_sort(a_seq, first, last):
    if first >= last:
        return
    else:
        pos = partition_seq(a_seq, first, last)
        rec_quick_sort(a_seq, first, pos - 1)
        rec_quick_sort(a_seq, pos + 1, last)


# Partitions the sequence using the first key as the pivot.
def partition_seq(a_seq, first, last):
    pivot = a_seq[first]
    left = first + 1
    right = last
    while left <= right:
        while left <= right and a_seq[left] < pivot:
            left += 1
        while left <= right and a_seq[right] >= pivot:
            right -= 1
        if left < right:
            a_seq[left], a_seq[right] = a_seq[right], a_seq[left]
    # Put the pivot in the proper position
    if right != first:
        a_seq[first], a_seq[right] = a_seq[right], a_seq[first]
    return right


# Sorts a sequence of positive integers using the radix sort algorithm.
def radix_sort(a_list, num_digits):
    bin_array = Array(10)
    for k in range(10):
        bin_array[k] = Queue()

    column = 1
    for d in range(num_digits):
        for key in a_list:
            digit = (key // column) % 10
            bin_array[digit].enqueue(key)

        i = 0
        for a_bin in bin_array:
            while not a_bin.is_empty():
                a_list[i] = a_bin.dequeue()
                i += 1

        column *= 10


# Sort a linked list using the technique of the insertion sort.
def link_list_insertion_sort(a_link_list):
    if a_link_list is None:
        return None

    new_link_list = LinkList()
    while a_link_list is not None:
        cur_node = a_link_list
        a_link_list = a_link_list.next_node

        cur_node.next_node = None
        add_to_sorted_list(new_link_list, cur_node.item)
    return new_link_list


# Sorts a linked list using merge sort
def link_list_merge_sort(a_link_list):
    if a_link_list.next_node is None:
        return a_link_list

    right_list = _split_link_list(a_link_list)
    left_list = a_link_list

    left_list = link_list_merge_sort(left_list)
    right_list = link_list_merge_sort(right_list)

    a_link_list = _merge_link_lists(left_list, right_list)

    return a_link_list


# Splits a linked list at the midpoint to create two sub-lists.
# The head reference of the right sub-list is returned.
# The left sub-list is still referenced by the original head reference.
def _split_link_list(a_link_list):
    mid_point = a_link_list
    cur_node = mid_point.next_node
    while cur_node is not None:
        cur_node = cur_node.next_node
        if cur_node is not None:
            mid_point = mid_point.next_node
            cur_node = cur_node.next_node
    right_list = mid_point.next_node
    mid_point.next_node = None
    return right_list


# Merges two sorted linked list; return head reference for the new list.
def _merge_link_lists(left_list, right_list):
    new_list = LinkListNode(None)
    new_tail = new_list

    while left_list is not None and right_list is not None:
        if left_list.item <= right_list.item:
            new_tail.next_node = left_list
            left_list = left_list.next_node
        else:
            new_tail.next_node = right_list
            right_list = right_list.next_node

        new_tail = new_tail.next_node
        new_tail.next_node = None

    if left_list is not None:
        new_tail.next_node = left_list
    else:
        new_tail.next_node = right_list

    return new_list.next_node


def simple_heap_sort(a_seq):
    heap = MaxHeap(len(a_seq))

    for element in a_seq:
        heap.add(element)

    for i in range(len(a_seq) - 1, -1, -1):
        a_seq[i] = heap.extract()


def heap_sort(a_seq):
    # Build a max-heap within the same array.
    for i in range(len(a_seq)):
        _sift_up(a_seq, i)

    # Extract each value and rebuild the heap.
    for i in range(len(a_seq) - 1, -1, -1):
        a_seq[0], a_seq[i] = a_seq[i], a_seq[0]
        _sift_down(a_seq, 0, i)


def _sift_up(a_seq, ndx):
    if ndx > 0:
        parent = (ndx - 1) // 2
        if a_seq[ndx] > a_seq[parent]:
            a_seq[ndx], a_seq[parent] = a_seq[parent], a_seq[ndx]
            _sift_up(a_seq, parent)


def _sift_down(a_seq, ndx, end):
    left = 2 * ndx + 1
    right = 2 * ndx + 2
    if left < end:
        if right < end:
            if a_seq[left] >= a_seq[right]:
                children = left
            else:
                children = right
        else:
            children = left
        if a_seq[children] > a_seq[ndx]:
            a_seq[ndx], a_seq[children] = a_seq[children], a_seq[ndx]
            _sift_down(a_seq, children, end)


if __name__ == '__main__':
    # from copy import copy
    # a = [1, 4, 5, 2, 3]
    # print a
    # b = copy(a)
    # bubble_sort(b)
    # print b
    # c = copy(a)
    # revised_bubble_sort(c)
    # print c
    # d = copy(a)
    # selection_sort(d)
    # print d
    # e = copy(a)
    # insertion_sort(e)
    # print e

    # a = [2, 8, 15, 23, 37]
    # b = [4, 6, 15, 20]
    # r = merge_sorted_lists(a, b)
    # print r

    # a = [10, 23, 531, 18, 4, 31, 5, 113]
    # print a
    # r = merge_sort(a)
    # b = [0] * 5
    # r = rec_merge_sort(a, 0, len(a) - 1, b)
    # new_merge_sort(a)
    # quick_sort(a)
    # radix_sort(a, 3)
    # print a

    # t_link_list = LinkList()
    # item_list = [23, 2, 51, 18, 4, 31, 1, 99]
    # for item in item_list:
    #     t_link_list.add(item)
    # for node in t_link_list:
    #     print node,
    # print "\nAfter sorted:"
    # # r_link_list = link_list_insertion_sort(t_link_list._head)
    # new_header = link_list_merge_sort(t_link_list._head)
    # while new_header is not None:
    #     print new_header.item,
    #     new_header = new_header.next_node

    a = [10, 23, -1, 531, 18, 4, 31, 5, 113]
    print a
    # simple_heap_sort(a)
    heap_sort(a)
    print a

