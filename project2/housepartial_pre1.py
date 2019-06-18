import random
import copy
import numpy as np
import Gnuplot
xyz=0
f1=open("abc.txt","a")
f2=open("abc1.txt","a")
f3=open("di3.txt","a")
f4=open("di4.txt","a")
g=Gnuplot.Gnuplot(persist=1)
c=0
l = [[0]]
op=[]
pq=[]
agent=[]
house=[]
h1=[0]
num=int(input("enter num: "))
for i in range(1,num+1):
    agent.append(i)
for i in range(num+1,num*2+1):
   house.append(i)
for i in range(len(house)):
  h1.append(house[i])
print '\n'
print 'h1 is: ',h1
pre=[[0]]
for j in range (0, len(house)):
    s=int((random.random()*100)%(num))
    if s==0:
      s+=2
    a=[]
    b=[]
    a=[ x for x in range(num+1,num*2+1) ]
    random.shuffle(a)
    for k in range(s):
      b.append(a[k])
    for k in range(s+1,num+1):
      b.append(0)
    b.append(0)
    pre.append(b)
print 'pre is: ',pre
print '\n'
f=[]
pre1=copy.deepcopy(pre)
pre2=copy.deepcopy(pre)
pre3=copy.deepcopy(pre)
print 'length of pre is:',len(pre)
for i in range(num+1,num*2+1):
   l.append([])
   l[i-num].append(i)
print 'initially l is: ',l
adlst=[0]*((num*2)+1)
def list1(graph,i,j):
  for m in range(1,len(pre)):
   for ii in range(len(pre[m])):
     if pre[m][ii]!=-2:
        l[m].append(pre[m][ii])
        break 
  print 'l is: ',l
  for m in range(1,len(pre)):
       graph[m]=[l[m][i]]
       k=l[m][j]
       if graph[k]==j:
          graph[k]=[m]
       else:
          graph[k].append(m)
  graph[0]=[0]
  print 'graph is: ',graph
  return  graph
print list1(adlst,1,0)
visit=[0]*len(adlst)
print 'visit is: ',visit
p=[]
res=[]
cy=[]
ll=[]
l3=[]
lst=[]
l5=[]
graph1=[]
y1=[0]*len(agent)
some_value=0
def dfsvisit(graph,u):
       global op
       global some_value
       global pq
       c=0
       visit[u]=1
       p.append(u)
       print 'p is: ',p
       for i in range(len(graph[u])):
            k=graph[u][i]
            if visit[k]==0:
               dfsvisit(graph,k)
               res.append(k)
            for t in range(len(p)):
              if p[t]==0:
                for m in range(len(p)):
                  cy.append(p[m])
            if visit[k]==1:
               ind=p.index(k)
               for i1 in range(ind,len(p)):
                      cy.append(p[i1])
               print 'cy is: ',cy
               if cy[0]==cy[1]:
                   cy.pop(0)
               for i in range(len(agent)):
                 if agent[i]==cy[0]:
                     c=1
            else:
               c=0 
            if len(cy)>=2:
               print cy 
            if c==0 and len(cy)%2==0:
                 if len(cy)!=0:
                   y=cy.pop(0)
                   cy.append(y)
            elif c==0 and len(cy)%2!=0:
                    cy.pop(0)
                    cy.reverse() 
            if len(cy)!=0:
                print 'cycle is ',cy
            for i2 in range(len(cy)/2):
              l1=cy.pop(0)
              print l1, 
              pre[l1][num]=-1
              l5.append(l1)
              ll.append(l1) 
              print '---',
              l2=cy.pop(0)
              print l2
              index1=pre3[l1].index(l2)
              y1[l1-1]=index1
              l3.append(l2)
              ll.append(l2)
            if p!=[]  and some_value==0:
              op=copy.deepcopy(p)
              print 'op is: ',op
              some_value=some_value+1
            elif p!=[] and some_value==1:
              pq=copy.deepcopy(p)
              print 'pq is: ',pq
            else:
              some_value=0
            if pq==op and op!=[] and pq!=[]:
              print 'inside if :'
              return l
            del p[:]
            del cy[:]
            
       visit[u]=2


def dfs(graph,i):
    if visit[i]==0:
        main_print=dfsvisit(graph,i)
    print 'main_print is: ',main_print
    res.append(i)

def end(graph,i):
  dfs(graph,i)
  for j in range(1,len(graph)):
    if j not in res:
         return dfs(graph,j)

inpt=input('enter the agent ')
def main(graph,s):
   end(graph,s)
   for i in range(1,len(pre)):
     if pre[i][num]==0:
       for ij in range(len(l3)):
         l4=l3[ij]
         if l4 in ll and l4 in pre[i]:
             inn=pre[i].index(l4)
             if pre[i][inn]!=-2:
                pre[i][inn]=-2
             else:
                 i=i+1
   del l3[:]
   for i in range(1,len(l)):
      l[i].pop(1)
   for j in range(len(graph)):
      graph[j]=0
      visit[j]=0
   list1(graph,1,0)
   for i in range(len(ll)):
     if (i%2)==0:
         p=ll[i]
         a1=l[p][0]
         a2=l[p][1]
         graph[a1].remove(p)
         graph[p].remove(a2)
   for i in range(1,len(agent)+1):
       if i not in ll:
            lst.append(i)
   if len(lst)!=0:
       st=lst.pop(0)
   m=0
   if len(l5)==len(agent):
         m=1
   if m==0:
           del lst[:]
           return main(graph,st)
   else:
          return 'allocation completed '
main_print=main(adlst,inpt)
print main_print
print 'op is: ',op
print 'pq is: ',pq
#----------------------------------------------
print '\n'
print 'Random Allocation'
del l[:]
l=[0]
y2=[0]*len(agent)
def prefer():
  for i in range(1,len(pre1)):
    for j in range(len(pre1[i])-1):
     f.append(pre1[i][j])
     e=random.choice(f)
    l.append(e)
    for ij in range(1,len(pre1)):
        pre1[ij].remove(e)
    del f[:]
  return l  
prefer()
for i in range(1,len(agent)+1):
    print i,
    print '----',
    lk=l.pop(1)
    print lk
    index2=pre2[i].index(lk)
    y2[i-1]=index2

di1=sum(y1)
print 'di1 is: ',di1
f3.write(str(di1))
f3.write('\n')
di2=sum(y2)
print 'di2 is: ',di2
f4.write(str(di2))
f4.write('\n')
print 'DSIC : ',y1
c=0
for i in range(len(y1)):
  if y1[i]==0:
    c=c+1
f1.write(str(c))
f1.write('\n')
print y2
print 'RANDOM : ',y2
c1=0
for i in range(len(y2)):
  if y2[i]==0:
    c1=c1+1
f2.write(str(c1))
f2.write('\n')
