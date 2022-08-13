n = int(input())

lst = []

for i in range(n):
    x = input().split(' ')
    command = x[0]
    if command == 'insert':
        lst.insert(int(x[1]), int(x[2]))
    if command == 'remove':
        lst.remove(int(x[1]))
    if command == 'append':
        lst.append(int(x[1]))
    if command == 'sort':
        lst.sort()
    if command == 'pop':
        if len(lst) != 0:
            lst.pop()
    if command == 'reverse':
        lst.reverse()
    if command == 'print':
        print(lst)
        