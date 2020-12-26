letras = {'F': 1,
          'e': 2,
          'l': 3,
          'i': 4,
          'p': 2}
total = 0
nome = input('Nome: ')
for l in nome:
    if l in letras:
        total += letras[l]
print(f'Total: {total}')
