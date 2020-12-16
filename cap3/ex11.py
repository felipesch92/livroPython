#Perde 10 minutos de vida por cigarro. Informar quantos dias de vida perdeu
q_d = int(input('Quantos cigarros por dia: '))
q_a = int(input('Fumante por quantos anos? '))
# Total de cigarros
t_c = (q_d * q_a) * 364
# Total de dias perdidos.
q_d = (t_c * 10) / 60 / 24
print(f'Você perdeu {q_d // 1:.0f} dias de vida fumando!')
