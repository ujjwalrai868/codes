from __future__ import division
from decimal import *
import numpy as np
import Gnuplot
import math
g=Gnuplot.Gnuplot(persist=1)
f1=open("di3.txt","a")
f2=open("di4.txt","a")
results = []
result2 = []
r1=[]
r2=[]
with open('abc.txt') as ab:
    for line in ab:
        results.append(int(line))
print 'dsic'
print results
n=sum(results)/100
k=math.ceil(n)
print ('k is:',k)
g1=Decimal(k)
print 'g1 is:'
print g1
if g1>1:
  f1.write('\t')
  f1.write(str(g1))
  f1.write('\n')
print 'n'

print '\n'

with open('abc1.txt') as a:
    for line in a:
         result2.append(int(line))
print 'random'
print result2
n1=sum(result2)/100
print n1
k1=math.ceil(n1)
g2=Decimal(k1)
print 'k1 is: '
print k1
print 'g2 is: '
print g2
if g2>=1:
  f2.write('\t')
  f2.write(str(g2))
  f2.write('\n')
print 'n1',k1

print 'dsic'
with open('di3.txt') as ab:
    for line in ab:
        r1.append(int(line))
print 'r1 is: ',r1
print r1
print '\n'

print 'random'
with open('di4.txt') as ab:
    for line in ab:
        r2.append(int(line))
print 'r2 is: ',r2
x=[50,100,150,200]
g('set xtics ("5" 0, "10" 1, "15" 2, "20" 3) ')
g('set title "House Allocation"')
g('set xlabel "Agents"')
g('set ylabel "Deviation"')
g('set xrange [0:5]')
g('set yrange [0:300]')
d1 = Gnuplot.PlotItems.Data(r1, with_="lp", title='DSIC')
d2 = Gnuplot.PlotItems.Data(r2, with_="lp", title='Random')
g.plot(d1,d2)
f1.close()
f2.close()


