#include<bits/stdc++.h>
using namespace std;
bool Is_leap(int y)
{
	if(y%4==0)
	{
		if(y%100==0)
		{
	       if(y%400==0)
		     return true;
	    }
	    else
	     return true;
	}
	return false;
}
int main()
{
	int t;  //test cases
	cin>>t;
    while(t>0)
    {
	  int max,count=0;
      string s;
      cin>>s;
      int yyyy,dd,mm;
      string y,d;  //will be substrings of s
      y=s.substr(0,4);
      string m=s.substr(5,2);
      d=s.substr(8,2);
      yyyy=stoi(y);
      mm=stoi(m);
      dd=stoi(d);
      if(dd%2==0)
      	dd++;
      while((dd%2!=0)&&((dd+2)%2!=0))
       {
    	if(mm==1||mm==3||mm==5||mm==7||mm==8||mm==10||mm==12)
    	  max=31;
    	else if(mm==2&&Is_leap(yyyy))
		  max=29;
		else if(mm==2&&!Is_leap(yyyy))
		  max=28;
		else
		  max=30; 
	    if(dd%2!=0) 
		{
			for(dd=dd;dd<=max;dd+=2)
    		    count++;
    		if(max%2==0)
    			dd=1;
    		else
		    	dd=2;
		} 
		if(mm==12){
		    mm=1;
		}
		else
		  mm++;
	  }
	  cout<<count<<endl;
	  t--;
	}
	return 0;
}
