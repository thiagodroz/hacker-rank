SinglyLinkedListNode* insertNodeAtTail(SinglyLinkedListNode* head, int data) {
  SinglyLinkedListNode *temp = new SinglyLinkedListNode(data);
  
  if (head == NULL) {
    head = temp;
  } else if (head->next == NULL) {
    head->next = temp;

    return head;
  } else {
    insertNodeAtTail(head->next, data);
  }
  
  return head;
}
