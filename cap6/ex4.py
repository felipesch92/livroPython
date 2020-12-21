u = 10
f = list(range(1, u+1))
while True:
    print(f'Existem {len(f)} clientes na fila')
    print(f'Fila atual: {f}')
    print('Digite F para adicionar um cliente ao fim da fila,')
    print('ou A para realizar o atendimento. S para sair.')
    op = input('Operação (F, A ou S): ').upper()
    if op == "A":
        if len(f) > 0:
            a = f.pop(0)
            print(f'Cliente {a} atendido')
        else:
            print('Fila vazia! ninguém para atender.')
    elif op == 'F':
        u += 1 # Incrementa o ticket do novo cliente
        f.append(u)
    elif op == 'S':
        break
    else:
        print('Operação inválida! Digite apenas F, A ou S!')
