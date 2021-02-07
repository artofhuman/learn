count_processors = 16
count_tasks = 12

# timings = [4, 5, 2, 0, 1, 0, 7, 2, 6, 8, 0, 0]

count_processors = 2
count_tasks = 12
timings = [1, 2, 3, 4, 5]

# out
# номер процессора, время когда это произойет
# 0 0
# 1 0
# 0 1
# 1 2
# 0 4

# - создать массив [proc_num, 0] равный кол-ву процессоров, for 2  [ [0, 0], [1, 0] ], 0 время
# - print head
# - к времени добавляем врeмя из времени задчи proc_num, time; time += timings[i]
# - поменять приориетет (утапливаем процессор)


# count_processors, count_tasks = map(int, input().split(" "))
# timings = map(int, input().split(" "))

def left_child_index(i):
    return (2 * i) + 1


def right_child_index(i):
    return (2 * i) + 2


def sit_down(arr, i):
    size = len(arr)
    max_index = i

    # breakpoint()

    l_index = left_child_index(i)
    r_index = right_child_index(i)

    if l_index < size:
        left = arr[l_index]
        _elem_max_i = arr[max_index]
        if left[1] < _elem_max_i[1] or (left[1] == _elem_max_i[1] and left[0] < _elem_max_i[0]):
            max_index = l_index

    if r_index < size:
        right = arr[r_index]
        _elem_max_i = arr[max_index]
        if right[1] < _elem_max_i[1] or (right[1] == _elem_max_i[1] and right[0] < _elem_max_i[0]):
            max_index = r_index

    if i != max_index:
        # breakpoint()
        arr[i], arr[max_index] = arr[max_index], arr[i]
        sit_down(arr, max_index)


def build_heap(_arr):
    i = int(len(_arr) // 2)
    while i >= 0:
        sit_down(_arr, i)
        i = i - 1


def solution(count_processors, timings):
    heap = []
    for i in range(count_processors):
        heap.append((i, 0))

    # build_heap(heap)

    # print("INIT heap", heap)
    # print("------")

    for time in timings:
        head = heap[0]
        proc_num, count_t = head

        # print("==========")
        # print("heap", heap)

        print(*head)

        # print("==========")

        count_t += time
        heap[0] = (proc_num, count_t)
        # print("new heap", heap)
        sit_down(heap, 0) # todo change priority


# solution(2, [1, 2, 3, 4, 5])
# solution(16, [4, 5, 2, 0, 1, 0, 7, 2, 6, 8, 0, 0])
# solution(4, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
