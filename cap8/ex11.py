def verifica(l, s):
    if s in l:
        return True
    else:
        return False


l = [1, 5, 10, 20, 25]
print(verifica(l, 26))
