static void levelOrder(Node root){
    Queue<Node> queue = new LinkedList<>();
    
    queue.add(root);
    
    while(!queue.isEmpty()) {
        Node currentNode = queue.remove();
        
        System.out.printf("%d ", currentNode.data);
        
        if (currentNode.left != null) {
            queue.add(currentNode.left);
        }
        if (currentNode.right != null) {
            queue.add(currentNode.right);
        }
    }
}