#include<iostream>
using namespace std;
class complex
{
public:
	int a,b;
	complex()
	{
		a=0;
		b=0;
	}
	complex(int x,int y)
	{
		a=x;
		b=y;
	}
	void showComplex()
	{
		cout<<a<<" + "<<b<<"i"<<endl;
	}
	void operator+(complex c2)
	{
        cout<<"Sum of the two complex numbers is: "<<a+c2.a<<" + "<<b+c2.b<<"i"<<endl;
	}
	void operator*(complex c2)
	{
		int m,n;
		m=(a*c2.a)-(b*c2.b);
		n=(a*c2.b)+(b*c2.a);
	    cout<<"Multiplication of given two complex numbers is: "<<m<<" + "<<n<<"i"<<endl;
	}
   
	
};
int main()
{
	complex c1(9,8),c2(7,3);
	cout<<"First complex number is: "<<endl;
	c1.showComplex();
	cout<<"Second complex number is: "<<endl;
	c2.showComplex();
    c1+c2;
    c1*c2;
    return 0;
}