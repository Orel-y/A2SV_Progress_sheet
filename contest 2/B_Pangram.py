n = int(input())
word = input()

set_of_word = set(word.lower())

if len(set_of_word) >= 26:
    print("YES")
elif len(set_of_word) < 26:
    print("NO")