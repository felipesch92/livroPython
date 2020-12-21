v_d = float(input('Valor da dívida: R$ '))
j_m = float(input('Juro mensal: '))
v_m = float(input('Valor mensal que será pago: R$ '))
c_m = 0
x = 0
t = 0
v_i = v_d
while v_d > x:
    v_d += v_d * (j_m / 100)
    print(f'Restante R$ {v_d:.2f}')
    v_d -= v_m
    c_m += 1
    if v_m < v_d:
        t += v_m
    else:
        t += v_d
print(f'Você levou {c_m} mes(es) para pagar a dívida.')
print(f'Você pagou um total de R$ {t:.2f}')
print(f'Você pagou em juros R$ {t - v_i:.2f}')
