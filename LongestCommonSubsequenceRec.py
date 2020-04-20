def lcs_rec(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs_rec(X, Y, m - 1, n - 1)
    else:
        return max(lcs_rec(X, Y, m - 1, n), lcs_rec(X, Y, m, n - 1))


if __name__ == "__main__":
    X = "ABCDFB"
    Y = "ADBJ"
    print(lcs_rec(X, Y, len(X), len(Y)))
