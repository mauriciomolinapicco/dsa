#include <iostream>
#include <vector>
using namespace std;

void printv(vector<int>& v) { 
    int n = v.size();
    for (int i=0; i<n; i++) {
        if (i) {
            cout << " ";
        }
        cout << v[i];
    }
    cout << endl;
}

void s(vector<int>&v, int i, vector<int>& actual) {
    if (i == v.size()) {
        printv(actual);
        return;
    }

    actual.push_back(v[i]);
    s(v,i+1,actual);
    actual.pop_back();
    s(v,i+1,actual);
}

void subsets(vector<int>& v) {
    vector<int> actual;
    s(v, 0, actual);
}

int main() {
    vector<int> v = {1, 2, 3, 4};
    subsets(v);
    return 0;
}