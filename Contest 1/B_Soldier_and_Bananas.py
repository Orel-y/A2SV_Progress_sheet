k, n, w = map(int, input().split())

sum: int = 0

for i in range(w + 1):
    sum += i

michelew = k * sum

if michelew < n:
    print (0)
else:
    print((michelew - n))