import collections

d={}

d['a']='A'
d['b']='B'
d['c']='C'

for k,v in d.items():
    print k,v

print "*"*100
e=collections.OrderedDict()

e['a']='A'
e['b']='B'
e['c']='C'
e['e']='E'
e['d']='D'

for k,v in e.items():
    print k,v
