import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;

public class Traversals<T extends Comparable<? super T>> {

    public List<T> preorder(TreeNode<T> root) {
        List<T> preorderList = new ArrayList<>();
        preorderHelper(root, preorderList);
        return preorderList;
    }

    private void preorderHelper(TreeNode<T> node, List<T> list) {
        if (node != null) {
            list.add(node.getData());
            preorderHelper(node.getLeft(), list);
            preorderHelper(node.getRight(), list);
        }
    }

    public List<T> inorder(TreeNode<T> root) {
	    List<T> inorderList = new ArrayList<>();
	    inorderHelper(root, inorderList);
	    return inorderList;
    }

    private void inorderHelper(TreeNode<T> node, List<T> list) {
	    if (node != null) {
            inorderHelper(node.getLeft(), list);
		    list.add(node.getData());
		    inorderHelper(node.getRight(), list);
	    }
    }

    public List<T> postorder(TreeNode<T> root) {
        List<T> postorderList = new ArrayList<>();
	    postorderHelper(root, postorderList);
	    return postorderList;
    }
	
    private void postorderHelper(TreeNode<T> node, List<T> list) {
	    if (node != null) {
		    postorderHelper(node.getLeft(), list);
		    postorderHelper(node.getRight(), list);
		    list.add(node.getData());
	    }
    }    
}

