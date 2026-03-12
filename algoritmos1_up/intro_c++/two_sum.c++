#include <iostream>
#include <cmath>
#include <unordered_map>
#include <vector>

using namespace std;

int main() {
    int n;
    int target;

    vector<int> nums;
    unordered_map<int, int> m;

    cin >> n;

    for(int i=0; i<n; i++) {
        int tmp;
        cin >> tmp;
        nums.push_back(tmp);
    }

    cin >> target;

    for(int i=0; i<n; i++) {
        int c = target - nums[i];

        if(m.find(c) != m.end()) {
            cout << m[c] << " " << i << endl;
            return 0;
        }

        m[nums[i]] = i;
    }


    return 0;
}
