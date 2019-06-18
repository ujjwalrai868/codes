#include <bits/stdc++.h>
using namespace std;
void find_median(vector<int> v)
{
    sort(v.begin(),v.end());
    int n=v.size();
    if(n%2==0)
      cout<<(v[n/2]+v[(n/2)-1])/2<<endl;
    else
      cout<<v[n/2]<<endl;
}
int main() {
	vector<int> v;
	int t,i,k;
	cin>>t;
	for(i=0;i<t;i++)
	{
	    cin>>k;
	    v.push_back(k);
	    find_median(v);
	}
	return 0;
}