#include<bits/stdc++.h>
using namespace std;
int main()
{
	int k,i,j,q,r,d,temp_var,m;
	cin>>k;
	vector<int> temp,total_digits;
	i=m=0;
	total_digits.push_back(0);
	total_digits.push_back(0);
	while(k>total_digits[m])
	{
		if(i==0)
		{
			total_digits.pop_back();
			total_digits.pop_back();
		}
		cout<<"in"<<endl;
		temp.push_back(9*int(pow(10,i)));
		if(i==0)
            total_digits.push_back(temp[i]);
		else
		{
            cout<<"temp[i] is: "<<temp[i]<<endl;
            total_digits.push_back(total_digits[i-1]+(temp[i])*(i+1));
            cout<<"total_digits is: "<<total_digits[i]<<endl;
            cout<<"out"<<endl;
		}
		cout<<"total digits is: "<<total_digits[i]<<endl;
		cout<<"k is: "<<k<<endl;
		i++;
		m=i-1;
  	}
	cout<<"i is: "<<i<<endl;
	k=k-total_digits[i-1];
	cout<<"k is: "<<k<<endl;
    q=k/i;
    r=k%i;
    for(j=i;j>0;j--)
    	q=q+temp[j-1];
    if(r==0)
    	cout<<q%10<<endl;
    else
    {
    	cout<<"q is: "<<q<<endl;
    	q=q+1;
    	temp_var=q;
    	j=0;
    	while(temp_var!=0)
    	{
    		temp_var=temp_var/(int(pow(10,i)));
    		j++;
    	}
        d=j-r+1;
        q=q/(int(pow(10,d-1)));
        cout<<"q is"<<q%10<<endl;
    }
   return 0;
}