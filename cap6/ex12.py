d = {}
palavra = 'Felipe Schmaedecke'
for l in palavra:
    if l in d:
        d[l] = d[l] + 1
    else:
        d[l] = 1
print(d)
