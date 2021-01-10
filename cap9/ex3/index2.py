with open('pares.txt', 'r') as pares, open('impares.txt', 'r') as impares, open('pareseimpares.txt', 'w') as pareseimpares:
    l_p = pares.readlines()
    l_i = impares.readlines()
    for i in range(0, 500):
        p = l_p[i]
        i = l_i[i]
        pareseimpares.write(p)
        pareseimpares.write(i)
