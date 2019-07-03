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
slot_left=[]
slots=[]
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
price_demand={}
no_allocations=0
prices=[10,20,30,40,50,60,70,80,90,100]
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
		if self.TR=='cpu':
			return 500
	def any_slot_left(self,totalCost):
		st=self.A
		ed=self.D
		slot_left=[]
		for time in range(st,ed):
			if self.TR=='cpu':
				if cpu[time]+self.W<self.capacity():
					slot_left.append(time)
		return slot_left
	def divide_slots(self,l):
		#print 'inside divide_slots'
		temp=[]
		n=[]
		for i in range(len(l)-1):
			if l[i+1]-l[i]==1:
				temp.append(l[i])
				if i==len(l)-2:
					temp.append(l[i+1])
					n.append(temp)
			else:
				temp.append(l[i])
				n.append(temp)
				temp=[]
		if not (l[len(l)-1] in n[len(n)-1]):
			temp=[]
			temp.append(l[len(l)-1])
			n.append(temp)
		return n
	def can_be_completed(self):
		ran=int(random.random()*100)%100
		if ran>50:
			return True
		else:
			print 'cannot be completed by the user!'
			print 'user needs one more hour'
			return False
	def demand(R):
		return int(random.random()*500)%500
	def decide(R,totalCost,V):
		global payment
		print 'our price is:',min(totalCost)
		payment=min(totalCost)
		#print 'valuation is: ',V
		if min(totalCost)<=V:
			#print 'accepted!'
			for i in range(len(totalCost)):
				if totalCost[i]==min(totalCost):
					return i
		else:
			print 'sorry,rejected!'
			return -1
	def generate_bid(self,lp_service_prviders,avg_bid):
		print 'bidding started'
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
		print 'further payment will be:',bids[m]
		return t
	def execute(self,avg_bid):
		if self.can_be_completed()==False:
				k=self.allocate_low_p(avg_bid)
				print k,'is allocated for further task'

	def make_reservaton(R):
		print 'reserving'
		global total_cost,promised,promised_cpu,count,mini
		global promised_cpu,promised_cores,promised_space
		global iden_var,payment,cnt,cont
		global slots
		cnt=0
		cont=0
		totalCost=[]
		mini=0
		count=0
		total_cost=0
		promised=0
		cost=[]
		print 'calculating price...'
		for t in range(R.D-R.A+1):
			temp_price=[]
			d=R.demand()  #demand estimate function
			#print 't is: ',t
			#print 'd is: ',d
			if R.TR=='CPU' or 'cpu':
				promised=cpu[R.A+(t)]
			price=0
			for i in range(R.W):
				c=R.capacity()
				for each_price in prices:
					price_demand[each_price]=R.demand()
				temp_list=[]
				for each_price in prices:
					if R.TR=='CPU' or 'cpu':
						if price_demand[each_price]+cpu[t]+i+1>c:
							temp_list.append(each_price)
				if len(temp_list)==0:
					p=10
				else:			
					p=max(temp_list)
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
		slots=R.any_slot_left(totalCost)
		k=R.decide(totalCost,R.V)
		#print 'k is: ',k
		if k!=-1:
			if R.TR=='CPU' or 'cpu':
					global no_allocations
					iden_var=0
					temp=[]
					for allocated_hours in range((R.A+k),((R.A+k+R.T))):
						allocated_hours_cpu.append(allocated_hours)
						cpu[allocated_hours]=cpu[allocated_hours]+R.W
						if cpu[allocated_hours]>R.capacity():
							for allocated_hours in range((R.A+k),((R.A+k+R.T))):
								cpu[allocated_hours]=cpu[allocated_hours]-R.W
							iden_var=-56
					if iden_var==-56:
						return 'reject'
					print allocated_hours_cpu
					#print 'R.capacity is: ',R.capacity()
					if cpu[allocated_hours]>R.capacity():
						for allocated_hours in range((R.A+k),((R.A+k+R.T))):
							allocated_hours_cpu.append(allocated_hours)
							cpu[allocated_hours]=cpu[allocated_hours]-R.W
						return 'reject'
					#print cpu factor
					print 'accepted at a payment of:',payment
					no_allocations+=1
					avg_bid=payment/(R.T)
					print 'allocated time will be from',(R.A+k),'to',(R.A+k+R.T)
					temp.append((R.A+k))
					temp.append((R.A+k+R.T))
					alloction_records_cpu.append(temp)
					#print 'alloction_records_cpu is:',alloction_records_cpu
					promised_cpu=promised_cpu+R.W
					#print 'promised_cpu are:',promised_cpu
					print 'executing...'
					R.execute(avg_bid)

#print '\t\t\tWELCOME!'
#inpt=int(input("Enter number of users:"))
inpt=500
print 'Instruction: Time format is: 24-hour'
for i in range(inpt):
	iden_va=0
	global div_slots,z,y
	z=0
	y=0
	div_slots=[]
	#print 'Enter type of resourse:'
	#ty_reso=raw_input()
	ty_reso='cpu'
	#print 'Number of',ty_reso,'needed:'
	#no_res=int(input())
	no_res=10
	print 'no_res is:',no_res
	#arrival_time=int(input("Enter arrival time in hrs:"))
	#departure_time=int(input("Enter departure_time in hrs:"))
	#req_time=int(input("How much time is required in hrs:"))
	'''arrival_time=3600*arrival_time
	departure_time=departure_time*3600
	req_time=req_time*3600'''
	#valuation=int(input("Your valuation is: "))
	arrival_time=0
	departure_time=23
	req_time=3
	valuation=100000000
	r=basic_econ_scheduling(no_res,req_time,arrival_time,departure_time,valuation,ty_reso)
	if no_res>r.capacity():
		print 'Sorry,demand is greater than our capacity'
		continue
	s=r.make_reservaton()
	#print 'slots are ',slots
	#print 'allocation data of',ty_reso,'is:'
	#if ty_reso=='cpu':
	#	print cpu
	if s=='reject' and len(slots)>1:
		#print 'slots are',slots
		div_slots=r.divide_slots(slots)
		#print 'div_slots are:',div_slots
	elif s=='reject' and len(slots)==1 and len(slots)<req_time:
		print 'sorry,rejected since all resources are busy,try at different time!'
	elif s=='reject' and len(slots)==1 and len(slots)==req_time:
		div_slots.append(slots)
	elif s=='reject' and len(slots)==0:
		print 'sorry,rejected since all resources are busy,try at different time'
	rej=[]
	temp_var=0
	for w in range(len(div_slots)):
		rej.append(len(div_slots[w]))
	for j in range(len(rej)):
		if rej[j]>=req_time:
			temp_var+=1
			z=-67
	if temp_var==0 and z==-67:
		print 'sorry,rejected since all resources are busy,try at different time!'
	for w in range(len(div_slots)):
		if len(div_slots[w])>=req_time:
			arrival_time=div_slots[w][0]
			departure_time=div_slots[w][len(div_slots[w])-1]+1
			temp_obj=basic_econ_scheduling(no_res,req_time,arrival_time,departure_time,valuation,ty_reso)
			t=temp_obj.make_reservaton()
			if t=='reject':
				print 'sorry,rejected since all resources are busy,try at different time!'
print 'no_allocations is:',no_allocations