SinglyLinkedListNode* mergeLists(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2) {
  SinglyLinkedListNode* returned_node = new SinglyLinkedListNode(0);
  
  if (head1 == NULL && head2 == NULL) {
    return NULL;
  } else if (head2 == NULL) {
    returned_node->data = head1->data;
    head1 = head1->next;
  } else if (head1 == NULL) {
    returned_node->data = head2->data;
    head2 = head2->next;
  } else if (head1->data < head2->data) {
    returned_node->data = head1->data;
    head1 = head1->next;
  } else {
    returned_node->data = head2->data;
    head2 = head2->next;
  }
  
  returned_node->next = mergeLists(head1, head2);
  
  return returned_node;
}
