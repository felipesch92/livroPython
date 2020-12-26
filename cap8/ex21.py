from random import randint
n = randint(1, 100)
for x in range(0, 3):
    n_t = int(input('Número: '))
    if n == n_t:
        print('Parabéns, você acertou!')
    else:
        print('Errou, tente novamente!')
print(n)