from collections import Counter
e=Counter()
with open('F:\chandan\mystuff\Collections\words.txt','rt') as f:
        for line in f:
            e.update(line.rstrip().upper())

print e.most_common(3)


#most_common 5 values used
for key,value in e.most_common(5):
    print "%s -> %s" % (key,value)
