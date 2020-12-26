l_num1 = [1, 2, 3, 4, 5]
l_num2 = [3, 4, 5, 6, 7]
for n in l_num1:
    if n in l_num2:
        print(f'Números comuns as duas listas: {n}')
    else:
        print(f'Números que só existem na primeira lista: {n}')
for n in l_num2:
    if n not in l_num1:
        print(f'Números que só existem na segunda lista: {n}')