class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.hm = {}

        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    #eliminar de la lista
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    #insertar a la derecha
    def insert(self, node):
        prev = self.right.prev
        right = self.right
        prev.next = node
        right.prev = node
        node.prev = prev
        node.next = right

    def get(self, key: int) -> int:
        if key in self.hm:
            self.remove(self.hm[key])
            self.insert(self.hm[key])
            return self.hm[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.remove(self.hm[key])
        self.hm[key] = Node(key, value)
        self.insert(self.hm[key])

        if len(self.hm) > self.cap:
            lru = self.left.next
            self.remove(lru) #borrado de la double linked list
            del self.hm[lru.key]
