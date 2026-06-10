// You are a professional robber planning to rob houses along a street.
// Each house has a certain amount of money stashed, the only constraint
// stopping you from robbing each of them is that adjacent houses have
// security systems connected and it will automatically contact the police
// if two adjacent houses were broken into on the same night.

// Given an integer array nums representing the amount of money of each house,
// return the maximum amount of money you can rob tonight without alerting the
// police.

#include <iostream>
#include <vector>
using namespace std;

int dp(vector<int>& nums, int n, unordered_map<int, int>& mem) {
    if (n == 0) return nums[0];
    if (n == 1) return max(nums[0], nums[1]);

    if (mem.find(n) != mem.end()) {
        return mem[n];
    }
    int res = max(dp(nums, n-1, mem), dp(nums, n-2, mem) + nums[n]);
    mem[n] = res;
    return res;
}

int rob(vector<int>& nums) {
    unordered_map<int, int> mem;
    return dp(nums, nums.size()-1, mem);
}

int main() {
    vector<int> a = {1, 2, 3, 1};
    cout << rob(a) << endl; // expected: 4

    vector<int> b = {2, 7, 9, 3, 1};
    cout << rob(b) << endl; // expected: 12

    return 0;
}
