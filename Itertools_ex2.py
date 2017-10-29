from itertools import *
#cycle function to repeat infinately
x=0;
for i in cycle(['x','y','z']):
    print i
    x=x+1;
    if(x==10):
       break;


#repeat function  repeat(to_repeat,no_of_times)


for i in repeat('python programming',5):
    print i


#including repeat in izip


for i in izip(repeat(3),['a','b','c']):
    print i
