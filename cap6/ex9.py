l = [3, 1, 3, 4, 5, 2]
l.sort()
print(l)
fim = len(l)
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if l[x] < l[x + 1]:
            trocou = True
            temp = l[x]
            l[x] = l[x + 1]
            l[x + 1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1
for e in l:
    print(e, end=' ')
