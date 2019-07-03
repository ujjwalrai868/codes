import random
import operator
import copy
from decimal import Decimal
cpu={}
no_allocations=0
for i in range(24):
	cpu[i]=0
class greedy:
	def __init__(R,W,T,A,D):
		R.W=W
		R.A=A
		R.D=D
		R.T=T
	def capacity(R):
		return 1000
	def price(R):
		fixed_price=10
		total_cost=R.W*fixed_price
		return total_cost
	def if_schedule_possible(R):
		count=0
		for t in range(R.A,R.D-R.T+1):
			for start_time in range(t,t+R.T):
				print 'cpu[t]+R.W is:',cpu[t]+R.W
				print 'capacity is:',R.capacity()
				if cpu[t]+R.W<R.capacity():
					print'inside if'
					count+=1
					print count
					if count==R.T:
						return start_time-R.T+1
				else:
					print 'inside else'
					if count<R.W:
						count=0
					print count
		if count<R.T:
			print 'returning -1'
			return -1
	def make_reservation(R):
		global no_allocations
		s=R.if_schedule_possible()
		#print 's is:',s
		if s!=-1:
			print 'scheduled from',s,'to',s+R.T
			#print 'price is:',R.price()
			no_allocations+=1
			#print 'no_allocations is:',no_allocations
			for i in range(s,s+R.T):
				cpu[i]=cpu[i]+R.W
		else:
			print 'not possible'''
no_of_users=input("Enter number of types of requests:")
for i in range(no_of_users):
	#inpt=input("Enter number of requests:")
	inpt=100
	no_reso=input("number of cpu required:")
	arrival_time=input("Enter arrival_time:")
	departure_time=input("Enter departure_time:")
	req_time=input("Enter req_time:")
	for j in range(inpt):
		r=greedy(no_reso,req_time,arrival_time,departure_time)
		r.make_reservation()
	print 'cpu is:',cpu
	print 'no_allocations is:',no_allocations