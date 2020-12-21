v_i = float(input('Valor inicial R$: '))
v_m = float(input('Valor mensal a ser depositado: '))
t_j = float(input('Informe a taxa de juros: '))
v_f = v_i
v_j = 0
x = 1
while x <= 24:
    v_j = v_f * (t_j / 100)
    print(f'Mês {x} - Valor: R$ {v_f} Juros R$: {v_j:.2f}')
    v_f += v_m
    x += 1
print(f'Valor final com juros: {v_f:.2f}')
