#map
print "**************************************"
from itertools import *
from math import *

integers = [1,2,3,4,5]
sqr_ints = map(sqrt, integers)
print (sqr_ints)

print "############################################"
#imap
from itertools import *
from math import *

integers = [1,2,3,4,5]
sqr_ints = imap(sqrt, integers)
print list(sqr_ints)
