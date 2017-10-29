from collections import deque


a=deque('sdhfafakak')

while True:
    try:

        print a.pop()

    except IndexError:
        break;


print "**********************"
a=deque('sdhfafakak')
while True:
    try:

        print a.popleft()

    except IndexError:
        break;
