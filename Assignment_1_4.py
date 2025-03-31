import time
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def improved_merge_sort(arr, threshold=32):
    if len(arr) <= threshold:
        return insertion_sort(arr)

    mid = len(arr) // 2
    left = improved_merge_sort(arr[:mid], threshold)
    right = improved_merge_sort(arr[mid:], threshold)

    return merge(left, right)


def classic_merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = classic_merge_sort(arr[:mid])
    right = classic_merge_sort(arr[mid:])
    return merge(left, right)


# Tests:
N = 100000
test_data = [random.randint(1, 1000000) for _ in range(N)]

print(f"N: {N}")
start = time.time()
classic_merge_sort(test_data.copy())
end = time.time()
print(f"Класичний Merge Sort: {end - start:.6f} секунд")

start = time.time()
improved_merge_sort(test_data.copy())
end = time.time()
print(f"Покращений Merge Sort: {end - start:.6f} секунд")
