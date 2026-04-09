#include <stdlib.h>
#include <iostream>

using namespace std;

//asumo que cada valor es unico

struct Nodo {
    int val;
    Nodo* next;
};

Nodo* head = NULL;

void agregar(int valor) {
    
    Nodo* new_node = new Nodo();
    new_node->val = valor;
    new_node->next = head;
    head = new_node;
}

Nodo* buscar_anterior(int valor) {
    if(head == NULL) return NULL;
    Nodo* tmp = head;
    while (tmp->next) {
        if(tmp->next->val == valor) {
            return tmp;
        }
        tmp = tmp->next;
    }
    
    return NULL;
}

Nodo* buscar(int valor) {
    if (head->val == )
    Nodo* ant = buscar_anterior(valor);
    return ant ? ant->next : NULL;
}

void eliminar(int valor) {
    Nodo* anterior = buscar_anterior(valor);
    if (anterior == NULL) return;
    Nodo* tmp = anterior->next->next;
    free(anterior->next);
    anterior->next = tmp;
}

void print_lista() {
    Nodo* current = head;
    for(int i=0; current!=NULL; i++, current = current->next) {
        if(i != 0) cout << " ";
        cout << current->val;
        
    }
    cout << endl;
}


int main() {
    agregar(1);
    agregar(2);
    agregar(4);

    print_lista();

    Nodo* a = buscar_anterior(2);
    cout << "valor: " << a->val << endl;

    eliminar(1);
    print_lista();

    return 0;
}
