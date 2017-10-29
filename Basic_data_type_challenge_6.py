if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    test=0
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    #to get specific students list of marks
    cal_list=student_marks[query_name]
    #to sum up list of marks
    for i in range(0,len(cal_list)):
        test=test+cal_list[i]
    #Calculate and round it to 2
    test=round(test/3,2)
    #dispaly in specific format
    print "%0.2f" % test
