if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    comb = []
    total_comb = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                ls = list((i, j, k))
                comb.append(ls)
                print(comb)
