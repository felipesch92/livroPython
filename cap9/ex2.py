def ler(arq, i, f):
    arq = open(arq, 'r')
    try:
        c = 1
        for l in arq.readlines():
            if c >= i:
                print(l.replace('\n', ''))
            if f == c:
                break
            c += 1
    except Exception as erro:
        print(erro)


#a = input('Digite o nome do arquivo4.txt a ser impresso: ')
a = 'nomes.txt'
i = 2
f = 4
ler(a, i, f)
