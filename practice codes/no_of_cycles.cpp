#include<bits/stdc++.h>
using namespace std;
//vector<vector<int>> G={{4},{1},{6},{3},{4},{5},{10,6},{7},{2,8},{9}};
//vector<vector<int>> G={{2,6},{},{1,4},{1,2},{4,2,6},{7,2},{5,4,8},{4,9,1,6},{3,4}};
vector<vector<int>> G={{2},{3,4},{1,7},{5,6},{2},{5,8},{5},{7}};
int cycle_count=0;
vector<int> dfs;
vector<vector<int>> dfs_all;
//dfs_all is vector of all dfs
void dfs_traversal(int x,int visited[],int start_time[]);
bool is_in_forward(int n,int m ) //return true if n is in forward of m
{
   //cout<<"in is_in_forward method"<<endl;
   //cout<<"m is: "<<m<<endl;
   int start_time[G.size()]={0};
   int visited[G.size()]={0};
   dfs.clear();
   cout<<endl<<endl<<"traversing "<<m<<"... "<<endl;;
   dfs_traversal(m,visited,start_time);
   vector<int>::iterator itr;
   //cout<<"dfs inside is_in_forward method is: "<<endl;
   for(itr=dfs.begin();itr!=dfs.end();itr++)
      cout<<*itr<<" ";
   cout<<endl;
   itr=find(dfs.begin(),dfs.end(),n);
   if(itr!=dfs.end())
     // cout<<"returning true"<<endl;;
      return true;
   else
     // cout<<"returning false"<<endl;
      return false;
}
void detect_cycle(int start_time[])
{
   vector<int>::iterator itr,itr1,itr2;
   int k=0;
   int m,last_index;
   cout<<"entered detect_cycle "<<endl;
   int i,j,l;
   vector<int> u,v;
   for(i=1;i<=G.size();i++)
      for(j=0;j<G[i-1].size();j++)
        //cout<<"start_time of "<<i<<" is "<<start_time[i-1]<<" "<<"start_time of "<<G[i-1][j]<<" is: "<<start_time[G[i-1][j]-1]<<endl; 
        if(start_time[i-1]>start_time[G[i-1][j]-1])
        {
         u.push_back(i);
         v.push_back(G[i-1][j]);
        }
 // cout<<"printing u and v: "<<endl;
  for(k=0;k<u.size();k++)
   cout<<"u is: "<<u[k]<<"v is: "<<v[k]<<endl;
  for(k=0;k<u.size();k++)
  {
     if(is_in_forward(u[k],v[k]))
     {
      //cout<<"a cycle exist between "<<u[k]<<" and "<<v[k]<<endl;
      cout<<"("<<u[k]<<","<<v[k]<<")"<<" is a back edge."<<endl;
      cycle_count++;
      cout<<"cycle count is: "<<cycle_count<<endl;
     }
   }
 }
int t=0;
void dfs_traversal(int x,int visited[],int start_time[])
{
   int i;
   dfs.push_back(x);
   if(!visited[x-1])
   {
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
  	int i,j,k;
    int start_time[G.size()]={0};
    int visited[G.size()]={0};
     for(i=1;i<=G.size();i++)
     {
      dfs.clear();
      for(j=0;j<G.size();j++)
        start_time[j]=0;
      for(j=0;j<G.size();j++)
        visited[j]=0;
      t=0;
      dfs_traversal(i,visited,start_time);
      cout<<endl;
      for(j=0;j<dfs.size();j++)
         cout<<"start time of vertex "<<dfs[j]<<" is: "<<start_time[dfs[j]-1]<<endl;
      cout<<endl;
      cout<<"dfs size is: "<<dfs.size()<<endl;
      cout<<"dfs_traversal of "<<i<<" is:"<<endl;
      for(k=0;k<dfs.size();k++)
        cout<<dfs[k]<<" ";
       cout<<endl;
      if(dfs.size()==G.size())
      {
         detect_cycle(start_time);
         break;
      }
      else
         continue;
	  }
    cout<<"number of cycles are: "<<cycle_count<<endl;
   return 0;
}