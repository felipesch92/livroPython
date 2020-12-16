m = float(input('Informe o valor da mercadoria: '))
d = float(input('Informe o desconto em %: '))
t = m - (m * d) / 100
print(f'O desconto foi de R$ {(m * d) / 100:.2f}')
print(f'O valor final é de R$ {t:.2f}')
