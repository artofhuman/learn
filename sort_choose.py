# O(n^2)

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def sort_by_choice(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest_i = find_smallest(arr)
        new_arr.append(arr.pop(smallest_i))
    return new_arr


print(sort_by_choice([1, 5, 10, 4, 3, 0]))
