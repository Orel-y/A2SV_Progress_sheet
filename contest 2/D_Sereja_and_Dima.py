n = int(input())
cards_list = list(map(int, input().split()))

sereja: int = 0
dima: int = 0
turn = True #serajs turn True, and dimas turn False

while len(cards_list) > 0:
    if turn:
        if cards_list[0] >= cards_list[-1]:
            sereja += cards_list[0]
            cards_list = cards_list[1:]
            turn = False
        elif cards_list[0] <= cards_list[-1]:
            sereja += cards_list[-1]
            cards_list.pop()
            turn = False
    
    elif not turn:
        if cards_list[0] >= cards_list[-1]:
            dima += cards_list[0]
            cards_list = cards_list[1:]
            turn = True
        elif cards_list[0] <= cards_list[-1]:
            dima += cards_list[-1]
            cards_list.pop()
            turn = True

print (sereja, dima)