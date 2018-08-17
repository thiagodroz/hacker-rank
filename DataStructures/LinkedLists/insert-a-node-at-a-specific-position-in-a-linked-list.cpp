SinglyLinkedListNode* insertNodeAtPosition(SinglyLinkedListNode* head, int data, int position) {
  SinglyLinkedListNode* new_node = new SinglyLinkedListNode(data);
  SinglyLinkedListNode* current_node = head;
  SinglyLinkedListNode* previous_node = NULL;
  int i = 0;
  
  while (i < position) {
    previous_node = current_node;
    current_node = current_node->next; 
    i++;
  }
  
  new_node->next = current_node;
  
  if (previous_node != NULL) {
    previous_node->next = new_node;
    
    return head;
  }
  
  return new_node;
}
