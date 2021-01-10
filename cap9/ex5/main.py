def escreve():
    with open('arquivo.txt', 'w') as arq:
        for x in range(1, 101):
            arq.write(f'Linha {x}\n')


def imprime(a):
    with open(a, 'r') as arq:
        p = 1
        c_p = 1
        for x, l in enumerate(arq):
            if c_p == 20 or x == 0:
                print(f'--------Página {p}--------')
                p += 1
                c_p = 1
            c_p += 1
            print(l.replace('\n', ''))


imprime('arquivo4.txt')
