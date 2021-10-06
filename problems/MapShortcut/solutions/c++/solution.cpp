#define _USE_MATH_DEFINES
 
#include <cmath> 
#include <iostream>

using namespace std;

float toRadians(float degrees) {
    return degrees * M_PI / 180.0;
}

float toDegrees(float radians) {
    return radians * 180.0 / M_PI;
}

int main()
{
    int steps;
    cin >> steps;
    float location_x = 0;
    float location_y = 0;
    int facing = 0;
    for(int i = 0; i < steps; i++){
        string direction;
        int angle;
        int paces;
        cin >> direction >> angle >> paces;
        if(direction == "Right") {
            angle = 360 - angle;
        }
        facing = (facing + angle) % 360;
        location_x += cos(toRadians(facing)) * paces;
        location_y += sin(toRadians(facing)) * paces;
    }
    float distance = sqrt((location_x * location_x) + (location_y * location_y));
    float heading = toDegrees(acos(location_x / distance));
    cout << (location_y > 0 ? "Left " : "Right ") << floor(heading + 0.5) << " " << floor(distance + 0.5) << "\n";
    return 0;
}
