#include <iostream>
#include <cmath>
using namespace std;

string reverse(string s) {
    int n = s.size();
    if (n <= 1) return s;

    int m = floor(n/2);
    string s1 = "";
    string s2 = "";

    for (int i=0; i<n; i++) {
        if (i<m) {
            s1 += s[i];
        } else {
            s2 += s[i];
        }
    }

    return reverse(s2) + reverse(s1);

    
}

int main() {
    string s;
    cin >> s;

    string r = reverse(s);

    cout << r << endl;

    return 0;
}
