	  public static int getHeight(Node root){
        if(root == null) {
            return -1;
        }
        int leftDepth = getHeight(root.left);
        int rightDepth = getHeight(root.right);

        return (leftDepth > rightDepth ? leftDepth : rightDepth) + 1;
    }
