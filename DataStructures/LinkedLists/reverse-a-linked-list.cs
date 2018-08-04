static SinglyLinkedListNode reverse(SinglyLinkedListNode head) {
    SinglyLinkedListNode current = head;
    SinglyLinkedListNode last = null;
    
    while(current != null) {
        var next = current.next;
        current.next = last;
        last = current;
        current = next;
    }
    
    return last;
}
