n = [0, 0, 0, 0, 0, 0, 0]
s = 0
x = 0
while x < 7:
    n[x] = float(input('Nota: '))
    s += n[x]
    x += 1
x = 0
while x < 7:
    print(f'Nota {x+1}: {n[x]}')
    x += 1
print(f'Média: {s/7:.2f}')
