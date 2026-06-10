#include <iostream>
#include <unordered_map>

using namespace std;

class LRUCache {
private:
   struct Node {
    int key;
    int val;
    Node* prev;
    Node* next;
    Node(int k, int v) : key(k), val(v), prev(nullptr), next(nullptr) {} //constructor
   };

   int cap; //capacity
   unordered_map<int, Node*> hm;
   Node* left;
   Node* right;

   void remove(Node* node) {
    Node* prevNode = node->prev;
    Node* nextNode = node->next;
    prevNode->next = nextNode;
    nextNode->prev = prevNode;
   }

   // insertar nodo a la derecha (por ser el mas recientemente usado)
   void insert(Node* node) {
    Node* prevNode = right->prev;
    prevNode->next = node;
    right->prev = node;
    node->prev = prevNode;
    node->next = right;
   }

public:
  LRUCache(int capacidad) {
    cap = capacidad;
    left = new Node(0, 0); 
    right = new Node(0, 0);

    // al principio contamos con una DLL vacia, compuesta solo por los dummy nodes left/right
    left->next = right;
    right->prev = left;
  }

  // destructor para liberar memoria. Powered by ChatGPT
  ~LRUCache() {
    Node* curr = left;
    while (curr) {
        Node* next = curr->next;
        delete curr;
        curr = next;
    }
  }

  int get(int clave) { // Si la clave existe retornar el valor else -1
    if (hm.find(clave) != hm.end()) {
        remove(hm[clave]); // eliminar el nodo actual de la DLL
        insert(hm[clave]); // insertar el nodo a la derecha porque ahora es el MRU
        return hm[clave]->val;
    }
    return -1;
  }

  void put(int clave, int valor) {
        // Si la clave ya existe, actualizar su valor
        // Si el cache esta lleno, eliminar el elemento
        // menos recientemente usado antes de insertar

      // caso 1 = la clave existe
      if (hm.find(clave) != hm.end()) {
            Node* existingNode = hm[clave];
            existingNode->val = valor; 
            remove(existingNode);  //lo saco de la posicion actual    
            insert(existingNode);  // lo muevo a la derecha y queda como MRU
            return;
        }
      
      // caso 2 = la clave no existe
      Node* newNode = new Node(clave, valor);
      hm[clave] = newNode;
      insert(newNode);

      // si excedo la capacidad obtengo y elimino el LRU
      if (hm.size() > cap) {
          Node* lru = left->next; 
          remove(lru); 
          hm.erase(lru->key);  //borro la clave del hashmap
          delete lru; // liberar memoria del nodo eliminado
      }
    }
};

int main() {
  LRUCache cache(2);

  cache.put(1, 1);
  cache.put(2, 2);
  cout << cache.get(1) << endl; // 1
  cache.put(3, 3);
  cout << cache.get(2) << endl; // -1
  cache.put(4, 4);
  cout << cache.get(1) << endl; // -1
  cout << cache.get(3) << endl; // 3
  cout << cache.get(4) << endl; // 4

  return 0;
}
