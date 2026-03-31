k = int(input())
arr = list(map(int, input()))

count = 0
window = {}
sub_set = set()

left = 0

for right in range(len(arr)):
    window[arr[right]] = window.get(window[arr[right]], 0) + 1

    if window[1] == k:
        count += 1

    
