q = float(input('Informe a KW consumida: '))
t = input('Informe o tipo de instalação: [R] [C] [I] ').upper()[0]
v = 0
if t == 'R':
    if q <= 500:
        v = q * 0.4
    else:
        v = q * 0.65
elif t == 'C':
    if q <= 1000:
        v = q * 0.55
    else:
        v = q * 0.60
elif t == 'I':
    if q <= 5000:
        v = q * 0.55
    else:
        v = q * 0.60
else:
    print('Opção inválida.')
print(f'Seu tipo de instalação é {t}, seu consumo foi de {q} KW total R$: {v:.2f}')
