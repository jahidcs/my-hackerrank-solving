if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks_total = 0

    for item in student_marks[query_name]:
        marks_total += item
    result = marks_total / 3
    print("{:.2f}".format(result))
