def split_and_join(sentence):
    lst = sentence.split(" ")
    resultant_str = ""
    for item in lst:
        if item == lst[-1]:
            resultant_str += item
        else:
            resultant_str += item + "-"
    return resultant_str


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
