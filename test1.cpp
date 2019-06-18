#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,i,k,cld,acld;
    char curr_char;
    cin>>t;
    map<int,int> m;
    m.insert(pair<char,int>('a',0));
    m.insert(pair<char,int>('b',1));
    m.insert(pair<char,int>('c',2));
    m.insert(pair<char,int>('d',3));
    m.insert(pair<char,int>('e',4));
    m.insert(pair<char,int>('f',5));
    m.insert(pair<char,int>('g',6));
    m.insert(pair<char,int>('h',7));
    m.insert(pair<char,int>('i',8));
    m.insert(pair<char,int>('j',9));
    m.insert(pair<char,int>('k',10));
    m.insert(pair<char,int>('l',11));
    m.insert(pair<char,int>('m',12));
    m.insert(pair<char,int>('n',13));
    m.insert(pair<char,int>('o',14));
    m.insert(pair<char,int>('p',15));
    m.insert(pair<char,int>('q',16));
    m.insert(pair<char,int>('r',17));
    m.insert(pair<char,int>('s',18));
    m.insert(pair<char,int>('t',19));
    m.insert(pair<char,int>('u',20));
    m.insert(pair<char,int>('v',21));
    m.insert(pair<char,int>('w',22));
    m.insert(pair<char,int>('x',23));
    m.insert(pair<char,int>('y',24));
    m.insert(pair<char,int>('z',25));
    while(t>0)
    {
       string s;
       cin>>s;
       int l;
       l=s.length();
       k=0;
       for(i=0;i<l;i++)
       {
          curr_char=s.at(i);
          if(m[curr_char]>=k)
            cld=m[curr_char]-k;
          else
            cld=26-k+m[curr_char];
          if(m[curr_char]>=k)
             acld=26-m[curr_char]+k;
          else
             acld=k-m[curr_char];
          k=min(cld,acld);
          if(k==acld&&k!=cld)
          {
            k=-k;
            cout<<k<<" ";
          }
          else if(k==cld)
            cout<<abs(k)<<" ";
          k=m[curr_char];
       }
       cout<<endl;
       t--;
    }
}


