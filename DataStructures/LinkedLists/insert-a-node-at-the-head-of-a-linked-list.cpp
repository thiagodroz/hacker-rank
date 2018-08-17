SinglyLinkedListNode* insertNodeAtHead(SinglyLinkedListNode* head, int data) {
  SinglyLinkedListNode* temp = new SinglyLinkedListNode(data);

  if (head == NULL) {
    return temp;
  } else {
    temp->next = head;
    head = temp;
    
    return head;
  }
}
