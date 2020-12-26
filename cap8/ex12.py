def verifica():
    s = input('Continuar? ')
    if s in 'SsNn':
        return True
    else:
        print('Opção inválida.')
        verifica()


print(verifica())
