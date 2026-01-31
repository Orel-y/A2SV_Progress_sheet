n = int(input())
phone_book = {}

for _ in range(n):
    name, phone_no = input().split()
    phone_book[name] = phone_no  

while True:
    try:
        name = input()
        if name in phone_book:
            print(f"{name}={phone_book[name]}")
        else:
            print("Not found")
    except EOFError:
        break

