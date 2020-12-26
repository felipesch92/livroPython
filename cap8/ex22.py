import types
l = ['A', ['b', 'c', 'd'], 'e']
for x in l:
    if isinstance(type(x), str):
        print(x)
    else:
        for c in x:
            print(c)