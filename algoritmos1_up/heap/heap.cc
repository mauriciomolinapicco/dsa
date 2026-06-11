#include <iostream>
#include <vector>
using namespace std;

struct MinHeap {
    vector<int> data;

    int parent(int i) { return (i - 1) / 2; }
    int left(int i)   { return 2 * i + 1; }
    int right(int i)  { return 2 * i + 2; }

    void push(int val) {
        data.push_back(val);
        int i = data.size() - 1;
        while (i > 0 && data[i] < data[parent(i)]) {
            swap(data[i], data[parent(i)]);
            i = parent(i);
        }
    }

    int top() { return data[0]; }

    void pop() {
        data[0] = data.back();
        data.pop_back();
        int i = 0;
        while (true) {
            int smallest = i;
            int l = left(i), r = right(i);
            int n = data.size();
            if (l < n && data[l] < data[smallest]) smallest = l;
            if (r < n && data[r] < data[smallest]) smallest = r;
            if (smallest == i) break;
            swap(data[i], data[smallest]);
            i = smallest;
        }
    }

    bool empty() { return data.empty(); }
};

int main() {
    MinHeap h;
    h.push(5);
    h.push(3);
    h.push(8);
    h.push(1);
    h.push(4);

    while (!h.empty()) {
        cout << h.top() << " ";
        h.pop();
    }
    cout << endl; // expected: 1 3 4 5 8

    return 0;
}
