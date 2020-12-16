v = float(input('Informe sua velocidade: '))
m = 0
if v > 80:
    m = (v - 80) * 5
    print(f'Você foi multado em R$ {m:.2f}')
else:
    print('Você está na velocidade permitida.')
