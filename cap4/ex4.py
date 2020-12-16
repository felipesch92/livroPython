km = int(input('Informe a distância em KM: '))
v = 0
if km <= 200:
    v = km * 0.50
else:
    v = km * 0.45
print(f'O valor de sua passagem é de R$ {v:.2f}')
