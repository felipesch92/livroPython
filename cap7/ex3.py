nome1 = 'Felipe'
nome2 = 'Schmaedecke'
for n in nome1:
    if n not in nome2:
        print(n, end=' ')
for n in nome2:
    if n not in nome1:
        print(n, end=' ')
