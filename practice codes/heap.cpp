#include<bits/stdc++.h>
using namespace std;
typedef struct Heap{
	int *array;
	int count;  //no of elements in the heap
	int capacity;
	int heap_type;
}heap;
heap *create_heap(int capacity,int heap_type)
{
	//heap *h=(heap*)malloc(sizeof(heap));
	heap *h=new heap();
	if(h==NULL)
		cout<<"memory underflow"<<endl;
    h->capacity=capacity;
    h->count=11;
    h->array=(int*)malloc(sizeof(int)*h->capacity);
    if(h->array==NULL)
    	cout<<"memory underflow"<<endl;
	return h;
}
int left_child(heap *h,int i)
{
	int left=2*i+1; 
    if(left>h->count)
    	return -1;
    else
    	return left;  //index of the left child
}
int right_child(heap* h,int i)
{
	int right=2*i+2;
	if(right>h->count)
		return -1;
	else
		return right;
}
int get_maximum(heap *h)
{
	if(h->count==0)
		return -1;
	return h->array[0];
}
void percolate_down(heap *h,int i)
{
	int left,right,temp,max;
	left=left_child(h,i);
	right=right_child(h,i);
	if(left!=-1||right!=-1)
	{

	   if(h->array[left]>h->array[i])
		   max=left;
	   else if(h->array[left]>h->array[i])
		   max=i;
	   if(h->array[right]>h->array[max])
		   max=right;
	   //to swap max and i
	   if(max!=i)
	   {
		   temp=h->array[i];
		   h->array[i]=h->array[max];
		   h->array[max]=temp;
	   }
	   percolate_down(h,max);
	}
}
bool check_if_heap(heap *h,int k)
{
	int l,r,n;
	n=h->count;
	for(int i=k;i<n;i++)
	{
      l=left_child(h,i);
      r=right_child(h,i);
      if(l!=-1&&r!=-1)
        if((h->array[l]>h->array[i])&&(h->array[r]>h->array[i]))
      	  return false;
	}
	return true;
}
int main()
{
	int n;
	cout<<"enter size of the heap: ";
	cin>>n;
	cout<<endl;
	heap*h=create_heap(n,1);  // 1 means max heap
	cout<<"enter elements in the heap: ";
	for(int i=0;i<n;i++)
      cin>>h->array[i];
    cout<<endl;
   // cout<<left_child(h,2)<<endl;
    cout<<"check if heap is: ";
    cout<<check_if_heap(h,0)<<endl;
    if(check_if_heap(h,0))
     cout<<"given array is already a heap"<<endl;
    else
    {
    	cout<<"heapifying..."<<endl<<endl;
    	//percolate_down(h,5);
    	percolate_down(h,3);
    	/*for(int i=(n/2)-1;i>=0;i--)
    	{
    		cout<<"i is: "<<i<<endl;
    		percolate_down(h,5);
    	/*	cout<<"check_if_heap(h,"<<i<<") is: "<<check_if_heap(h,i)<<endl;
    		if(!check_if_heap(h,i))
    		{

    		   percolate_down(h,i);
    		   cout<<"obtained arr is: "<<endl;
    		   for(int i=0;i<n;i++)
                 cout<<h->array[i]<<" ";
               cout<<endl;
    		}
    	}*/
    }
    cout<<"heap is: "<<endl;
    for(int i=0;i<n;i++)
       cout<<h->array[i]<<" ";
	return 0;
}