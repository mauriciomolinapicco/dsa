#include <iostream>
using namespace std;

bool is_pow_two(long long n) {
    if (n == 1) return true;
    if (n % 2 != 0) return false;
    return is_pow_two(n/2);
}

int main() {
    long long n;
    string result;
    cin >> n;

    if (n <= 0) {
        cout << "false" << endl;
        return 0;
    }


    (is_pow_two(n) == 1) ? result="true" : result="false";
    cout << result << endl;
    
    return 0;
}
