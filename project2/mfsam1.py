import random
import copy
import numpy as np
import Gnuplot
f1=open("mfsam.txt","r")
f1.read(10)
#assuming 10 users of the given category
users=[]
service_providers=[]
availability=[]
availability_list=[]
time_cons=[]
curr_pre=[]
l1=[]
l2=[]
l3=[]
visit=[]
temp=[]
time_cons_list=[]
no_of_users=int(input('Enter number of users:'))
inpt=int(input('Enter number of service_providers:'))
for i in range(no_of_users):
	users.append(i+1)
print 'users are:',users
for i in range(no_of_users):
	visit.append(0)
#print visit
#creating preferance list for each user
#let their be 10 service providers
k=no_of_users
for i in range(inpt):
	service_providers.append(k+i+1)
print 'service providers are: ',service_providers
#allocating availability of service providers
for i in range(inpt):
	ran=int(random.random()*1000)%100
	if ran<40:
		ran=42
	availability.append(ran)
	temp=[]
	
for i in range(inpt):
	temp.append(i+no_of_users+1)
	temp.append(availability[i])
	availability_list.append(temp)
	temp=[]
print 'availability of service providers are: ',availability_list

for i in range(no_of_users):
	ran=int(random.random()*1000)%40
	if ran==0:
		ran=14
	time_cons.append(ran)
del temp[:]
temp=[]

#time consumption of each user
for i in range(no_of_users):
	temp.append(i+1)
	temp.append(time_cons[i])
	time_cons_list.append(temp)
	temp=[]
print 'time consumption of each user are: ',time_cons_list
#generating preferance list
pre=[]
for j in range (0,no_of_users):
    s=int((random.random()*100)%(len(service_providers)))
    if s==0:
      s+=2
    a=[]
    b=[]
    a=service_providers
    random.shuffle(a)
    for k in range(s):
      b.append(a[k])
    for k in range(s+1,len(service_providers)+1):
      b.append(0)
    pre.append(b)
for i  in range(len(pre)):
	print 'preferance list of ',i+1,'th user is:',
	for j in range(len(pre[i])):
		if pre[i][j]!=0:
			print pre[i][j],
	print '\n'
	#randomising the users list
#make a new list of ith priority of all users
i=0;
random.shuffle(users)
print 'shuffled users are:',users
for prefer in range(len(service_providers)):
	for user in users:
		l1.append(user)
		l1.append(pre[user-1][prefer])
		l2.append(l1)
		l1=[]
	l3.append(l2)
	l2=[]
#print 'l3 is:',l3
for prelist in l3:
	for lis in range(len(prelist)):
		if prelist[lis][1]!=0:
			if time_cons[prelist[lis][0]-1]<availability[prelist[lis][1]-1-no_of_users] and visit[prelist[lis][0]-1]==0:
			    print prelist[lis][0],'is allocated to ',prelist[lis][1],'for',time_cons[prelist[lis][0]-1],'minutes'
			    '''f1.write(str(prelist[lis][0]))
			    f1.write(str(prelist[lis][1]))
			    f1.write('\n')'''
			    #print 'availability of',prelist[lis][1],'is',availability[prelist[lis][1]-1-no_of_users]
			    availability[prelist[lis][1]-1-no_of_users]=availability[prelist[lis][1]-1-no_of_users]-time_cons[prelist[lis][0]-1]
			    #print 'current availability of',prelist[lis][1]-1,'is',availability[prelist[lis][1]-1-no_of_users]
			    visit[prelist[lis][0]-1]=1
            #visit[prelist[lis][0]-1]=1
#print 'visit is:',visit
global count
count=0
#for i in vi
for i in range(len(visit)):
	if visit[i]==1:
		count+=1
print 'total number of allocations are:',count
print '\n'
print 'unallocated agents are: ',
for i in range(len(visit)):
	if visit[i]==0:
		print i+1,