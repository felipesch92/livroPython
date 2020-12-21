while True:
    op = int(input('[1] Adição [2] Subtração [3] Divisão [4] Multiplicação [0] Sair '))
    if op == 0:
        break
    n1 = float(input('Número 1: '))
    n2 = float(input('Número 2: '))
    if op == 1:
        r = n1 + n2
    elif op == 2:
        r = n1 - n2
    elif op == 3:
        r = n1 / n2
    elif op == 4:
        r = n1 * n2
    else:
        print('Opção inválida!')
    x = 1
    while x <= 10:
        print(f'{r:.2f} x {x} = {r * x:.2f}')
        x += 1
