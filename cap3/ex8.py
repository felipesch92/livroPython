km = float(input('Informe a distância em KM: '))
v = float(input('Informe a velocidade média: '))
t = km / v
t_h = t // 1
t_m = (t - t_h) * 60
print(f'O tempo da viagem será de {t_h:.0f} horas e {t_m:.0f} minutos.')
