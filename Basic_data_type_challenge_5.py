from operator import itemgetter
from itertools import groupby
grade_list=[]
students=[]
temp=[]
k=1
n=int(raw_input())
if n >=2 and n <=5:
    j=0
    for j in range(0,n):
        #print j
        name = raw_input()
        score = float(raw_input())
        grade_list.insert(j,name)
        grade_list.insert(j+1,score)
        students.insert(j,grade_list)
        grade_list=[]

second_highest = sorted(list(set([marks for name, marks in students])))[1]
print('\n'.join([a for a,b in sorted(students) if b == second_highest]))
