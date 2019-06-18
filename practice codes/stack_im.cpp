#include<iostream>
using namespace std;
int push(int arr[],int data,int top)
{
	int n=10; 
	cout<<"n is: "<<n<<endl;
    if(top==n-1)
    {
    	cout<<"stack overflow :("<<endl;
    	return top;
    }
    else
    {
    	cout<<"top is: "<<top<<endl;
    	arr[top]=data;
    	top++;
        return top;
    }
}
int pop(int arr[],int top)
{
	if(top==0)
	{
		cout<<"memory underflow:("<<endl;
		return top;
	}
	else 
		return top-1;
}
int main()
{
	int s,data,top,k,i;  //size of the stack
	cout<<"enter size of the stack: ";
	cin>>s;
	cout<<endl;
	int stack[s];
	top=0;
	cout<<"Instructions: "<<endl;
	cout<<"1.Enter 1 for push and any 0 for pop and -1 to stop the program: ";
	while(true)
	{
	   cout<<"Enter operation: ";
       cin>>k;
       cout<<endl;
       if(k==1)
       {
          cout<<"Enter data to be pushed: ";
          cin>>data;
          top=push(stack,data,top);
          cout<<endl;
       }
       else if(k==0)
          top=pop(stack,top);       
       else if(k==-1)
       {
          cout<<"program stopped by the user! "<<endl;
          return 0;
       }
       else 
       	cout<<"unrecognised operation :("<<endl;
       cout<<"new stack after operation is: "<<endl;
       for(i=0;i<top;i++)
       	cout<<stack[i]<<" ";
       cout<<endl;
	}
}