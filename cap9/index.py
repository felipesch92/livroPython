def escrever():
    arquivo = open('numeros.txt', 'w')
    for linha in range(1, 101):
        arquivo.write(f'{linha}\n')
    arquivo.close()


def ler():
    arq = open('numeros.txt', 'r')
    for l in arq.readlines():
        print(l.replace('\n', ''))
    arq.close()


def ler_with():
    with open('numeros.txt', 'r') as arq:
        for l in arq.readlines():
            print(l.replace('\n', ''), end=' ')


escrever()
ler()
ler_with()
