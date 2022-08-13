def swap_case(sentence):
    sentence_lst = sentence.split(" ")
    resultant_str = ""
    for item in sentence_lst:
        if item == sentence_lst[-1]:
            resultant_str += item
        else:
            resultant_str += item + " "

    return resultant_str.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
