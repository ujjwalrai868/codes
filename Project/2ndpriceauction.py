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
g=Gnuplot.Gnuplot(debug=1)
g.title('2nd Price Auction')
x=arange(a[n-t], dtype='float_')
y=n
d = Gnuplot.Data(x, y,
                     title='calculated by python',
                     with_='points 3 3')