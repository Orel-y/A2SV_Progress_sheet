n = int(input())

for _ in range(n):
    tc = int(input())

    if tc % 3 == 2 and tc > 3:
        print(1)
    else:
        print(tc % 3)
    
