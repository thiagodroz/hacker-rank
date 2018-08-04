static bool CompareLists(SinglyLinkedListNode head1, SinglyLinkedListNode head2) {
    var current1 = head1;
    var current2 = head2;
    
    while(current1 != null && current2 != null) {
        if (current1.data != current2.data) {
            return false;
        }
        
        current1 = current1.next;
        current2 = current2.next;
    }
    
    if(current1 != current2) {
        return false;
    }
    
    return true;
}
