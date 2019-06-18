import copy
import random
num=5
a=a=[ x for x in range(num+1,num*2+1) ]
random.shuffle(a)
print a
random.shuffle(a)
print a
pre=[[0]]
pre.append(a)
pre.append(a)
random.shuffle(a)
pre.append(a)
print pre
a.append(0)
print 'a is: '
print a
print 'pre is: '
pre.append(a)
print pre