import collections
#Normal tuples

x=('Chandan',23,'Male')

print x
print x[0]


#named tuples
#This can be accessed through index or name
d=collections.namedtuple('Person','name age gender')

chandan=d(name='Chandan',age=21,gender='Male')


print chandan
print chandan.name
print chandan.age

#errors in declaration can be catched like


try:
    e=collections.namedtuple('Test','Qst Ans sol Ans')

except ValueError,err:
    print "error encountered-->",err
#Renaming of fields at run time
e=collections.namedtuple('Test','Qst Ans sol Ans',rename='True')

#To get field values
print e._fields
