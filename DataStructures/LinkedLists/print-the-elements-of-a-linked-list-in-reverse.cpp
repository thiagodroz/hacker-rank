// Complete the reversePrint function below.

void reversePrint(SinglyLinkedListNode* head) {
  if (head == NULL) {
    return;
  }
  
  reversePrint(head->next);
  
  cout << head->data << '\n';
}
