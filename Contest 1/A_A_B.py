n = int(input())
inputs = [input() for _ in range(n)]

for exp in inputs:
    a = int(exp[0])
    b = int(exp[-1])

    print (a + b)
