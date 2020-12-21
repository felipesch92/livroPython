n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
t = 0
x = 1
while x <= n2:
    if x != n2:
        print(f'{n1} + ', end='')
    else:
        print(f'{n1} = ', end='')
    x += 1
    t += n1
print(t)
