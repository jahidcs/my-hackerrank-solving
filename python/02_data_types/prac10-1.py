n = int(input())
x = []
x1 = []
x2 = []
for i in range(n):
    n1 = input()
    n2 = float(input())
    this = list((n1, n2))
    x.insert(i, this)

print(x)
for i in range(n):
    x1.append(x[i][1])
for i in range(x1.count(min(x1))):
    x1.remove(min(x1))

print(x1)
x1.sort()
for i in range(n):
    if x1[0] == x[i][1]:
        x2.append(x[i][0])
    else:
        pass

x2.sort()
for item in x2:
    print(item)
