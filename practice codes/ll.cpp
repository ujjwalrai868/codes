#include<bits/stdc++.h>
using namespace std;
typedef struct linked_list{
	int data;
	struct linked_list *next;
}node;
int main(){
	int d;
    cout<<"address of d is: "<<&d;
    cin>>d;
	node* start;
	cout<<"address of start is: "<<&start;
	return 0;
}