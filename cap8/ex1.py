def maior(a, b):
    if a > b:
        return f'{a} é maior que {b}!'
    elif b > a:
        return f'{b} é maior que {a}!'
    else:
        return f'Os números são iguais!'


print(maior(15, 15))
