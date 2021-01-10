larg = 79
with open('entrada.txt') as entrada:
    for l in entrada.readlines():
        if l[0] == ';':
            continue
        elif l[0] == '>':
            print(l[1:].rjust(larg))
        elif l[0] == '*':
            print(l[1:].center(larg))
        elif l[0] == '=':
            print(f'{l * 40}')
        else:
            print(l)
