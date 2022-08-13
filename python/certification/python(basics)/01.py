def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    x = sentence.split(" ")
    resultant_str = ""
    x.reverse()
    for item in x:
        if item == x[-1]:
            resultant_str += item
        else:
            resultant_str += item + " "

    return resultant_str.swapcase()


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
