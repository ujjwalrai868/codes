#include<bits/stdc++.h>
using namespace std;
string encrypt(string s,string a,int l,int r)
{
    int mid;
    a="";
    if(l<r)
    {
        mid=(l+r)/2;
        a=a+s.at(mid);
        encrypt(s,a,l,mid-1);
        encrypt(s,a,mid+1,r);
    }
    return s;
}
int main()
{
    int t;
    cin>>t;
    while(t>0)
    {
        int n;
        cin>>n;
        string s,a;
        a="";
        cin>>s;
        cout<<encrypt(s,a,0,n-1)<<endl;
    }
}