#include<bits/stdc++.h>
using namespace std;
typedef struct bst_node{
	int data;
	struct bst_node* left;
	struct bst_node* right;
}bst_node;
bst_node* GetNewNode(int data)
{
	//bst_node* newNode=(bst_node*)malloc(sizeof(bst_node));
     bst_node* newNode=new bst_node();
     newNode->data=data;
	newNode->left=NULL;
	newNode->right=NULL;
	return newNode;
}
bst_node* insert(bst_node* root,int data)
{
	if(root==NULL)
	{
		root=GetNewNode(data);
		return root;
	}
	else if(data>=root->data)
		root->right=insert(root->right,data);
	else if(data<root->data)
		root->left=insert(root->left,data);
	return root;
}   
void inorder(bst_node* root)
{
	if(root==NULL)
	    return;
	inorder(root->left);
	cout<<root->data<<" ";
	inorder(root->right);
}
void preorder(bst_node* root)
{
	if(root==NULL)
		return;
	cout<<root->data<<" ";
	preorder(root->left);
	preorder(root->right);
} 
void postorder(bst_node* root)
{
	if(root==NULL)
		return;
	postorder(root->left);
	postorder(root->right);
	cout<<root->data<<" ";
}
int main()
{
   int n,data;
   bst_node* root=NULL;
   cout<<"enter no. of nodes of the tree: "<<endl;
   //cin>>n;
   for(int i=5;i<10;i++)
   {
      //cin>>data;
      root=insert(root,i);
   }
   for(int i=1;i<15;i++)
   {
   	root=insert(root,i);
   }
   cout<<"inorder traversal is: "<<endl;
   inorder(root);
   cout<<endl;
   cout<<"preorder traversal is: "<<endl;
   preorder(root);
   cout<<endl;
   cout<<"postorder traversal is: "<<endl;
   postorder(root);
   return 0;
}