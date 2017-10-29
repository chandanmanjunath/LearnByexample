from collections import defaultdict

s = 'mississippi'
d = defaultdict(int)
print list(d)
for k in s:
     d[k] += 1
print d.items()
