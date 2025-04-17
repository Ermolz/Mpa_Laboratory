import sys

def read_input():
    try:
        # Зчитуємо N й перевіряємо, що воно в межах [4, 9]
        N = int(input().strip())
        if N < 4 or N > 9:
            raise ValueError
    except:
        print("Invalid input")
        sys.exit()

    try:
        # Зчитуємо перший рядок як список цілих чисел
        first_row = list(map(int, input().split()))
    except:
        print("Invalid input")
        sys.exit()

    # Перевіряємо довжину й коректність перестановки 1..N
    if len(first_row) != N or sorted(first_row) != list(range(1, N+1)):
        print("Invalid input")
        sys.exit()

    return N, first_row

def print_board(board):
    # Вивід кожного рядка квадрату через space
    for row in board:
        print(" ".join(map(str, row)))

def solve_sudoku_modified(N, first_row):
    # Знаходимо індекс стовпчика, де в першому рядку стоїть 1
    col_one = first_row.index(1)

    # Створюємо порожню дошку і заповнюємо:
    # перший рядок із first_row
    # фіксовану колонку зі строго зростаючими значеннями 1..N
    board = [[None]*N for _ in range(N)]
    board[0] = first_row.copy()
    for i in range(N):
        board[i][col_one] = i + 1 

    # Підтримуємо множини використаних чисел у кожному рядку та стовпчику
    row_used = [set() for _ in range(N)]
    col_used = [set() for _ in range(N)]
    # Заповнюємо для першого рядка
    for j, v in enumerate(board[0]):
        row_used[0].add(v)
        col_used[j].add(v)
    # Заповнюємо для фіксованої колонки
    for i in range(N):
        row_used[i].add(board[i][col_one])
        col_used[col_one].add(board[i][col_one])

    # Збираємо всі інші порожні клітинки (крім першого рядка та фіксованої колонки)
    empty_cells = [
        (i, j)
        for i in range(1, N)
        for j in range(N)
        if j != col_one
    ]

    # Рекурсивна функція для backtracking по порожніх клітинках
    def dfs(pos):
        # Якщо всі клітинки заповнені => знайдено рішення
        if pos == len(empty_cells):
            return True
        i, j = empty_cells[pos]

        # Перебір можливих значень від 1 до N
        for val in range(1, N+1):
            if val not in row_used[i] and val not in col_used[j]:
                # Пробуємо поставити val
                board[i][j] = val
                row_used[i].add(val)
                col_used[j].add(val)

                if dfs(pos + 1):
                    return True

                # Відкачуємо зміни
                row_used[i].remove(val)
                col_used[j].remove(val)

        # Якщо жодне значення не пішло повертаємо False
        return False

    # Повертаємо готову дошку або None, якщо рішення немає
    return board if dfs(0) else None

def main():
    N, first_row = read_input()
    sol = solve_sudoku_modified(N, first_row)
    if sol:
        print_board(sol)
    else:
        print("No solution")

if __name__ == "__main__":
    main()
