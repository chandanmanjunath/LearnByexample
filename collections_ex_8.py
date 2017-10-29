import collections

d=collections.deque([1,2,3,4,5,6,7])

print d

d.rotate(2)
print d
d=collections.deque([1,2,3,4,5,6,7])

d.rotate(-2)
print d
