def linear_search(values, target):
    n = len(values)
    for i in range(n):
        if values[i] == target:
            return True
    return False


def binary_search(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        mid = (low + high) // 2
        entry = values[mid]
        if entry < target:
            low = mid + 1
        elif entry > target:
            high = mid - 1
        else:
            return True
    return False


# Modified version of the binary search that returns the index within
# a sorted sequence indicating where the target should be located.
def find_sorted_position(a_seq, target):
    low = 0
    high = len(a_seq) - 1
    while low <= high:
        mid = (low + high) // 2
        entry = a_seq[mid]
        if entry < target:
            low = mid + 1
        elif entry > target:
            high = mid - 1
        else:
            return mid
    return low


# Performs a recursive binary search on a sorted sequence.
def rec_binary_search(a_seq, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if a_seq[mid] == target:
            return True
        elif target < a_seq[mid]:
            return rec_binary_search(a_seq, target, low, mid - 1)
        else:
            return rec_binary_search(a_seq, target, mid + 1, high)


if __name__ == '__main__':
    t_list = [1, 2, 3, 4, 5]
    for i in range(2, 7):
        print "#" * 10
        print linear_search(t_list, i)
        print binary_search(t_list, i)
        print find_sorted_position(t_list, i)
        print rec_binary_search(t_list, i, 0, len(t_list) - 1)
