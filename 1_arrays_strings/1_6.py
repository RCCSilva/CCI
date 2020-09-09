def compress(s: str) -> str:
    if len(s) < 2:
        return s

    string = list(s)

    i = 0
    j = 1

    c = 1
    b = string[i]

    while j < len(string) - 1 and i < len(string) - 1:
        while string[j] == b and j < len(string) - 1:
            j += 1
            c += 1
        string[i] = b
        b = string[j]    
        i += 1
        string[i] = str(c)
        i += 1
        c = 1
    
    if i == j:
        return s
    else:
        return ''.join(string[:i])

if __name__ == '__main__':
    print(compress('aaaaaabbcccccccccccccccccc'))
    print(compress('ab'))
