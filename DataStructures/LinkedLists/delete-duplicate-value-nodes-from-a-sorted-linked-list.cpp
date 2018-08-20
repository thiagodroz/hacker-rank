SinglyLinkedListNode* removeDuplicates(SinglyLinkedListNode* head) {
  SinglyLinkedListNode *first = head->next, *second = head;
  
  while (first != NULL) {
    if (second->data == first->data) {
      first = first->next;
      second->next = first;
    } else {
      second = first;
      first = first->next;
    }
  }

  return head;
}
