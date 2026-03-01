def less_or_equal(arr, n, k):
    arr.sort()

    if k == 0:
        if arr[0] == 1:
            return -1
        return arr[0] - 1

    if k == n:
        return arr[n-1]

    if arr[k-1] == arr[k]:
        return -1

    return arr[k-1]


n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(less_or_equal(arr, n, k))