password = input()
password_set = set(password)

n = int(input())

guessed_string = ""
left_guess_set = set()
right_guess_set = set()


for _ in range(n):
    kash_guess = input()
    left_guess_set.add(kash_guess[0])
    right_guess_set.add(kash_guess[1])

    


if password[0] in right_guess_set and password[-1] in left_guess_set:
    print("YES")

else:
    print("NO")