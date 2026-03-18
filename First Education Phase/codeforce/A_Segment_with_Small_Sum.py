n, s = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
max_len = 0
seg_sum = 0

for right in range(n):
    seg_sum += nums[right]

    while seg_sum > s:
        seg_sum -= nums[left]
        left += 1
    
    max_len = max(right - left + 1, max_len)

print(max_len)
