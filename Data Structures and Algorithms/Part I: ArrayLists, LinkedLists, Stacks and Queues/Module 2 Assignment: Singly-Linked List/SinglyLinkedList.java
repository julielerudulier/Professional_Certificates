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
	
    public SinglyLinkedListNode<T> getHead() {
        return head;
    }

    public SinglyLinkedListNode<T> getTail() {
        return tail;
    }

    public int size() {
        return size;
    }
}
