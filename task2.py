def subset_sum(S, coins):
    dp = [False] * (S + 1)
    dp[0] = True

    for c in coins:
        for j in range(S, c - 1, -1):
            if dp[j - c]:
                dp[j] = True

    return dp[S]

if __name__ == "__main__":
    S = int(input().strip())
    coins = list(map(int, input().split()))

    result = subset_sum(S, coins)
    print(result)

# Оцінка складності алгоритму:
# Якщо монет буде k, а сума велика — наприклад S то виходить, що у нас буде приблизно k * S дій.
# Ну воно доволі ефективне для середніх задач хоча для дуже великих сум вже буде трошки повільно.