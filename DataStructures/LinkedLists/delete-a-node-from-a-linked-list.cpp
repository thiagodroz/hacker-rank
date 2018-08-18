SinglyLinkedListNode* deleteNode(SinglyLinkedListNode* head, int position) {
  if (position == 0) {
    return head->next;
  }
  
  SinglyLinkedListNode* previous_node = NULL;
  SinglyLinkedListNode* current_node = head;
  int current_index = 0;
  
  while (current_index < position) {
    previous_node = current_node;
    current_node = current_node->next;
    current_index++;
  }
  
  previous_node->next = current_node->next;
  
  return head;
}
