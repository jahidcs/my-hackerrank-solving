def missingCharacters(s):
    # Write your code here
    missing_char = ""
    c = [
        "0", "1", "2", "3", '4',
        "5", '6', "7", '8', "9",
        "a", "b", "c", "d", "e",
        "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o",
        "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y",
        "z"
    ]
    for item in c:
        for char in s:
            if char == item:
                pass
            else:
                missing_char += item
                c.remove(item)

    print(missing_char)

    return missing_char


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = missingCharacters(s)

    # fptr.write(result + '\n')

    # fptr.close()
