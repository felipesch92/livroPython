jogo = [[], [], []], [[], [], []], [[], [], []]
cont = 0
contx = conto = contxc = contoc  = 0
while True:
    l = int(input('Informe a linha: '))
    c = int(input('Informe a coluna: '))
    if l < 4 and c < 4:
        if cont % 2 == 0:
            jogo[l-1][c-1] = 'X'
        else:
            jogo[l-1][c-1] = 'O'
        cont += 1
        for x in range(0, 3):
            for j in jogo[x]:
                if j == 'X':
                    contx += 1
                if j == 'O':
                    conto +=1
            for k in range(0, 3):
                if jogo[k][x] == 'X':
                    contxc += 1
                if jogo[k][x] == 'O':
                    contoc += 1
            print(jogo[x])
            if jogo[0][0] == 'X' and jogo[1][1] == 'X' and jogo[2][2] == 'X':
                print(jogo[x + 1])
                print(jogo[x + 2])
                print(f'Parabéns, X venceu!')
                break
            if jogo[0][0] == 'O' and jogo[1][1] == 'O' and jogo[2][2] == 'O':
                print(jogo[x + 1])
                print(jogo[x + 2])
                print(f'Parabéns, X venceu!')
                break
            if jogo[0][2] == 'X' and jogo[1][1] == 'X' and jogo[2][0] == 'X':
                print(jogo[x + 1])
                print(jogo[x + 2])
                print(f'Parabéns, X venceu!')
                break
            if jogo[0][2] == 'O' and jogo[1][1] == 'O' and jogo[2][0] == 'O':
                print(jogo[x + 1])
                print(jogo[x + 2])
                print(f'Parabéns, X venceu!')
                break
            if contx == 3 or contxc == 3:
                print(jogo[x+1])
                print(f'Parabéns, X venceu!')
                break
            if conto == 3 or contoc == 3:
                print(jogo[x+1])
                print(f'Parabéns, O venceu!')
                break
            contx = conto = contxc = contoc = 0
    else:
        print('Posição já preenchida')
