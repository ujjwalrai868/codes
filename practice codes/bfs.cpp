#include<bits/stdc++.h>
using namespace std;
vector<vector<int>> G={{2,6},{},{1,4},{1,2},{4,2,6},{7,2},{5,4,8},{4,9,1,6},{3,4}};
void bfs_traversal(int x,int visited[])
{
	int i,u,j;
	queue<int> q;
	q.push(x);
	while(!q.empty())
	{
        u=q.front();
        q.pop();
        if(visited[u-1]==0)
            cout<<u<<" ";
        visited[u-1]=1;
        for(j=0;j<G[u-1].size();j++)
           if(!visited[G[u-1][j]-1])
              q.push(G[u-1][j]);
	}
	cout<<endl;
}
int main()
{
	int i;
	for(i=1;i<9;i++)
	{
	   int visited[9]={0};
	   bfs_traversal(i,visited);
	}
	return 0;
}