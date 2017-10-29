from collections import deque

#can insert the elements on either of sides
print deque('abacde')


a=deque('jdsadasfgajs')

print a[0]
print len(a)
print a[11]
print a[-1]

#append rt(only append)

a.append('xyxxxx')

print len(a)
print a[12]


a.remove('xyxxxx')
print len(a)


a.extend('xyxxxx')
print len(a)
print a[17]

a.extendleft('yyyyyyyy')
print len(a)
print a[0]


a.appendleft('z')
print len(a)
print a[0]
