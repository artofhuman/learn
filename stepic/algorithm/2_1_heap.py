import pdb

arr = [5, 12, 64, 1, 37, 90, 91, 97]

def left_child_index(i):
    return (2 * i) + 1


def right_child_index(i):
    return (2 * i) + 2


def sit_down(arr, i):
    size = len(arr)
    max_index = i

    l = left_child_index(i)
    if l < size and arr[l] > arr[max_index]:
            max_index = l

    r = right_child_index(i)
    if r < size and arr[r] > arr[max_index]:
            max_index = r

    if i != max_index:
        arr[i], arr[max_index] = arr[max_index], arr[i]
        sit_down(arr, max_index)


def build_max_heap(_arr):
    i = int(len(_arr) // 2) - 1
    while i >= 0:
        sit_down(_arr, i)
        i = i - 1
    return _arr

build_max_heap(arr)
print(arr)
