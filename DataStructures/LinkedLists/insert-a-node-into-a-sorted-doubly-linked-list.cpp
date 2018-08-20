DoublyLinkedListNode* sortedInsert(DoublyLinkedListNode* head, int data) {
  if (head == NULL) {
    DoublyLinkedListNode* node = new DoublyLinkedListNode(data);
    
    return node;
  }

  if (head->data <= data) {
    head->next = sortedInsert(head->next, data);
    head->next->prev = head;
  } else if (head->data > data) {
    DoublyLinkedListNode *node = new DoublyLinkedListNode(data);
    
    node->next = head;
    node->prev = head->prev;

    head->prev = node;
    head = node;
  }

  return head;
}
