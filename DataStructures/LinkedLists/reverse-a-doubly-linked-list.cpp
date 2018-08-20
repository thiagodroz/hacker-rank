DoublyLinkedListNode* reverse(DoublyLinkedListNode* head) {
  if (head == NULL)
    return NULL;
  
  DoublyLinkedListNode *current = head, *tmp;

  while (current->next != NULL) {
    tmp = current->next;
    current->next = current->prev;
    current->prev = tmp;
    current = tmp;
  }
  
  current->next = current->prev;
  current->prev = NULL;
  
  return current;
}
