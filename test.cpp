#include <random>
#include<bits/stdc++.h>
using namespace std;
int main(int, char**)
{
    // random device class instance, source of 'true' randomness for initializing random seed
    std::random_device rd; 

    // Mersenne twister PRNG, initialized with seed from previous random device instance
    std::mt19937 gen(rd()); 

    int i;
    float sample;
    for(i = 0; i < 1000; ++i)
    {
        // instance of class std::normal_distribution with specific mean and stddev
        std::normal_distribution<float> d(7,8); 

        // get random number with normal distribution using gen as random source
        sample = d(gen); 

        // profit
        cout<<int(sample)<<endl;
    }
    return 0;
}
