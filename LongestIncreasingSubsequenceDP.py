def long_inc_sub(arr):
    n = len(arr)
    lis = [1] * n
    for i in range(1, n):
        # print(lis)
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    maxm = 0

    for i in lis:
        maxm = max(maxm, i)
    print(lis)
    return maxm


if __name__ == "__main__":
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print(long_inc_sub(arr))
