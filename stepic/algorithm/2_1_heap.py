def left_child_index(i):
    return (2 * i) + 1


def right_child_index(i):
    return (2 * i) + 2


def sit_down(arr, i, m, swaps):
    size = len(arr)
    max_index = i

    l = left_child_index(i)
    if l < size and arr[l] < arr[max_index]:
            max_index = l

    r = right_child_index(i)
    if r < size and arr[r] < arr[max_index]:
            max_index = r

    if i != max_index:
        swaps.append([i, max_index])
        arr[i], arr[max_index] = arr[max_index], arr[i]
        m = m + 1
        m, swaps = sit_down(arr, max_index, m, swaps)
    return m, swaps


size = input()
arr = list(map(int, input().split(" ")))
def build_heap(_arr):
    m = 0
    swaps = []
    i = int(len(_arr) // 2)
    while i >= 0:
        m, swaps = sit_down(_arr, i, m, swaps)
        i = i - 1
    return m, swaps

m, swaps = build_heap(arr)


print(m)
for e in swaps:
    print(*e)
