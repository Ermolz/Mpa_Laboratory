import time
import random

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


def recursive_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = recursive_merge_sort(arr[:mid])
    right = recursive_merge_sort(arr[mid:])
    return merge(left, right)


def iterative_merge_sort(arr):
    width = 1
    n = len(arr)

    while width < n:
        for i in range(0, n, 2 * width):
            left = arr[i:i + width]
            right = arr[i + width:i + 2 * width]
            arr[i:i + 2 * width] = merge(left, right)
        width *= 2

    return arr


N = 100000
test_data = [random.randint(1, 1000000) for _ in range(N)]
print(f"N: {N}")

start = time.time()
recursive_merge_sort(test_data.copy())
end = time.time()
print(f"Рекурсивний Merge Sort: {end - start:.6f} секунд")

start = time.time()
iterative_merge_sort(test_data.copy())
end = time.time()
print(f"Ітеративний Merge Sort: {end - start:.6f} секунд")




N = 5
test_data = [5, 2, 4, 1, 3]
print(f"N: {N}")

start = time.time()
recursive_merge_sort(test_data.copy())
end = time.time()
print(f"Рекурсивний Merge Sort: {end - start:.6f} секунд")

start = time.time()
iterative_merge_sort(test_data.copy())
end = time.time()
print(f"Ітеративний Merge Sort: {end - start:.6f} секунд")
