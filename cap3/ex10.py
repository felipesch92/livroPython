km = float(input('Informe a KM percorrida: ')) # 0.15
d = int(input('Informe quantos dias: ')) # 60
print(f'{d} dias e {km} km rodados. Valor final: R$ {(km * 0.15) + (d * 60):.2f}')
