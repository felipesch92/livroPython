p = [1, 4, 9, 10, 20, 25]
e1 = int(input('Primeiro elemento: '))
e2 = int(input('Segundo elemento: '))
x = 0
achou = False
primeiro = 0
while x < len(p):
    if p[x] == e1:
        print(f'Elemento 1 encontrado na posição {x} da lista!')
        if primeiro == 0:
            primeiro = 1
    if p[x] == e2:
        print(f'Elemento 2 encontrado na posição {x} da lista!')
        if primeiro == 0:
            primeiro = 2
    x += 1
print(f'Foi encontrado primeiro o {primeiro} elemento!')
