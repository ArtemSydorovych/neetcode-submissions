class Node{
    int value;
    Node next;
    Node prev;

    public Node(int value){
        this.value = value;
    }
}

class Deque {
    
    private Node head;
    private Node tail;

    public Deque() {
    }

    public boolean isEmpty() {
        return head == null || tail == null;
    }

    public void append(int value) {
        Node newNode = new Node(value);
        
        if (this.isEmpty()){
            head = newNode;
            tail = newNode;
            return;
        }
        
    
        newNode.prev = tail;
        tail.next = newNode;
        tail = newNode;
    }

    public void appendleft(int value) {
        Node newNode = new Node(value);
        
        if (this.isEmpty()){
            head = newNode;
            tail = newNode;
            return;
        }

        newNode.next = head;
        head.prev = newNode;
        head = newNode;
    }

    public int pop() {
        if (isEmpty()) {
            return -1;
        }
        
        int value = tail.value;
        
        if (head == tail) {
            head = null;
            tail = null;
        } else {
            tail = tail.prev;
            tail.next = null;
        }
        
        return value;
    }

    public int popleft() {
        if (this.isEmpty()){
            return -1;
        }

        int value = head.value;
        if (head == tail){
            head = null;
            tail = null;
            return value;
        }else{
            head = head.next;
            head.prev = null;
        }

        return value;
    }
}
