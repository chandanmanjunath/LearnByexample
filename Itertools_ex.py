#Itertools
from itertools import *
#chain

for i in chain([1,2,3],['a','b','c']):
    print i

#izip
print "**********************************************************"
for i in izip([1,2,3],['a','b','c','d','e']):
    print i

#Difference between zip and izip
#zip will have exact list ,izip is having an instane
#Check with isinstance
#izip can be used for better performance since it is having only instance

#To get elements of first list and second list
print "##########################################"
for i,j in izip([1,2,3],['a','b','c','d','e']):
    print i,j

#syntax :islice(function,start,end,step)

print "???????????????????????????????????????????????????????"

for i in islice(count(),5):
    print i


print "???????????????????????????????????????????????????????"

for i in islice(count(),3,7):
    print i

print "???????????????????????????????????????????????????????"

for i in islice(count(),10,100,10):
    print i


#tee function is used to get multiples groups of values returned by islice
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
r=islice(count(),5,10)

t1,t2=tee(r)

for i in t1:
    print i

for i in t2:
    print i
