#include<vector>
#include<iostream>
using namespace std;
int main()
{
	vector<vector<int> > v;
	int i,j,value;
	vector<int> temp;
	for(i=0;i<5;i++)
	{
		temp.clear();
       for(j=0;j<5;j++)
       {
          cin>>value;
          temp.push_back(value);
       }
       v.push_back(temp);
	}
	cout<<"Elements in the vector of vectors are: "<<endl;
	for(i=0;i<v.size();i++)
	{
		for(j=0;j<5;j++)
			cout<<v[i][j]<<" ";
		cout<<endl;
	}
}
