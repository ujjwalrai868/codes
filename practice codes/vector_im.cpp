//vector implementation
#include<bits/stdc++.h>
using namespace std;
int main()
{
   int n,i,k,j,m,s;
   i=j=m=0;
   n=int(pow(2,j));
   while(true)
   {  
      //increase m upto n 
   	  s=m;
   	  for(i=0;i<n;i++)
   	  	m++;
      if(m>n)
      {
         j++;
         n=int(pow(2,j));
      }
      int b[n];
      for(i=0;i<m-s;i++)
      {
      	cout<<"enter a value: "<<endl;
      	cin>>k;
      	b[i]=k;
      }
      int *arr=(int*)malloc(sizeof(int)*(n));
      for(i=0;i<m-s;i++)
      	arr[i]=b[i];
      cout<<"elements in the vector are: "<<endl;
      cout<<"m is: "<<m<<endl;
      for(int l=0;l<m;l++)
      	cout<<arr[l]<<" ";
      cout<<"n is: "<<n<<endl;
      cout<<endl;
   }
  return 0;
}