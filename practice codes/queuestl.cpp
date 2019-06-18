#include<bits/stdc++.h>
using namespace std;
int main()
{
    int i,k;
    queue<int> q;
    for(i=0;i<5;i++)
    {
        cout<<"Enter a number to enqueue"<<endl;
        cin>>k;
        q.push(k);
    }
    for(i=0;i<2;i++)
        q.pop();
    cout<<q.back()<<" ";
    cout<<q.front()<<" ";
    cout<<q.size()<<endl;
    return 0;
}
