# ler quantidade de dias, horas, minutos e segundos e calcular o total em segundos.
d = int(input('Dias: '))
h = int(input('Horas: ')) + (d * 24)
m = int(input('Minutos: ')) + (h * 60)
s = int(input('Segundos: ')) + (m * 60)
print(f'Segundos: {s}')
