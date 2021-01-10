with open('pares.txt', 'w') as pares, open('impares.txt', 'w') as impares:
    for x in range(0, 1001):
        if x % 2 == 0:
            pares.write(f'{x}\n')
        else:
            impares.write(f'{x}\n')
