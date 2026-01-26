t = int(input())

for _ in range(t):
    inputs = list(map(int, input().split()))

    # compare 3 numbers and increment the smallest one
    for _ in range(5):
        inputs.sort()
        inputs[0] += 1

    print(inputs[0] * inputs[1] * inputs[2])
