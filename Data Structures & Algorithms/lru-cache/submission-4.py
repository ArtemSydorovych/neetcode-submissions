class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashes = {} # key: int, val: Node 
        self.capacity = capacity

        # Dummy nodes
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.right.prev = self.left
        self.left.next = self.right

    def get(self, key: int) -> int:
        if key in self.hashes:
            node = self.hashes[key]
            self.removeNode(node)
            self.insert(node)
            return node.val
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.hashes:
            node = self.hashes[key]
            node.val = value
            self.removeNode(node)
            self.insert(node)
        else:
            if self.capacity == len(self.hashes):
                lru = self.left.next
                self.removeNode(lru)
                del self.hashes[lru.key]
            
            node = Node(value, key)
            self.hashes[key] = node
            self.insert(node)

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def removeNode(self, node : Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev