def count(S, m, n):
    table = [[0] * m for i in range(n)]
    table = [[0 for x in range(m)] for x in range(n + 1)]

    # Fill the entries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1
    for i in range(1, n + 1):
        for j in range(m):
            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i - S[j] >= 0 else 0

            # Count of solutions excluding S[j]
            y = table[i][j - 1] if j >= 1 else 0

            # total count
            table[i][j] = x + y

    print(table)

    return table[n][m - 1]


# def count(S, m, n):
#     # table[i] will be storing the number of solutions for
#     # value i. We need n+1 rows as the table is constructed
#     # in bottom up manner using the base case (n = 0)
#     # Initialize all table values as 0
#     table = [0 for k in range(n + 1)]
#
#     # Base case (If given value is 0)
#     table[0] = 1
#
#     # Pick all coins one by one and update the table[] values
#     # after the index greater than or equal to the value of the
#     # picked coin
#     for i in range(0, m):
#         for j in range(S[i], n + 1):
#             table[j] += table[j - S[i]]
#     print(table)
#
#     return table[n]


if __name__ == "__main__":
    print(count([1, 2, 3], 3, 4))
