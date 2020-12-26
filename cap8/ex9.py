def fibonacci(n):
    anterior = antepenultimo = tmp = 0
    atual = 1
    print(anterior)
    for x in range(0, n):
        print(atual)
        tmp = atual
        antepenultimo = anterior
        anterior = tmp
        atual = anterior + antepenultimo


print(fibonacci(10))
