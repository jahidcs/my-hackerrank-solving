if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))

    flag = 0

    for i in range(len(scores)):
        for j in range(len(scores) - 1):
            if scores[j] < scores[j + 1]:
                flag = scores[j]
                scores[j] = scores[j + 1]
                scores[j + 1] = flag

    for i in range(len(scores) - 1):
        if scores[i] != scores[i + 1]:
            runner_up = scores[i + 1]
            print(runner_up)
            break
