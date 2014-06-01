from copy import *
import time
import datetime
import dateutil

class way:
    right = 0
    down = 0


class counter:
    count = 0


def go_further(path=way(), c=counter(), max=20):
    if path.right == max or path.down == max:
        c.count += 1
        #if c.count%100000==0:
            #print c.count
        return
    path.down += 1
    go_further(path, c, max)
    path.down -= 1
    path.right += 1
    go_further(path, c, max)
    path.right -= 1


c = counter()
for n in range(20,21):
    start = time.time()
    go_further(way(), c,n)
    duration = time.time()-start
    print str(n)+" "+str(c.count)+" "+str(duration)
    c.count = 0