def lcs(X, Y, m, n):
    lcs_table = [[0 for j in range(m + 1)] for i in range(n + 1)]
    result = 0
    row, col = 0, 0

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                lcs_table[i][j] = 0
            elif Y[i - 1] == X[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
                if lcs_table[i][j]>result:
                    result = lcs_table[i][j]
                    row = i
                    col = j
            else:
                lcs_table[i][j] = 0

    if result == 0:
        return "No string found"
    result_str = ['0'] * result
    while lcs_table[row][col] != 0:
        result = result - 1
        result_str[result] = X[row - 1]
        row = row - 1
        col = col - 1

    # print(lcs_table)
    return ''.join(result_str)


if __name__ == '__main__':
    X = 'SAURAVVS'
    Y = 'SOURAVV'
    print(lcs(X, Y, len(X), len(Y)))
