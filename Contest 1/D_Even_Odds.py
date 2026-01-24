n, k = map(int, input().split())
result = []


for i in range(1, n + 1):
    if i % 2 == 1:
        result.append(i)

for i in range(1, n + 1):
    if i % 2 == 0:
        result.append(i)


print (result[k - 1])