# Imprimir a maior e menor temperatura, e a temperatura média.
t = [-10, -8, 0, 1, 2, 5, -2, -4]
maior = t[0]
menor = t[0]
s = 0
for x in t:
    if x > maior:
        maior = x
    if x < menor:
        menor = x
    s += x
print(f'A maior temperatura é de: {maior}')
print(f'A menor temperatura é de: {menor}')
print(f'A temperatura média e de: {s / len(t)}')
