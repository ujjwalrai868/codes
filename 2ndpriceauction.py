from numpy import *
import random
import array
import Gnuplot, Gnuplot.funcutils
a=array.array('i',[])
n=int(input("Enter the number of persons:"))  #no of persons
t=int(input("Enter the number of items:"))  #no of items
for i in range(n):
	x=random.randint(100,1000)
	a.append(x)
a=sorted(a)
for i in range(n):
	print(a[i])
print("payment is :")
print(a[n-t])
