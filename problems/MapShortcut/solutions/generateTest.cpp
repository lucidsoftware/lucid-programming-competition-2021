#include <cmath> 
#include <iostream>

using namespace std;

int main()
{
    int steps = 10000;
    cout << steps << "\n";
    for(int i = 0; i < steps; i++){
        cout << ((rand() % 2 == 0) ? "Left " : "Right ")<< (rand() % 180) + 1 << " " << (rand() % 100) + 1 << "\n";
    }
    return 0;
}
