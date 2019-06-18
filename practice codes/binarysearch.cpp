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
   return -1;
}
int main()
{
	int n,i,key;
	cout<<"enter size of array"<<endl;
	cin>>n;
	int a[n];
	for(i=0;i<n;i++)
		cin>>a[i];
	sort(a,a+n);
	cout<<"enter a value to be searched: ";
	cin>>key;
	int test=binary_saerch(a,0,n-1,key);
	if(test!=-1)
		cout<<"FOUND! at position "<<test+1<<endl;
	else
		cout<<"NOT FOUND!"<<endl;
	return 0;
}