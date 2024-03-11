import java.util.NoSuchElementException;

public class BST<T extends Comparable<? super T>> {

    private BSTNode<T> root;
    private int size;

    public void add(T data) {
        if (data == null) {
            throw new IllegalArgumentException("Data is null!");
        }
        if (root == null) {
            root = new BSTNode<>(data);
            size++;
        } else {
            addHelper(data, root);
        }
    }

    private void addHelper(T data, BSTNode<T> curr) {
        if (data.compareTo(curr.getData()) > 0) {
            if (curr.getRight() == null) {
                curr.setRight(new BSTNode<>(data));
                size++;
            } else {
                addHelper(data, curr.getRight());
            }
        }
        else if (data.compareTo(curr.getData()) < 0) {
            if (curr.getLeft() == null) {
                curr.setLeft(new BSTNode<>(data));
                size++;
            } else {
                addHelper(data, curr.getLeft());
            }
        }
    }

    public T remove(T data) {
        if (data == null) {
            throw new IllegalArgumentException("Data is null!");
        }
        BSTNode<T> removed = new BSTNode<>(null);
        root = removeHelper(data, root, removed);
        return removed.getData();
    }

    private BSTNode<T> removeHelper(T data, BSTNode<T> curr, BSTNode<T> removed) {
        if (curr == null) {
            throw new NoSuchElementException("Data is not found.");
        } else {
            if (data.compareTo(curr.getData()) > 0) {
                curr.setRight(removeHelper(data, curr.getRight(), removed));
            } else if (data.compareTo(curr.getData()) < 0) {
                curr.setLeft(removeHelper(data, curr.getLeft(), removed));
            } else {
                removed.setData(curr.getData());
                size--;
                if (curr.getRight() == null) {
                    return curr.getLeft();
                } else if (curr.getLeft() == null) {
                    return curr.getRight();
                } else {
                    BSTNode<T> child = new BSTNode<>(null);
                    curr.setRight(successorHelper(curr.getRight(), child));
                    curr.setData(child.getData());
                }
            }
        }
        return curr;
    }

    private BSTNode<T> successorHelper(BSTNode<T> curr, BSTNode<T> child) {
        if (curr.getLeft() == null) {
            child.setData(curr.getData());
            return curr.getRight();
        }
        curr.setLeft(successorHelper(curr.getLeft(), child));
        return curr;
    }
    
    public BSTNode<T> getRoot() {
        return root;
    }

    public int size() {
        return size;
    }
}
