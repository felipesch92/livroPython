def soma(a, b):
    return a + b


def epar(x):
    return x % 2 == 0


def par_impar(x):
    if epar(x):
        return 'Par'
    else:
        return 'Impar'


print(par_impar(30))
print(par_impar(29))