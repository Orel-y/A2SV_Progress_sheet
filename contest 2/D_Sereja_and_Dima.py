n = int(input())
cards_list = list(map(int, input().split()))

sereja: int = 0
dima: int = 0
turn = True #serajs turn True, and dimas turn False
left, right = 0, len(cards_list) - 1

while left <= right:
    if turn:
        if cards_list[left] >= cards_list[right]:
            sereja += cards_list[left]
            left += 1
            turn = False
        elif cards_list[left] <= cards_list[right]:
            sereja += cards_list[right]
            right -= 1
            turn = False
    
    elif not turn:
        if cards_list[left] >= cards_list[right]:
            dima += cards_list[left]
            left += 1
            turn = True
        elif cards_list[left] <= cards_list[right]:
            dima += cards_list[right]
            right -= 1
            turn = True

print (sereja, dima)