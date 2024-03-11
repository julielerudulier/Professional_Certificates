public class AVL<T extends Comparable<? super T>> {

    public void updateHeightAndBF(AVLNode<T> currentNode) {
      int leftHeight;
	    if (currentNode.getLeft() == null) { 
		    leftHeight = -1;
	    } else { 
		    leftHeight = currentNode.getLeft().getHeight();
	    }
	
	    int rightHeight;
	    if (currentNode.getRight() == null) {
		    rightHeight = -1;
	    } else {
		    rightHeight = currentNode.getRight().getHeight();
	    }
        
	    int currentHeight = Math.max(leftHeight, rightHeight) + 1;
	    currentNode.setHeight(currentHeight);

	    int currentBF = leftHeight - rightHeight;
	    currentNode.setBalanceFactor(currentBF);
    }
  
    public AVLNode<T> rotateLeft(AVLNode<T> currentNode) {
      T temp = currentNode.getData();
      AVLNode<T> rightChild = currentNode.getRight();
	    currentNode.setRight(rightChild.getLeft());
	    rightChild.setLeft(currentNode);
	    updateHeightAndBF(currentNode);
	    updateHeightAndBF(rightChild);
	    return rightChild;
    }

    public AVLNode<T> rotateRight(AVLNode<T> currentNode) {
      T temp = currentNode.getData();
	    AVLNode<T> leftChild = currentNode.getLeft();
      currentNode.setLeft(leftChild.getRight());
	    leftChild.setRight(currentNode);
	    updateHeightAndBF(currentNode);
	    updateHeightAndBF(leftChild);
	    return leftChild;
    }
  
    public AVLNode<T> balance(AVLNode<T> currentNode) {
        updateHeightAndBF(currentNode);

        if (currentNode.getBalanceFactor() == -2) {
            if (currentNode.getRight().getBalanceFactor() == 1) {
                currentNode.setRight(rotateRight(currentNode.getRight()));
            }
            currentNode = rotateLeft(currentNode);
        } else if (currentNode.getBalanceFactor() == 2) {
            if (currentNode.getLeft().getBalanceFactor() == -1) {
                currentNode.setLeft(rotateLeft(currentNode.getLeft()));
            }
            currentNode = rotateRight(currentNode);
        }
        return currentNode;
    }
}
