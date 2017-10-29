from itertools import *

#lambda function and imap
def lambda_test(x):
         return lambda y:x+y
         #print x

temp=lambda_test(5)
temp(3)
print temp(3)


#imap
print "*****************************************************************************"
#range creates a list internally for evaluation
#xrange is a sequential object which is faster not create any list internally
for i in imap(lambda x:x*2,xrange(7)):
    print i
