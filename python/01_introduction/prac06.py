n = int(input())
text = ''


def print_func(s, x):
    s = ''
    for i in range(x+1):
        if i == 0:
            i += 1
        else:
            si = str(i)
            s += si
    return s


print(print_func(text, n))
