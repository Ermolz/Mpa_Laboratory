import random

C1 = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

C2 = [
    [0, 29, 20, 21, 16, 31],
    [29, 0, 15, 29, 28, 40],
    [20, 15, 0, 15, 14, 25],
    [21, 29, 15, 0, 10, 20],
    [16, 28, 14, 10, 0, 18],
    [31, 40, 25, 20, 18, 0]
]

def generate_large_matrix(n, min_val=1, max_val=100):
    matrix = [[0 if i == j else random.randint(min_val, max_val) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            matrix[j][i] = matrix[i][j]
    return matrix

C3 = generate_large_matrix(8)

C4 = [
    [0, 5],
    [5, 0]
]