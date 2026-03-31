tc = int(input())

for _ in range(tc):
    n, k = map(int, input().split())
    s = input()

    protect_count = 0
    last_one = -k # -6

    # i = 0
    
    # 0 - (-6) = 6 > 5
    for i in range(n):
        if s[i] == '1':
            if (i - last_one) > (k - 1):
                protect_count += 1
            last_one = i

    print(protect_count)