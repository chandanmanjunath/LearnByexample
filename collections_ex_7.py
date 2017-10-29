import collections
import threading
import time

test_queue=collections.deque(xrange(11))


def trial_fun(direction,next_arg):
    while True:

      try:
          next=next_arg()
      except IndexError:
          break;
      else :
         print "%s direction %s removed" % (direction,next)
         time.sleep(0.1)
    print "%s done" % (direction)
    return


l1=threading.Thread(target=trial_fun,args=('left',test_queue.popleft))
l2=threading.Thread(target=trial_fun,args=('right',test_queue.pop))

l1.start()
#l1.join()
l2.start()
#l2.join()

l1.join()
l2.join()
