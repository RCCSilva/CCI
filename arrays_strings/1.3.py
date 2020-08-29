def urlfy(string: str) -> str:
    string = list(string)
    i = len(string) - 1
    j = first_non_space(string)

    space_values = []

    while i > 0 and j >= 0:
        while space_values:
            string[i] = space_values.pop()
            i -= 1

        if string[j] == ' ':
            space_values = ['%', '2', '0']
        elif i >= 0 and j >= 0:
            string[i], string[j] = string[j], string[i]

            i -= 1
        j -= 1

    return ''.join(string)

def first_non_space(string: str) -> int:
    j = len(string) - 2
    while string[j] == ' ' and j > 0:
        j -= 1

    return j


if __name__ == '__main__':
    print(urlfy('my first test    '))

