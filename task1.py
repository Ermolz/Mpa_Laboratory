def pos(c):
    return ord(c) - ord('a') + 1

def modified_levenshtein(s: str, t: str) -> list[list[int]]:
    m, n = len(s), len(t)
    D = [[0] * (n + 1) for _ in range(m + 1)]


    for i in range(1, m + 1):
        D[i][0] = D[i - 1][0] + pos(s[i - 1])

    for j in range(1, n + 1):
        D[0][j] = D[0][j - 1] + pos(t[j - 1])

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost_sub = abs(pos(s[i - 1]) - pos(t[j - 1]))
            cost_delete = D[i - 1][j] + pos(s[i - 1])
            cost_insert = D[i][j - 1] + pos(t[j - 1])
            cost_replace = D[i - 1][j - 1] + cost_sub
            D[i][j] = min(cost_replace, cost_delete, cost_insert)

    return D

if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    D = modified_levenshtein(s, t)

    max_val = max(max(row) for row in D)
    width = len(str(max_val)) + 1

    for row in D:
        print("".join(str(val).rjust(width) for val in row))
    print(f"result: {D[len(s)][len(t)]}")
