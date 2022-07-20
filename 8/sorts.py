
# Обменная сортировка (метод пузырька):
def bubble(h):
    f = 1
    while f == 1:
        f = 0
        for i in range(len(h) - 1):
            if h[i] > h[i + 1]:
                h[i], h[i + 1] = h[i + 1], h[i]
                f = 1
    return h


def bubble_reverse(h):
    f = 1
    while f == 1:
        f = 0
        for i in range(len(h) - 1):
            if h[i] < h[i + 1]:
                h[i], h[i + 1] = h[i + 1], h[i]
                f = 1
    return h


# Сортировка слиянием:
def confluence(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)
    for i in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list


def confluence_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left_list = confluence_sort(a[:mid])
    right_list = confluence_sort(a[mid:])
    return confluence(left_list, right_list)


# Быстрая сортировка:
def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


def Check(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    else:
        return True

