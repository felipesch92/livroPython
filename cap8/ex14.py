def soma(a, b, imprime=False):
    s = a + b
    if imprime:
        print(s)
    return s
teste = soma(10, 15)
print(teste)
soma(30, 1500, True)
