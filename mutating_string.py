def mutate_string(string, position, character):
    letters = list(string)
    letters[position] = character
    st = ''.join(letters)
    return st

if __name__ == '__main__':
    a=1