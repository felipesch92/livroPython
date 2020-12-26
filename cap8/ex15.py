def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def imprime(a, b, foper):
    print(foper(a, b))


imprime(10, 15, subtracao)
