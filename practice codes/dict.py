import random
from random import shuffle
no_of_males=input("Enter number of males:")
no_of_females=input("Enter number of females:")
males=[]
females=[]
dict_males={}
dict_females={}
pre=[]
for i in range(no_of_males):
	pre.append(i+1)
l=['name','gender','preferances']
for i in range(no_of_males):
	dict_males={}
	for li in l:
		if li=='name':
			dict_males['name']=raw_input('Enter name:')
		elif li=='gender':
			dict_males['gender']=raw_input('enter gender')
		elif li=='preferances':
			random.shuffle(pre)
			temp_l=pre
			dict_males['preferances']=temp_l
	males.append(dict_males)
print males

