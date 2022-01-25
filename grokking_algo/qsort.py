def qsort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]

        less = []
        greater = []

        for i in array[1:]:
            if i < pivot:
                less.append(i)
            else:
                greater.append(i)

        return qsort(less) + [pivot] + qsort(greater)


print(qsort([10, 2, 30, 1, 2, 1, 5]))
