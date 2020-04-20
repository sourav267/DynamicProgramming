def lcs_dp(X, Y):
    m = len(X)
    n = len(Y)
    lcs_table = [[None] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs_table[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i][j - 1], lcs_table[i - 1][j])

    # length of the longest common sub sequence = lcs_table[m][n]
    index = lcs_table[m][n]
    lcs = [""] * (index + 1)
    lcs[index] = ""

    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    i = m
    j = n
    while i > 0 and j > 0:

        # If current character in X[] and Y are same, then
        # current character is part of LCS
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1

        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif lcs_table[i - 1][j] > lcs_table[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return ''.join(lcs)

# O(n) space complexity
# def lcs_dp(X, Y):
#     # Find lengths of two strings
#     m = len(X)
#     n = len(Y)
#
#     L = [[0 for i in range(n + 1)] for j in range(2)]
#
#     # Binary index, used to index current row and
#     # previous row.
#     bi = bool
#     # print(bi)
#
#     for i in range(m):
#         # Compute current binary index
#         print(L)
#         bi = i & 1
#
#         for j in range(n + 1):
#             if i == 0 or j == 0:
#                 L[bi][j] = 0
#
#             elif X[i] == Y[j - 1]:
#                 L[bi][j] = L[1 - bi][j - 1] + 1
#
#             else:
#                 L[bi][j] = max(L[1 - bi][j],
#                                L[bi][j - 1])
#
#                 # Last filled entry contains length of LCS
#     # for X[0..n-1] and Y[0..m-1]
#     print(L)
#     return L[bi][n]


if __name__ == "__main__":
    X = "ABCDFB"
    Y = "ABDB"
    print(lcs_dp(X, Y))
