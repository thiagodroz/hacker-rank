bool isBST(Node *root, int min, int max) {
  if (root == NULL)
    return true;

  if (root->data <= min || root->data >= max)
    return false;

  return isBST(root->left, min, root->data) && isBST(root->right, root->data, max);
}

bool checkBST(Node *root) {
  return isBST(root, 0, 10000);
}
