#include <iostream>
#include <stdlib.h>
#include <queue>

using namespace std;

typedef struct Nodo {
    int val;
    Nodo* left;
    Nodo* right;
} Nodo;


void bfs(Nodo* root) {
    if (root == NULL) {
        return;
    }

    queue<Nodo*> q;
    q.push(root);

    while(!q.empty) {
        Nodo* nodo = q.front();
        q.pop(); // lo saco de la cola

        cout << nodo->val << endl;
        if (nodo->left != NULL) {
            q.push(nodo->left);
        }
        if (nodo->right != NULL) {
            q.push(nodo->right);
        }
    }
}


int main() {
    Nodo* root = (Nodo*)malloc(sizeof(Nodo));

    root→val = 3;

    Nodo* l1 = (Nodo*)malloc(sizeof (Nodo));
    Nodo* r1 = (Nodo*)malloc(sizeof(Nodo));

    l1→val = 1; 
    r1→val = 5;

    root→left = l1; 
    root→right = r1;

    Nodo* l2 = (Nodo*)malloc(sizeof(Nodo));
    Nodo* r2 = (Nodo*)malloc(sizeof(Nodo));

    l2→val = 4; 
    r2→val = 6;

    r1→ left = l2; 
    r1→right = r2;

    bfs(root);

    return 0;
}