import itertools
import time

# Матриця відстаней між містами
from tsp_test_cases import C1, C2, C3, C4

def calculate_path_cost(path, matrix):
    cost = 0
    for i in range(len(path) - 1):
        cost += matrix[path[i]][path[i + 1]]
    cost += matrix[path[-1]][path[0]]
    return cost

def brute_force_tsp(matrix):
    n = len(matrix)
    cities = list(range(n))
    min_cost = float('inf')
    best_path = None

    for perm in itertools.permutations(cities[1:]):
        path = [0] + list(perm)
        cost = calculate_path_cost(path, matrix)
        if cost < min_cost:
            min_cost = cost
            best_path = path

    return best_path, min_cost

# Вихідні дані
for i, C in enumerate([C1, C2, C3, C4], start=1):
    print(f"\nТестовий набір C{i}:")
    start = time.time()
    path, cost = brute_force_tsp(C)
    end = time.time()
    route = " -> ".join(str(x + 1) for x in path + [path[0]])
    print(f"Тестовий набір С{i}: {end - start:.6f} секунд")
    print(f"Оптимальний маршрут: {route}")
    print(f"Загальна довжина: {cost}")
