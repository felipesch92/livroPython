p = 0
q = 1
while q <= 3:
    r = input(f'Resposta da questão {q}: ').upper()
    if q == 1 and r == 'B':
        p += 1
    if q == 2 and r == 'A':
        p += 1
    if q == 3 and r == 'D':
        p += 1
    q += 1
print(f'O aluno fez {p} ponto(s)')
