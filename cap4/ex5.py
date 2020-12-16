n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
r = 0
op = int(input('[0]-Soma [1]-Subtração [2]-Multiplicação [3]-Divisão '))
if op == 0:
    r = n1 + n2
elif op == 1:
    r = n1 - n2
elif op == 2:
    r = n1 * n2
elif op == 3:
    r = n1 / n2
else:
    print('Opção inválida')
if op < 4:
    print(f'Resultado: {r} ')
