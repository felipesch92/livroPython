s = float(input('Informe seu salário: R$ '))
if s > 1250:
    s = s * 1.1
else:
    s = s * 1.15
print(f'Seu novo salário é de: R$ {s:.2f}')
