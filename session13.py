
# %%

elements = [2, 3, 4, 3, 2, 23, 4, 5]


# Omega(1)
# O(N)
def linear_search(lst, element):
    for value in lst:
        if value == element:
            return True

    return False


print(linear_search(elements, 33))
print(linear_search(elements, 23))

# %%
# If the collection of elements is sorted, we can use
# binary search


# Omega(1)
# O(log(N))
def binary_search(lst, element):
    left_pivot = 0
    right_pivot = len(lst) - 1
    middle = (left_pivot + right_pivot) // 2

    while left_pivot <= right_pivot:
        middle = (left_pivot + right_pivot) // 2

        if lst[middle] == element:
            return True
        elif lst[middle] < element:
            left_pivot = middle + 1
        else:
            right_pivot = middle - 1

    return False


print(binary_search([1, 2, 3, 4, 5, 6, 7], 4))
print(binary_search([1, 2, 3, 4, 5, 6, 7], 1))
print(binary_search([1, 2, 3, 4, 5, 6, 7], 0))
print(binary_search([1, 2, 3, 4, 5, 6, 7], 8))

# %%


def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def bubble_sort(lst):
    for elem in lst:
        i = 0
        while i < len(lst) - 1:
            if lst[i] > lst[i + 1]:
                swap(lst, i, i + 1)
            i += 1


numbers = [4, 3, 3, 4, 1, 2, 3]
bubble_sort(numbers)

print(numbers)


# %%

# left and righ should be already sorted
def merge(left, right):
    result = []

    while left and right:
        if left[0] > right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if left:
        result += left
    if right:
        result += right

    return result


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    middle = len(lst) // 2

    left = lst[:middle]
    right = lst[middle:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


print(merge_sort([1, 2, 3, 4, 3, 2, 1]))
print(merge_sort([1, 2, 3, 4, 3, 2, 1, 3, 5, 3,
      1412341234, 3, 2, 1, 2, 4, 234234234234]))

# %%
