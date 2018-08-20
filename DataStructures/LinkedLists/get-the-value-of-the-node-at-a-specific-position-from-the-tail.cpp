int getNode(SinglyLinkedListNode* head, int positionFromTail) {
  SinglyLinkedListNode *fast = head, *slow = head;
  
  for (int i = 0; i < positionFromTail; i++) {
    fast = fast->next;
  }

  while (fast->next != NULL) {
    fast = fast->next;
    slow = slow->next;
  }
  
  return slow->data;
}
