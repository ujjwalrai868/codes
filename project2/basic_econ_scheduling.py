import random
import operator
from decimal import Decimal
temp=[]
temp_price=[]
promised_cpu=0
promised_space=0
promised_cores=0
total_cost=0
promised=0
payment=0
totalCost=[]
alloction_records_cpu=[]
allocation_records_cores=[]
allocation_records_space=[]
lp_service_prviders=[]
allocated_hours_cpu=[]
allocated_hours_space=[]
allocated_hours_cores=[]
cpu={}
cores={}
space={}
bids={}
for i in range(24):
	cpu[i]=0
	cores[i]=0
	space[i]=0
'''print cpu
print space
print cores'''
for i in range(10):
	lp_service_prviders.append(i+1)
class basic_econ_scheduling:
	def __init__(R,W,T,A,D,V,TR):
		R.W=W
		R.T=T
		R.A=A
		R.D=D
		R.V=V
		R.TR=TR
	def capacity(self):
		if self.TR=='cores':
			return 50
		elif self.TR=='CPU' or 'cpu':
			return 70
		elif self.TR=='space':
			return 60
	def can_be_completed(self):
		ran=int(random.random()*100)%100
		if ran>50:
			return True
		else:
			return False
	def demand(R):
		return int(random.random()*100)%100
	def decide(R,totalCost,V,factor):
		global payment
		print 'our price is:',min(totalCost)/factor
		payment=min(totalCost)/factor
		#print 'valuation is: ',V
		if min(totalCost)/factor<=V:
			#print 'accepted!'
			for i in range(len(totalCost)):
				if totalCost[i]==min(totalCost):
					return i
		else:
			print 'sorry,rejected!'
			return -1
	def generate_bid(self,lp_service_prviders,avg_bid):
		for service_providers in lp_service_prviders:
			bids[service_providers]=int(random.random()*10000)%avg_bid
			if bids[service_providers]<avg_bid/2:
				bids[service_providers]=bids[service_providers]+avg_bid/3
	def allocate_low_p(self,avg_bid):
		self.generate_bid(lp_service_prviders,avg_bid)
		print bids
		k=min(bids.iteritems(),key=operator.itemgetter(1))[0]
		t=k
		s=max(bids.iteritems(),key=operator.itemgetter(1))[0]
		bids[k]=bids[s]
		m=min(bids.iteritems(),key=operator.itemgetter(1))[0]
		print 'payment will be:',bids[m]
		return t
	def execute(self,avg_bid):
		if self.can_be_completed()==False:
				k=self.allocate_low_p(avg_bid)
				print k,'is allocated for further task'

	def make_reservaton(R):
		global total_cost
		global promised
		global promised_cpu
		global count
		global mini
		global promised_cores
		global promised_space
		global iden_var
		global payment
		totalCost=[]
		mini=0
		count=0
		total_cost=0
		promised=0
		cost=[]
		if R.TR=='cores':
			resource_price=2
			factor=200
			d1=Decimal(resource_price)/factor
			print 'per unit price of cores is:',round(d1,4)
		elif R.TR=='CPU' or 'cpu':
			resource_price=3
			factor=150
			d1=Decimal(resource_price)/factor
			print 'per unit price of CPU is:',round(d1,4)
		elif R.TR=='space':
			resource_price=1
			factor=300
			d1=d1=Decimal(resource_price)/factor
			print 'per unit price of space is:',round(d1,4)
		print 'calculating price...'
		for t in range(R.D-R.A+1):
			temp_price=[]
			d=R.demand()  #demand estimate function
			#print 't is: ',t
			#print 'd is: ',d
			if R.TR=='CPU' or 'cpu':
				promised=cpu[R.A/3600+(t/3600)]
			elif R.TR=='space':
				promised=space[R.A/3600+(t/3600)]
			elif R.TR=='cores':
				promised=cores[R.A/3600+(t/3600)]
			price=0
			for i in range(R.W):
				c=R.capacity()
				if d+promised+i+1>c:
					p=resource_price
				else:
					p=2
				temp_price.append(p)
				#print 'p is: ',p
				#print 'price is:',temp_price
				price=price+p
			cost.append(price)
			#print 'cost is: ',cost
		for i in range(R.A,R.D-R.T+1):
			total_cost=0
			for t in range(i,i+R.T):
				#print 't is: ',t
				count+=1
				total_cost=total_cost+cost[t-R.A]
				#print 'total_cost is: ',total_cost
			totalCost.append(total_cost)
		#print 'min is: ',min(totalCost)
		k=R.decide(totalCost,R.V,factor)
		#print 'k is: ',k
		if k!=-1:
			if R.TR=='CPU' or 'cpu':
					iden_var=0
					temp=[]
					for allocated_hours in range((R.A+k)/3600,((R.A+k+R.T)/3600)):
						allocated_hours_cpu.append(allocated_hours)
						cpu[allocated_hours]=cpu[allocated_hours]+R.W
						if cpu[allocated_hours]>R.capacity():
							for allocated_hours in range((R.A+k)/3600,((R.A+k+R.T)/3600)):
								cpu[allocated_hours]=cpu[allocated_hours]-R.W
							iden_var=-56
					if iden_var==-56:
						return 'reject'
					print allocated_hours_cpu
					#print 'R.capacity is: ',R.capacity()
					if cpu[allocated_hours]>R.capacity():
						for allocated_hours in range((R.A+k)/3600,((R.A+k+R.T)/3600)):
							allocated_hours_cpu.append(allocated_hours)
							cpu[allocated_hours]=cpu[allocated_hours]-R.W
						return 'reject'
					#print cpu
					print 'accepted at a payment of:',payment
					avg_bid=payment/(R.T/3600)
					print 'allocated time will be from',(R.A+k)/3600,'to',(R.A+k+R.T)/3600
					temp.append((R.A+k)/3600)
					temp.append((R.A+k+R.T)/3600)
					alloction_records_cpu.append(temp)
					print 'alloction_records_cpu is:',alloction_records_cpu
					promised_cpu=promised_cpu+R.W
					#print 'promised_cpu are:',promised_cpu
					R.execute(avg_bid)
			elif R.TR=='cores':
					temp=[]
					iden_var=0
					for allocated_hours in range((R.A+k)/3600,((R.A+k+R.T)/3600)):
						allocated_hours_cores.append(allocated_hours)
						cores[allocated_hours]=cores[allocated_hours]+R.W
						if cores[allocated_hours]>R.capacity():
							cores[allocated_hours]=cores[allocated_hours]-R.W
							iden_var=-56
					if iden_var==-56:
						return 'reject'
					print allocated_hours_cores
					print cores
					print 'accepted at a payment of:',payment
					print 'allocated time will be from',(R.A+k)/3600,'to',(R.A+k+R.T)/3600
					temp.append((R.A+k)/3600)
					temp.append((R.A+k+R.T)/3600)
					allocation_records_cores.append(temp)
					promised_cores=promised_cores+R.W
					#print 'promised_cores are:',promised_cores
			elif R.TR=='space':
					temp=[]
					iden_var=0
					for allocated_hours in range((R.A+k)/3600,((R.A+k+R.T)/3600)):
						allocated_hours_space.append(allocated_hours)
						space[allocated_hours]=space[allocated_hours]+R.W
						if space[allocated_hours]>R.capacity():
							space[allocated_hours]=space[allocated_hours]-R.W
							iden_var=-56
					if iden_var==-56:
						return 'reject'
					print allocation_records_space
					print space
					print 'accepted at a payment of:',payment
					print 'allocated_time will be from',(R.A+k)/3600,'to',(R.A+k+R.T)/3600
					temp.append((R.A+k)/3600)
					temp.append((R.A+k+R.T)/3600)
					allocation_records_space.append(temp)
					promised_space=promised_space+R.W
					#print 'promised_space are:',promised_space

print '\t\t\tWELCOME!'
inpt=int(input("Enter number of resources required:"))
print 'Instruction: Time format is: 24-hour'
for i in range(inpt):
	print 'Enter type of resourse:'
	ty_reso=raw_input()
	print 'Number of',ty_reso,'needed:'
	no_res=int(input())
	arrival_time=int(input("Enter arrival time in hrs:"))
	departure_time=int(input("Enter departure_time in hrs:"))
	req_time=int(input("How much time is required in hrs:"))
	arrival_time=3600*arrival_time
	departure_time=departure_time*3600
	req_time=req_time*3600
	valuation=int(input("Your valuation is: "))
	r=basic_econ_scheduling(no_res,req_time,arrival_time,departure_time,valuation,ty_reso)
	s=r.make_reservaton()
	if s=='reject':
		print 'sorry,rejected since all resources are busy,try at different time!'
	print 'executing...'
	#r.execute()
	#print 'count is: ',count

'''r=basic_econ_scheduling(2,20,10,40,10000,'cores')
r.make_reservaton()'''