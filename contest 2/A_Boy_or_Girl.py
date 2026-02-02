user_name = input()
char_no = len(user_name)

un = set(user_name)

if len(un) % 2 == 0:
    print("CHAT WITH HER!")
elif len(un) % 2 == 1:
    print("IGNORE HIM!")