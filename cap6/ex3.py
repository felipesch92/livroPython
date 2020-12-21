l1 = [1, 2, 3, 4, 5]
l2 = [2, 3, 4, 5, 6, 7, 8]
l3 = []
x = 0
while x < len(l1):
    l3.append(l1[x])
    x += 1
x = 0
while x < len(l2):
    if l2[x] not in l3:
        l3.append(l2[x])
    x += 1
print(l3)
