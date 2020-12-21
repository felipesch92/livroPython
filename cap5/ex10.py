c = {
    1: 0.5,
    2: 1,
    3: 4,
    5: 7,
    9: 8
}
s = 0
while True:
    op = int(input('Código do produto: '))
    if op in c:
        q = float(input('Quantidade: '))
        s += q * c[op]
    if op == 0:
        break
print(f'O valor total dos produtos é de R$ {s:.2f}')
