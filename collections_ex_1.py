#passing elements to collections
from collections import Counter
#Sequence
print Counter('aaaaaaaaaaaaabbccdde')

#list
print Counter(['a','a','a','b'])

#dictionary

print Counter({'a':4,'b':60})

#assiging values with =
print Counter(a=1,b=10)

#declare and initialize with none
c=Counter()

#update values
c.update(a=1,b=4)

print c

c.update(['a','a','a'])

print c


#retriving/accessing using for loop


for values in 'ab':
    print "%s : %d" % (values,c[values])#accessing values from a dictionary using keys


#declare dictionary

a={'x':1,'y':2}

for item in a:
    print item,a[item]


#elements method in collections
d=Counter('fhdvfavasvaskfvaskfqdvdfqv')

print list(d.elements())
