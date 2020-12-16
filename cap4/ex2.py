maior = menor = 0
for x in range(0, 3):
    n = int(input('Informe um número: '))
    if x == 0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
