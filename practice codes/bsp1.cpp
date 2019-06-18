#include<bits/stdc++.h>
using namespace std;
int binary_saerch(int a[],int low,int high,int key)
{
   int n=high-low+1; //n is size of a[]
   int mid=low+n/2;
   while(low<high)
   {
     if(a[mid]==key)
   	  return mid;
     else if(key<a[mid])
   	  return binary_saerch(a,low,mid-1,key);
     else if(key>a[mid])
   	  return binary_saerch(a,mid+1,n-1,key);
   }
}
int main()
{
	int n,i,q,key;
	cin>>n;
	int a[n];
	for(i=0;i<n;i++)
		cin>>a[i];
    sort(a,a+n);
    cin>>q;
    while(q>0)
    {
	   cin>>key;
	   int test=binary_saerch(a,0,n-1,key);
	   cout<<test+1<<endl; 
	   q--;
    }
	return 0;
}