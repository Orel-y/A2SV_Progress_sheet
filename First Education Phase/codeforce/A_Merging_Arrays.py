an, bn = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
merged = []

min_len = min(an, bn)
i, j = 0, 0

while i < an and j < bn:
    if a[i] < b[j]:
        merged.append(a[i])
        i+=1
    
    else:
        merged.append(b[j])
        j+=1

merged = merged+ a[i:] + b[j:]
print(*merged)

