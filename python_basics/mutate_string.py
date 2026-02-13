def mutate_string(string, position, character):
    str_list = list(string)
    str_list[position] = character
    
    answer = "".join(str_list)
    return answer

if __name__ == '__main__':
