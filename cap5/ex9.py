c = 0
s = 0
while True:
    n = int(input('Número: '))
    if n == 0:
        break
    c += 1
    s += n
print(f'{c} Números digitados Soma: {s} Média: {s / c:.2f}')
