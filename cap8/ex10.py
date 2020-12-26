def valida_str(s):
    if 5 <= len(s) <= 10:
        return True
    else:
        print(f'String com {len(s)} caracteres, fora do parametro aceito.')


nome = input('Nome: ')
if valida_str(nome):
    print(f'Olá, {nome}')
