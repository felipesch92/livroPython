a = 5
def muda():
    global a
    a = 7
    print(f'A dentro da função: {a}')
    return a


print(f'A antes de mudar: {a}')
muda()
print(f'A depois de mudar: {a}')
