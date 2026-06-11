#include <iostream>
#include <vector>
using namespace std;

void merge(vector<int>& v, int l, int mid, int r) {
    vector<int> left(v.begin() + l, v.begin() + mid + 1);
    vector<int> right(v.begin() + mid + 1, v.begin() + r + 1);

    int i = 0, j = 0, k = l;
    while (i < left.size() && j < right.size()) {
        if (left[i] <= right[j]) v[k++] = left[i++];
        else                      v[k++] = right[j++];
    }
    while (i < left.size())  v[k++] = left[i++];
    while (j < right.size()) v[k++] = right[j++];
}

void mergeSort(vector<int>& v, int l, int r) {
    if (l >= r) return;
    int mid = (l + r) / 2;
    mergeSort(v, l, mid);
    mergeSort(v, mid + 1, r);
    merge(v, l, mid, r);
}

int main() {
    vector<int> v = {5, 3, 8, 1, 9, 2, 7, 4, 6};
    mergeSort(v, 0, v.size() - 1);
    for (int x : v) cout << x << " ";
    cout << endl; // expected: 1 2 3 4 5 6 7 8 9
    return 0;
}
