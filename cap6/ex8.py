v = [9, 8, 7, 12, 0, 13, 21]
p = []
i = []
for x in v:
    if x % 2 == 0:
        p.append(x)
    else:
        i.append(x)
print(f'Números pares: {p}')
print(f'Números ímpares: {i}')
