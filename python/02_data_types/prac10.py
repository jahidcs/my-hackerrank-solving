if __name__ == '__main__':
    n = int(input())
    records = []
    scores = []
    min_sec = []
    for _ in range(n):
        name = input()
        score = float(input())
        records.append(list((name, score)))

    for i in range(n):
        scores.append(scores[i][1])
    for i in range(scores.count(min(scores))):
        scores.remove(min(scores))

    scores.sort()
    for i in range(len(records)):
        if scores[0] == records[i][1]:
            min_sec.append(records[i][0])
        else:
            pass

    min_sec.sort()
    for item in min_sec:
        print(item)

