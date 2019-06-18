#include<iostream>
using namespace std;
class B;
class A
{
private:
	int a;
public:
	A(int k)
	{
		a=k;
	}
	friend int compare(A x,B y);
};
class B
{
private:
	int b;
public:
	B(int k)
    {
    	b=k;
    }
    friend int compare(A,B);
};
int compare(A x,B y)
{
	if (x.a>y.b)
	   return x.a;
	else if(x.a<y.b)
		return y.b;
	else
		return 0;
}
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
	int a,b;
	cout<<"Write two numbers to be compared\n";
	cin>>a;
	A first(a);
	cin>>b;
	B second(b);
    int c=compare(first,second);
    if(c==0)
    	cout<<"Both numbers are same"<<endl;
    else
        cout<<c<<" is greater\n";
    }
	return 0;
}