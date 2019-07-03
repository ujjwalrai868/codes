#l=[12,13,14,15,16,17,19,20,21,22,24,25,26,27,29,30,31,33,35,36,37,38,39,41,44,49,50,46,47,48,67,68,89]
l=[15,19]
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
print n