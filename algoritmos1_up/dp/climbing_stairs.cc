#include <iostream>
#include <vector>
using namespace std;

// You are climbing a staircase with n steps.
// Each time you can climb 1 or 2 steps.
// In how many distinct ways can you climb to the top?

// dp 0 = 0
// dp 1 = 1
// dp 2 = 2
// dp 3 = 3
// dp 4 = 5
// dp n = dp(n-1) + dp(n-2)

int dp(int n, unordered_map<int, int>& mem) {
    if (n<=2) return n;
    if (mem.find(n) != mem.end()) {
        return mem[n];
    }
    int res = dp(n-1, mem) + dp(n-2, mem);
    mem[n] = res;
    return res;
}

int climbStairs(int n) {
    unordered_map<int, int> mem;
    return dp(n, mem);
}

int main() {
    cout << climbStairs(2) << endl; // expected: 2
    cout << climbStairs(3) << endl; // expected: 3
    cout << climbStairs(5) << endl; // expected: 8
    cout << climbStairs(32) << endl;
    return 0;
}

