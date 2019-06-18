#include<iostream>
using namespace std;
class WeightX
{
public:
	 int kg,gms;
	 WeightX()
	 {
	 	kg=0;
	 	gms=0;
	 }
	 WeightX(int k,int g)
	 {
         kg=k;
         gms=g;
	 }
	 friend WeightX sum(WeightX w1,WeightX w2);
	 void display(WeightX w)
	 {
         cout<<"Sum of the two weights is : "<<w.kg<<" Kilograms "<<w.gms<<" Grams";
	 }
};
WeightX sum(WeightX w1,WeightX w2)
{
   WeightX w3;
   w3.kg=w1.kg+w2.kg;
   w3.gms=w1.gms+w2.gms;
   if(w3.gms>=1000)
   {
   	w3.kg++;
   	w3.gms=w3.gms-1000;
   }
   return w3;
}
int main()
{
	WeightX w1(10,900),w2(24,400);
    WeightX w3=sum(w1,w2);
    w3.display(w3);
    return 0;
}