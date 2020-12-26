nome = 'Banana'
nome_l = {}
for n in nome:
    if n in nome_l:
        nome_l[n] += 1
    else:
        nome_l[n] = 1
print(nome_l)
