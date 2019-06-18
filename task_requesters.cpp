#include<bits/stdc++.h>
using namespace std;
int find_max(int a[])
{
	int i,ma=a[0];
	for(i=0;i<3;i++)
	{
		if(a[i]>ma)
			ma=a[i];
	}
	return ma;
}
int search_index_of(int a[],int key)
{
	cout<<"I have got to search "<<key<<endl;
	int i,j=0;
	for(i=0;i<3;i++)
	{
		if(a[i]==key)
			return i;
	}
	return -1;
}
int quality_voter(int b[],int n)
{
	int i,s,index;
	int a[3]={0};//to count votes
	for(i=0;i<n-3;i++)
	{
		int k=rand()%3;
		a[k]++;
	}
	int m=find_max(a);
	index=search_index_of(a,m);
	return index;
}
bool IsPresent(int a[],int key)
{
	int i;
	for(i=0;i<3;i++)
	{
		if(a[i]==key)
			return true;
	}
	return false;
}
int main()
{
	//cout<<"Enter no of tasks:"<<endl;
	int n,i,j,N;
	int flag=1;
	int quality_voters[20];//i need 20 quality voters
	/*cout<<"Enter number of tasks to be assigned: "<<endl;
	cin>>N;//total number of tasks to be assigned
	int a[N];
	cout<<"Enter budgets of each task:"<<endl;
	for(i=0;i<N;i++)
	{
		cout<<"Enter budget of task:"<<i<<endl<<endl;
		cin>>a[i];
	}
	*/
	cout<<"Enter no. of task completers :"<<endl;
	cin>>n;
	int c[3];
	int index=0;
	while(flag<21)
	{	
        for(i=0;i<3;i++)
        {
    	    int new_bidder=rand()%n;
    	    if(IsPresent(c,new_bidder))
    	        i--;
            else
            	c[i]=new_bidder;
        }
        int index_of_winner=quality_voter(c,n);
        if(IsPresent(quality_voters,c[index_of_winner]))
           flag--;
        else
        {
        	quality_voters[index]=c[index_of_winner];
        	index++;
        }
        flag++;
    }
    cout<<"list of quality voters is :"<<endl;
    for(i=0;i<20;i++)
    {
    	cout<<quality_voters[i]<<" ";
    }
	return 0;
}
