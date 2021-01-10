with open('pares.txt', 'r') as pares:
    l_p = pares.readlines()
    pares.close()
with open('pares.txt', 'w') as pares:
    for x in range(len(l_p)-1, 0, -1):
        pares.write(l_p[x])
