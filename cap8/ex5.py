def pesquise(lista, valor):
    for x, e in enumerate(lista):
        if e == valor:
            return x
    return None


def soma(l):
    total = 0
    for e in l:
        total += e
    return total


def media(l):
    return soma(l) / len(l)


l = [10, 20, 25, 30]
print(pesquise(l, 10))
print(pesquise(l, 19))
print(pesquise(l, 30))
print(media(l))
print(soma(l))
