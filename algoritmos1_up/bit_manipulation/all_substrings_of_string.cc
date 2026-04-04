#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main() {
    string s = "hello world";
    n = s.length();
    n_combinations = pow(2, n);


    for (int x=0; x<n_combinations; x++) {
        for (int b=0; b<n; b++) {
            bit_prendido = (x & (1 << b))
            if (bit_prendido) {
                cout << s[b];
            }
        }
        cout << endl;
    }
}