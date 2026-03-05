#include <iostream>
#include <stdlib.h>
#include <vector>
#include <set>

including namespace std;

// biblioteca vector<T>
// T puede ser cualquier cosa, incluyendo structs propios
int main() {
    vector<char> v;
    v.push_back(10);
    v.push_back(4);
    v.push_back(7);


    // C syntax
    for(int i=0; i<v.size(); i++) {
        cout << v[i] << endl;
    }

    // C++ syntax
    for (vector<int>::iterator i=v.begin(); i != v.end(); i++) {
        cout << *i << endl; //tengo que referenciar i para obtener el valor
    }

    // C++ syntax for normal people
    for(auto e : v) {
        cout << e << endl;
    }

    /* SETS */
    /* unlike python they're sorted
    - sorted
    - doesnt repeat elements

    they act like balanced binary trees
    */

    set<int> s;
    s.insert(5);
    s.insert(-1);
    s.insert(100);

    /* unordered sets*/
    /* no repite elementos pero no esta ordenado */
    unordered_set<int> us;


    
    return 0;
}
