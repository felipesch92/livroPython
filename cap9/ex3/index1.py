with open('multiplos4.txt', 'w') as multiplos:
    pares = open('pares.txt')
    for l in pares.readlines():
        num = l.replace('\n', '')
        if int(num) % 4 == 0:
            multiplos.write(f'{num}\n')
