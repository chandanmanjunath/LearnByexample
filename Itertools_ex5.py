from itertools import *
from operator import itemgetter

d = dict(a=1, b=2, c=1, d=2, e=1, f=2, g=3)
#print d
#print list(d.iteritems())
#print d.items()
#print list(itemgetter(1))
di = sorted(d.iteritems(), key=itemgetter(1))#for each iteritems first indexed item considered for sorting
print di

for k, g in groupby(di, key=itemgetter(1)):#for each iteritems first indexed item considered for group by
    #print k, map(itemgetter(0), g)
    print k,list(g)

k=[('a',1),('b',2),('c',1)]
value=itemgetter(2)(k)
print value

#grouping makes sense only when items are sorted and grouped
