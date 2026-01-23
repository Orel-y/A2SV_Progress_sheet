def swap_case(s):
    str = []
    for char in s:
        current_char = ord(char)
        if 65 <= current_char <= 90:
            str.append(char.lower())
        elif 90 <= current_char <= 122:
            str.append(char.upper())
        else:
            str.append(char)
    return ''.join(str)

# capitals start from 65 and end at 90
# small start from 97 and end at 122

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
