def mountain_peak(arr):
    i = 0
    k = n - 1
    left_min_idx = i

    while i < k:
        if arr[i] < arr[left_min_idx]:
            left_min_idx = i
            i+=1
        
        if arr[left_min_idx] < arr[k]:
            j = left_min_idx + 1
            
            while j < k:
                if arr[left_min_idx] < arr[j] > arr[k]:
                    return [left_min_idx+1, j+1, k+1]
                
                j+=1
        i += 1
        k -= 1
    
    return []

tc = int(input())

for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = mountain_peak(arr)
    if ans:
        print("YES")
        print(*ans)
    else:
        print("NO")
    
        
