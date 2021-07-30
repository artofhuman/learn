# разделяй и властвуй

# Подсчет суммы рекурсией
def sum(arr, acc = 0):
    if len(arr) == 0:
        return acc
    acc += arr.pop()
    return sum(arr, acc)

result = sum([1, 2, 4, 5])
print(result)


# Количество элементов в списке
def count_items(arr, i = 0):
    try:
        arr[i]
        i += 1
        return count_items(arr, i)
    except:
        return i

result = count_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(result)


def biggest_number(arr, biggest):
    if len(arr) == 0:
        return biggest
    else:
        elem = arr.pop()
        if elem > biggest:
            biggest = elem
        return biggest_number(arr, biggest)

result = biggest_number([1, 20, 3, 4, 5, 6, 7, 8, 9, 30], 0)
print(result)


# without acc argument

def sum2(arr):
    if arr == []:
        return 0
    return arr[0] + sum2(arr[1:])


result = sum2([1, 2, 4, 5])
print("sum2", result)


def count_items2(arr):
    if arr == []:
        return 0
    return 1 + count_items2(arr[1:])


result = count_items2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20])
print("count_itmes2", result)


def biggest_number2(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    submax = biggest_number2(arr[1:])
    return arr[0] if arr[0] > submax else submax

result = biggest_number2([1, 2, 30, 4, 5, 6, 7, 8, 9, 10, 11, 20])
print("biggest_number2", result)


