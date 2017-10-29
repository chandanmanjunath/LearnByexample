from itertools import *
print "**************************************************"
def test_val(x):
    print "test_val",x
    return (x<1)


for i in dropwhile(test_val,[-1,0,1,2,3,4,2,2]):
    print "infor",i

print "###############################################################"
def test_val(x):
    print "test_val",x
    return (x>2)


for i in takewhile(test_val,[3,4,5,-1,0,2]):
    print "infor",i
