static bool hasCycle(SinglyLinkedListNode head) {
    var slow = head;
    
    if (slow == null) return false;
    
    var fast = head.next;
    
    if (fast == null) return false;
    
    while (fast.next != null && fast.next.next != null) {
        if (slow == fast) {
            return true;
        }
        
        slow = slow.next;
        fast = fast.next.next;
    }
    
    return false;
}
