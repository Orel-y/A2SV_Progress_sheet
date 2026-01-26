n: int = int(input())
words_list = [input() for _ in range(n)]

for word in words_list:
    if len(word) > 10:
        print(f"{word[0]}{len(word)-2}{word[-1]}")
    else:
        print(word)