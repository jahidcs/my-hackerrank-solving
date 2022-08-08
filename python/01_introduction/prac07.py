year = int(input())


def is_leap(x):
    leap = True
    if (x % 400 == 0 or x % 100 != 0) and x % 4 == 0:
        return leap
    else:
        return not leap


print(is_leap(year))
