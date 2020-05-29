def longPalSubS(string):
    n = len(string)
    table = [[0 for j in range(n)] for i in range(n)]
    maxLength = 1
    i = 0
    while i < n:
        table[i][i] = 1
        i = i + 1

    start = 0
    i = 0
    while i < n - 1:
        if string[i] == string[i + 1]:
            table[i][i + 1] = 1
            start = i
            maxLength = 2
        i = i + 1

    for i in table:
        print(i)
    k = 3
    while k <= n:
        # Fix the starting index
        i = 0
        while i < (n - k + 1):

            # Get the ending index of
            # substring from starting
            # index i and length k
            j = i + k - 1

            # checking for sub-string from
            # ith index to jth index iff
            # st[i+1] to st[(j-1)] is a
            # palindrome
            if (table[i + 1][j - 1] and
                    string[i] == string[j]):
                table[i][j] = 1

                if (k > maxLength):
                    start = i
                    maxLength = k
            i = i + 1
        k = k + 1


    return string[start:start + maxLength]


if __name__ == "__main__":
    print(longPalSubS('geeegks'))
