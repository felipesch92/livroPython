estoque = {'tomate': [1000, 2.3],
           'alface': [500, 0.45],
           'batata': [2001, 1.2],
           'feijao': [100, 1.5]}
total = 0
while True:
    produto = input('Informe o produto: ')
    if produto in estoque:
        quantidade = int(input('Informe a quantidade: '))
        preco = estoque[produto][1]
        custo = quantidade * preco
        print(f'{produto}: {quantidade} x {preco} = {custo}')
        estoque[produto][0] -= quantidade
        total += custo
    else:
        print('Produto não encontrado no estoque.')
    continuar = input('Deseja continuar? [S/N]').upper()
    if continuar == 'N':
        break
print(f'Total a pagar: R$ {total:.2f}')
print('Estoque:')
for chave, dados in estoque.items():
    print(f'Descrição: {chave}')
    print(f'Quantidade: {dados[0]}')
    print(f'Preço: {dados[1]:6.2f}\n')
