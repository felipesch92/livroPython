v = float(input('Qual o valor do imóvel? R$ '))
s = float(input('Informe seu salário R$ '))
a = int(input('Financiar em quantos anos? '))
# Prestação
p = v / (a * 12)
# porcentagem do salário
if (s * 0.3) > p:
    print('Parabéns, financiamento aprovado.')
else:
    print('A prestação fica maior que 30% do seu salário, financiamento reprovado.')
print(f'Salário: R$ {s:.2f} - Prestação: R$ {p:.2f}')
