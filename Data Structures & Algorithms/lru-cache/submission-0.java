public class Node{
    int value;
    int key;

    Node prev;
    Node next;
    Node(int key, int value) { this.key = key; this.value = value; }
}

class LRUCache {
    private int capacity;
    private Map<Integer, Node> map = new HashMap<>();
    
    // sentinels: those are never in the map just gives an oportunity to get rid of null checks for each opeartion
    private Node head = new Node(0,0);
    private Node tail = new Node(0,0);

    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        var node = map.get(key);
        if (node == null){
            return -1;
        }

        moveToFront(node);
        return node.value;
    }
    
    public void put(int key, int value) {
        var node = map.get(key);
        if (node == null){
            Node newNode = new Node(key,value);
            map.put(key, newNode);
            addFirst(newNode);
            cleanUp();
            return;
        }
        node.value = value;
        moveToFront(node);
    }

    private void cleanUp(){
        if (map.size() > capacity){
            Node lru = tail.prev;
            map.remove(lru.key);
            remove(lru);
        }
    }

    private void addFirst(Node n) {
        n.next = head.next;
        n.prev = head;
        head.next.prev = n;
        head.next = n;
    }


    private void moveToFront(Node n){
        remove(n);
        addFirst(n);
    }
    
    private void remove(Node n) {
        n.next.prev = n.prev;
        n.prev.next = n.next;
    }
}



