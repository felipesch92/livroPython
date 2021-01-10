def escreve():
    with open('arquivo3.txt', 'w') as arq:
        for x in range(0, 20):
            arq.write(f'Celular{x}\n')


def ler(a):
    arq = open(a)
    for l in arq.readlines():
        print(l.replace('\n', ''))


ler('arquivo1.txt')
ler('arquivo2.txt')
ler('arquivo3.txt')
ler('arquivo4.txt')
