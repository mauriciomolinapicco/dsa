#include <iostream>

including namespace std;

int main() {
    string nombre;
    cin >> nombre;
    cout << "Hola " << nombre << endl;

    string s = "Mauricio";
    s.push_back("x"); //same as append

    s += "x";

    return 0;
}