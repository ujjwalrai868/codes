//BUDGET FEASIBLE MECHANISM
//given some tasks and many competitors for the task
#include<bits/stdc++.h>
using namespace std;
int search_index_of(int a[],int n,int key)
{
  int i;
  for(i=0;i<n;i++)
  {
    if(a[i]==key)
      return i;
  }
  return -1;
}
int find_max(int a[],int n)
{
  int i,ma=a[0];
  for(i=0;i<n;i++)
  {
    if(a[i]>ma)
      ma=a[i];
  }
  return ma;
}
static int k=1;
map<int,int> bid_mapper(vector<int>v,int qvn,int curr_budget_value)
{
  int i,factor,ran;
  k=k*10;
  map<int,int> m;
  map<int,int>::iterator itr;
  srand(time(0));
  for(i=0;i<qvn;i++)
  {
    int ran=rand()%((curr_budget_value/4)*k+rand())%(curr_budget_value/4);
    if(ran>(int(curr_budget_value/10))&&ran<curr_budget_value/4)
    {
       m.insert(pair<int,int>(ran,v[i]));
    }
    else
       i--;
  }
  return m;
}
int main()
{
   int n,temp_int,ni,N,qvn,i,pb,j,k,key,payment,ran,budget_value,t,sum,first_loser,size,total_time,curr_budget_value,in;
   //ni is the number of installments
   int utility_sum=0;
   int total_payment[100];
   int proposed_budget_value,max_sum;
   int average_payment,utility;
   //cout<<"enter number of installments"<<endl;
   //cin>>ni;
   ni=5;
   vector<int> winning_bids;
   int installments[ni];
   vector<int> quality_voters,c,b,temp,win_set,bbyk;
   map<int,int> win_map;
   map<int,int> bid_map;
   map<int,int>::iterator itr,itr1,itr2;
   vector<int> ::iterator ptr,ptr1;
   cout<<"Enter number of tasks:"<<endl;
   int value=0;
   cin>>N;
   int a[N];
   total_time=0;
   for(i=0;i<N;i++)
   {
      a[i]=5;
      total_time=total_time+a[i];
   }
   cout<<"enter proposed budget: "<<endl;
   cin>>proposed_budget_value;
   //proposed budget value 70% of which will be utilised for the job
   budget_value=(7*proposed_budget_value)/10;
   cout<<"Budgets for the tasks is: "<<endl;
   cout<<budget_value<<endl;
   sum=0;
   for(i=1;i<ni;i++)
   {
      installments[i-1]=rand()%(budget_value/ni-4);
      if(installments[i-1]>=budget_value/(ni+1))
        sum=sum+installments[i-1];
      else
        i--;
   }
   installments[ni-1]=budget_value-sum;
   /*cout<<"Enter total number of competetors for bidding: "<<endl;
   cin>>n;*/
   n=100;
   //cout<<"Enter number of quality voters needed: "<<endl;
   //cin>>qvn;
   qvn=10;
   t=qvn;
   utility_sum=0;
   while(value<100)
   {
     while(qvn>0)
     {
      c.clear();
      b.clear();
      srand(time(0));
      int r=rand()%100;
      if(r>50)
   	   k=100-r;
      else
   	   k=r;
     // cout<<"value of k is:"<<k<<endl;
      for(i=1;i<=k;i++)
   	     c.push_back(i);
      map<int,int> m;
      for(i=1;i<=k;i++)
         m.insert(pair<int,int>(i,k-i+1));
      for(i=0;i<k;i++)
      {
   	   ran=rand()%n;
       if(std::find(b.begin(),b.end(),ran)==b.end())
   	       b.push_back(ran);    //b is the array having k voters
   	   else
   		   i--;
      }
     /* cout<<endl<<"bidders standing in this round are: "<<endl;
      for(ptr=b.begin();ptr!=b.end();ptr++)
      {
   	   cout<<*ptr<<" ";
      }*/
      //cout<<endl;
 	    int sum[k]={0};
      for(i=k+1;i<=n;i++)
      {
         random_shuffle(c.begin(),c.end());
         //cout<<"Priority list of "<<i-k<<"th voter is: ";
         //for(ptr=c.begin();ptr!=c.end();ptr++)
      	  // cout<<*ptr<<" ";
         for(j=0;j<k;j++)
           sum[j]=sum[j]+c[j]*m[c[j]];
        // cout<<endl;
      }
      for(i=0;i<k;i++)
   	   //cout<<sum[i]<<" ";
      //cout<<endl;
      max_sum=find_max(sum,k);
   //search max_sum index in the sum array and then search the number
   //at that index in vector b which contains the actual voters and not
   //the positions only
      int index=search_index_of(sum,k,max_sum);
      int push=b[index];
      if(find(quality_voters.begin(),quality_voters.end(),push)==quality_voters.end())
      {
   	   // cout<<"winner is :"<<push<<endl;
        quality_voters.push_back(push);
      }
      else
      { 
   	  //  cout<<"repeated winner,hence vote again!"<<endl;
        qvn++;
      }
      qvn--;
      }
      cout<<"quality voters are: "<<endl;
      for(ptr=quality_voters.begin();ptr!=quality_voters.end();ptr++)
  	    cout<<*ptr<<" ";
      cout<<endl;
   //send the quality_voters and its size to map
   //between voter and bid value
   //voters will bid for each task seperately
   //and no voter will be allocated two tasks
   //for(itr=bid_map.begin
   //sort all quality voters according to their bid value
   //already sorted in the map
      cout<<"budget is: "<<budget_value<<endl;
      cout<<"installments of the budget are: "<<endl;
      for(i=0;i<ni;i++)
       cout<<installments[i]<<endl;
  //for each task we will have a winning set
      total_payment[value]=0;
     for(j=0;j<N;j++)
     {
       bbyk.clear();
       win_set.clear();
       win_map.clear();
       curr_budget_value=(budget_value*a[j])/(total_time);
       cout<<endl<<endl<<"Budget for the "<<j+1<<"th task is: "<<curr_budget_value<<endl;
    //new biddings for this budget
       bid_map=bid_mapper(quality_voters,t,curr_budget_value);
       cout<<"biddings of each quality voter are: "<<endl;
       for(itr=bid_map.begin();itr!=bid_map.end();itr++)
       {
         cout<<itr->second<<"     "<<itr->first<<endl;
       }
       for(i=1;i<=t;i++)
       {
           bbyk.push_back((curr_budget_value)/i);
       }
       for(ptr=bbyk.begin();ptr!=bbyk.end();ptr++)
         cout<<*ptr<<" ";
       in=0;
       for(itr=bid_map.begin();itr!=bid_map.end();itr++)
       {
          if(itr->first>bbyk[in])
            break;
          in++;
       }
       key=in;
       cout<<"key is: "<<key<<endl;
       i=1;
       for(itr=bid_map.begin();itr!=bid_map.end();itr++)
       {
          if(i==key+2)
            break;
          else
            win_set.push_back(itr->first);
          i++;
       }
       first_loser=win_set[key];
       cout<<"first_loser is: "<<first_loser<<endl;
       cout<<"payment made will be: "<<endl;
       payment=min((curr_budget_value)/key,first_loser);
       cout<<payment*key<<endl;
       total_payment[value]=total_payment[value]+payment*key;
       utility=0;
       for(i=0;i<key;i++)
       {
         utility=utility+(payment-win_set[i]);
         cout<<"utility is: "<<utility<<endl;
       }
       utility_sum=utility_sum+utility/key;
     }
     cout<<"Proposed budget_value was :"<<proposed_budget_value<<endl;
     cout<<"Rs "<<(proposed_budget_value*3)/10<<" is distributed among all peer graders"<<endl;
     cout<<"Total money spend for the task is : "<<total_payment[value]<<endl;
     //for utility
     value++;
  }
  average_payment=0;
  cout<<"total payments are : "<<endl;
  for(i=0;i<100;i++)
    cout<<total_payment[i]<<" ";
  cout<<"Average payment will be: "<<endl;
  for(i=0;i<100;i++)
    average_payment=average_payment+total_payment[i];
  average_payment=average_payment/100;
  cout<<average_payment<<endl;
  cout<<"final utility is :"<<utility_sum<<endl;
  cout<<"average utility is: "<<utility_sum/100;
  return 0;
}