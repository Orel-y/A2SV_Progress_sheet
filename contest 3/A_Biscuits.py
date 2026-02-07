n = int(input())

for _ in range(n):
    tc = int(input())
    
    if (tc % 2 == 1):
        ans = int(tc // 2)
    elif (tc % 2 == 0):
        ans = (tc // 2) - 1
    print(ans)

