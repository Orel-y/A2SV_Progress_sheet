def winner_changed(first_winner, last_winner):
    if first_winner != last_winner:
        return True
    return False
    
# does winner chaged if the winner change there may be a chance for a tie
tc = int(input())

for _ in range(tc):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    first_winner = ''
    last_winner = ''

    if x1 > y1:
        first_winner = 'x'
    if y1 > x1:
        first_winner = 'y'
    if x2 > y2:
        last_winner = 'x'
    if y2 > x2:
        last_winner = 'y'

    ans = winner_changed(first_winner, last_winner)
    if ans:
        print("NO")
    else:
        print("YES")