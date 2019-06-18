#include<bits/stdc++.h>
using namespace std;
int main()
{
	vector<int> v1;
	int i,n;
	for(i=0;i<5;i++)
	{
		cin>>n;
		v1.push_back(n);
	}
	vector<int>::iterator ptr;
	for(ptr=v1.begin();ptr<v1.end();ptr++)
     cout<<*ptr<<" ";
	return 0;
}