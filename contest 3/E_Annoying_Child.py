def max_score(tn, coins):
    ans = list(0 for _ in range(tn))
    sum = 0
    for k in range(1, tn + 1):
        if ans:
            sum += ans[k-1]
        ans.append(pick_max_odd(k, coins, sum))
        

    return ans

def pick_max_odd(k, coins, sum):
    max_non_des = 0

    if k % 2 == 1:
        max_odd = float("-inf")
        for c in coins:
            if c % 2 == 1 and c > max_odd:
                max_odd = c
            max_non_des += (max_odd + sum)
    if k % 2 == 0:
        max_even = float("-inf")
        for c in coins:
            if c % 2 == 0 and c > max_even:
                max_even = c
                max_non_des += (max_even + sum)
    
    if max_non_des % 2  == 0:
        return 0
    return max_non_des



n = int(input())

for _ in range(n):
    tn = int(input())
    coins = list(map(int, input().split()))

    ans = max_score(tn, coins)
    print (*ans)