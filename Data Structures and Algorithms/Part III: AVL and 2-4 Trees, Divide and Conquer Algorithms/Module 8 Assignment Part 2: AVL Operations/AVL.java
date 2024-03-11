import java.util.NoSuchElementException;

public class AVL<T extends Comparable<? super T>> {

    private AVLNode<T> root;
    private int size;

    public void add(T data) {
      if (data == null) { throw new IllegalArgumentException(); }
	    this.root = addHelper(this.root, data);
    }

    private AVLNode<T> addHelper(AVLNode<T> curr, T data) {
        if (curr == null) {
            size++;
            return new AVLNode<T>(data);
        } else if (data.compareTo(curr.getData()) < 0) {
            curr.setLeft(addHelper(curr.getLeft(), data));
        } else if (data.compareTo(curr.getData()) > 0) {
            curr.setRight(addHelper(curr.getRight(), data));
        }
        curr = balance(curr);
        return curr;
    }
  
    public T remove(T data) {
        if (data == null) { throw new IllegalArgumentException(); }
        AVLNode<T> dummy = new AVLNode<T>(null);
        this.root = helperRemove(this.root, data, dummy);
        return dummy.getData();
    }

    private AVLNode<T> helperRemove(AVLNode<T> curr, T data, AVLNode<T> dummy) {
        if (curr == null) {
            throw new NoSuchElementException();
        } else if (data.compareTo(curr.getData()) < 0) {
            curr.setLeft(helperRemove(curr.getLeft(), data, dummy));
        } else if (data.compareTo(curr.getData()) > 0) {
            curr.setRight(helperRemove(curr.getRight(), data, dummy));
        } else {
            dummy.setData(curr.getData());
            this.size--;
            if (curr.getLeft() == null && curr.getRight() == null) {
                return null;
            } else if (curr.getRight() == null) {
                return curr.getLeft();
            } else if (curr.getLeft() == null) {
                return curr.getRight();
            } else {
                AVLNode<T> dummy2 = new AVLNode<>(null);
                curr.setRight(removeSuccessor(curr.getRight(), dummy2));
                curr.setData(dummy2.getData());
            }
        }
        curr = balance(curr);
        return curr;
    }

    private AVLNode<T> removeSuccessor(AVLNode<T> curr, AVLNode<T> dummy) {
        if (curr.getLeft() == null) {
            dummy.setData(curr.getData());
            return curr.getRight();
        }
        curr.setLeft(removeSuccessor(curr.getLeft(), dummy));
        curr = balance(curr);
        return curr;
    }

    private void updateHeightAndBF(AVLNode<T> node) {
      int leftHeight;
	    if (node.getLeft() == null) { 
		    leftHeight = -1;
	    } else { 
		    leftHeight = node.getLeft().getHeight();
	    }
	
	    int rightHeight;
	    if (node.getRight() == null) {
		    rightHeight = -1;
	    } else {
		    rightHeight = node.getRight().getHeight();
	    }
        
	    int currentHeight = Math.max(leftHeight, rightHeight) + 1;
	    node.setHeight(currentHeight);

	    int currentBF = leftHeight - rightHeight;
	    node.setBalanceFactor(currentBF);
    }

    private AVLNode<T> rotateLeft(AVLNode<T> currentNode) {
      T temp = currentNode.getData();
      AVLNode<T> rightChild = currentNode.getRight();
	    currentNode.setRight(rightChild.getLeft());
	    rightChild.setLeft(currentNode);
	    updateHeightAndBF(currentNode);
	    updateHeightAndBF(rightChild);
	    return rightChild;
    }

    private AVLNode<T> rotateRight(AVLNode<T> currentNode) {
      T temp = currentNode.getData();
	    AVLNode<T> leftChild = currentNode.getLeft();
	    currentNode.setLeft(leftChild.getRight());
	    leftChild.setRight(currentNode);
	    updateHeightAndBF(currentNode);
	    updateHeightAndBF(leftChild);
	    return leftChild;
    }

    private AVLNode<T> balance(AVLNode<T> currentNode) {
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

    public AVLNode<T> getRoot() {
        return root;
    }

    public int size() {
        return size;
    }
}
