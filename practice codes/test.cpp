#include<bits/stdc++.h>
using namespace std;
vector<vector<int>> G={{4},{1},{6},{3},{4,8},{5},{10,6},{7},{2,8},{9}};
int t=0;
vector<int> dfs;
void dfs_traversal(int x,int visited[],int start_time[]);
void dfs_traversal(int x,int visited[],int start_time[])
{
   int i;
   if(!visited[x-1])
   {
   	  dfs.push_back(x);
      t=t+1;
      start_time[x-1]=t;
   }
   visited[x-1]=1;
   for(i=0;i<G[x-1].size();i++)
   	if(!visited[G[x-1][i]-1])
   	  dfs_traversal(G[x-1][i],visited,start_time);
}
int main()
{
	int i,j,k,l;
    for(i=1;i<=G.size();i++)
     {
      cout<<endl<<endl<<"traversing "<<i<<"... "<<endl;;
      dfs.clear();
      int start_time[G.size()]={0};
      int visited[G.size()]={0};
      t=0;
      dfs_traversal(i,visited,start_time);
      cout<<endl;
      for(j=0;j<dfs.size();j++)
         cout<<"start time of vertex "<<dfs[j]<<" is: "<<start_time[j]<<endl;
      cout<<endl;
      cout<<"dfs size is: "<<dfs.size()<<endl<<endl;;
      cout<<"dfs_traversal of "<<i<<" is:"<<endl;
      for(k=0;k<dfs.size();k++)
         cout<<dfs[k]<<" ";
     cout<<"visited is: "<<endl;
     for(l=0;l<G.size();l++)
     	cout<<visited[l]<<" ";
     }
   return 0;
}