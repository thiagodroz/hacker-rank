    public static Node insert(Node head,int data) {
        if (head != null) {
            Node currentNode = head;
            
            while (currentNode.next != null) {
                currentNode = currentNode.next;
            }

            currentNode.next = new Node(data);
        } else {
            head = new Node(data);
        }
        
        return head;
    }