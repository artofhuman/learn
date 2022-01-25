def qsort(array):
    if len(array) < 2:
        return array
    else:
        median_index = len(array) // 2
        pivot = array[median_index]

        less = []
        greater = []

        for idx, i in enumerate(array):
            if idx == median_index:
                continue

            if i < pivot:
                less.append(i)
            else:
                greater.append(i)

        return qsort(less) + [pivot] + qsort(greater)


print(qsort([10, 2, 30, 20, 10, 2, 1, 5]))
