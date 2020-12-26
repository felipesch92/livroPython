def barra(n=10, c='*'):
    print(c * n)


l = [[5, '-'], [15, '.'], [20, '_'], [30, '%']]
for e in l:
    barra(*e)
