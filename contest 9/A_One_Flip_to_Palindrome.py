def is_palindrome(st, n):
    s = list(st)
    org = s.copy()

    left = 0
    right = n - 1
     
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1  
  
    return True
tc = int(input())

for _ in range(tc):
    n = int(input())
    s = input()

    is_p = is_palindrome(s, n)
    if is_p:
        print("Yes")
    else:
        print("NO")

