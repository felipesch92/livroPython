def soma(*args):
    s = 0
    for x in args:
        s += x
    return s


print(soma(1, 5, 10, 30))
print(soma(5, 8, 20))
print(soma(2, 4, 2))
