#include<bits/stdc++.h> 
using namespace std;
void engineers()
{
	char resp;
	ofstream fout;
	ifstream fin;
	fin.open("engineers.txt");
	char ch;
	cout<<ch;
	while(!fin.eof())
	{
		cout<<ch;
		ch=fin.get();
	}
	cout<<"\n\nWant to ask some more questions ? Press y for yes and n for no";
	cin>>resp;
	if(resp=='y')
	{   
	    string s;
	    fout.open("engineers.txt", fstream::app);
	    getchar();
		getline(cin,s);
		fout<<s;
	}
}
void doctors()
{
	ofstream fout;
    ifstream fin;
	fin.open("doctor.txt");
	char ch,resp;
	cout<<ch;
	while(!fin.eof())
	{
		cout<<ch;
		ch=fin.get();
	}	
	cout<<"\n\nWant to ask some more questions ? Press y for yes and n for no";
	cin>>resp;
	if(resp=='y')
	{   
	    string s;
	    fout.open("doctor.txt", fstream::app);
	    getchar();
		getline(cin,s);
		fout<<s;
	}
}
void police()
{
	ofstream fout;
	ifstream fin;
	char resp;
	fin.open("police.txt");
	char ch;
	cout<<ch;
	while(!fin.eof())
	{
		cout<<ch;
		ch=fin.get();
	}
	cout<<"\n\nWant to ask some more questions ? Press y for yes and n for no";
	cin>>resp;
	if(resp=='y')
	{   
	    string s;
	    fout.open("police.txt", fstream::app);
	    getchar();
		getline(cin,s);
		fout<<s;
	}
}
class profile{
	private:
		string s[9]={"Engineer","ENGINEER","engineer","Doctor","DOCTOR","doctor","police","POLICE","Police"};
	public:
	void profileName(string p)
	{	   
			if(p==s[0]||p==s[1]||p==s[2])
			{
				engineers();
			}
			else if(p==s[3]||p==s[4]||p==s[5])
			{
			     doctors();
			}
			else if(p==s[6]||p==s[7]||p==s[8])
			{
				police();
			} 
			else
			cout<<"Sorry I do not recognised what you typed,please see the spelling mistake \n or some inappropriate uses of capital letter of capital and small letters :(";
		
   	}
	
};
int main()
{
  while(1)
  {
	profile p1;
	cout<<"Which profile you want to search?";
	string k,m;
	cin>>k;
	p1.profileName(k);
	cout<<"\nWrite e and hit enter to exit or press any other key to continue:";
	cin>>m;
	if(m=="e")
	{   
	    cout<<" \n Thanks for using our service ";
	    return 0;
	}
	cout<<"\n";
  }
	return 0;
}
