def is_possible(arr):
    arr.sort()
    
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > 1:
            return "NO"
    
    return "YES"


tc = int(input())

for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))

    print(is_possible(arr))