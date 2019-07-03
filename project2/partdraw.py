import random
import numpy as np 
student=[]
room=[]
global count
count =0

no_of_users=input("Enter number of users:")
inpt=int(input('Enter number of service_providers:'))
for i in range(no_of_users):
    student.append(i+1)
for i in range(inpt):
    room.append(i+1)
n=inpt
final = []
combinePref = []

for each in range(len(student)):# RANDOM PREFERENCE FILLING
    pref = []
    s=int(random.random()*200)
    s=s%n
    while len(pref)<s:
        temp = np.random.randint(low=1,high=n)
        if temp not in pref:
            pref.append(temp)
    for i in range(s+1,n):
	pref.append(0)
    print pref	
    combinePref.append(pref)
rand = []#RANDOM GENERATION
for pre in combinePref:
	while len(rand)<len(pre):
    		temp = np.random.randint(low=1,high=n+1)
    		if temp not in rand:
        		rand.append(temp)


for each in range(len(rand)):#SORTING
    for each1 in range(each,len(rand)):
        if rand[each]>rand[each1]:
            temp = rand[each1]
            rand[each1] = rand[each]
            rand[each] = temp    
            temp = combinePref[each1]
            combinePref[each1] = combinePref[each]
            combinePref[each] = temp
            temp = student[each1]
            student[each1] = student[each]
            student[each] = temp
	#print(rand)
     
for each in range(len(rand)):#ALLOTMENT
    for each1 in range(len(rand)):
        if( room[combinePref[each][each1]-1] !=0 ):
            final.append("student "+str(student[each])+ " got "+ str( room[combinePref[each][each1]-1]))
            room[combinePref[each][each1]-1] = 0
            break

for each in range(len(final)):
    count+=1
    print(final[each])
    print count
print 'count is:',count
            
            
            
