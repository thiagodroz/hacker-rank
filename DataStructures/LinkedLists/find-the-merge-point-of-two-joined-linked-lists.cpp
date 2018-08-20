int findMergeNode(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2) {
  SinglyLinkedListNode *current_a = head1, *current_b = head2;

  while (current_a != current_b) {
    if (current_a->next == NULL) {
      current_a = head2;
    } else {
      current_a = current_a->next;
    }
    
    if (current_b->next == NULL) {
      current_b = head1;
    } else {
      current_b = current_b->next;
    }
  }
  
  return current_b->data;
}
