if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    mark=student_marks[query_name]
    mark_avg=(mark[0]+mark[1]+mark[2])/3
    print('%.2f' %mark_avg)

