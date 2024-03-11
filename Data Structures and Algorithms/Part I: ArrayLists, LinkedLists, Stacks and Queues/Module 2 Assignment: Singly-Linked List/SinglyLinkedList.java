import java.util.NoSuchElementException;

public class SinglyLinkedList<T> {

    private SinglyLinkedListNode<T> head;
    private SinglyLinkedListNode<T> tail;
    private int size;

    public void addToFront(T data) {
        if (data == null) { throw new IllegalArgumentException("no data"); }
	SinglyLinkedListNode<T> newNode = new SinglyLinkedListNode<>(data);
	if (size == 0) { 
		head = newNode; 
		tail = newNode;
	} else {
		newNode.setNext(head);
		head = newNode;
	}
	size += 1;		
    }

    public void addToBack(T data) {
        if (data == null) { throw new IllegalArgumentException("no data"); }
	SinglyLinkedListNode<T> newNode = new SinglyLinkedListNode<>(data);
	if (size == 0) {
		head = newNode;
		tail = newNode;
	} else {
		tail.setNext(newNode);
		tail = newNode;
	}
	size += 1;
    }

    public T removeFromFront() {
        if (size == 0) { throw new NoSuchElementException("The list is currently empty"); }
	T removedData = head.getData();
	if (size == 1) {
		head = null;
		tail = null;
	} else {
		head = head.getNext();
	}
	size -= 1;
	return removedData;
    }

    public T removeFromBack() {
        if (size == 0) { throw new NoSuchElementException("The list is currently empty"); }
	T removedData = tail.getData();
	if (size == 1) {
		head = null;
		tail = null;
	} else {
		SinglyLinkedListNode<T> currentNode = head;
		while (currentNode.getNext() != tail) {
			currentNode = currentNode.getNext();
		}
		currentNode.setNext(null);
		tail = currentNode;
	}
	size -= 1;
	return removedData;
    }

    /**
     * Returns the head node of the list.
     *
     * For grading purposes only. You shouldn't need to use this method since
     * you have direct access to the variable.
     *
     * @return the node at the head of the list
     */
    public SinglyLinkedListNode<T> getHead() {
        // DO NOT MODIFY THIS METHOD!
        return head;
    }

    /**
     * Returns the tail node of the list.
     *
     * For grading purposes only. You shouldn't need to use this method since
     * you have direct access to the variable.
     *
     * @return the node at the tail of the list
     */
    public SinglyLinkedListNode<T> getTail() {
        // DO NOT MODIFY THIS METHOD!
        return tail;
    }

    /**
     * Returns the size of the list.
     *
     * For grading purposes only. You shouldn't need to use this method since
     * you have direct access to the variable.
     *
     * @return the size of the list
     */
    public int size() {
        // DO NOT MODIFY THIS METHOD!
        return size;
    }
}
