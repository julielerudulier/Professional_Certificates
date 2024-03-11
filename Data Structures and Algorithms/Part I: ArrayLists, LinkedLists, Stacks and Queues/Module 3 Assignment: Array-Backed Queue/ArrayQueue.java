import java.util.NoSuchElementException;

public class ArrayQueue<T> {

    public static final int INITIAL_CAPACITY = 9;
    private T[] backingArray;
    private int front;
    private int size;

    public ArrayQueue() {
        backingArray = (T[]) new Object[INITIAL_CAPACITY];
    }

    public void enqueue(T data) {
        if (data == null) { throw new IllegalArgumentException("Data is null."); }
	if (size == backingArray.length) {
		T[] newArray = (T[]) new Object[backingArray.length * 2];
		for (int i = 0; i < backingArray.length; i++) {
			newArray[i] = backingArray[(front + i) % backingArray.length];
		}
		backingArray = newArray;
		front = 0;
	}
	int back = (front + size) % backingArray.length;
	backingArray[back] = data;
	size += 1;
    }
  
    public T dequeue() {
        if (size == 0) { throw new NoSuchElementException("The queue is currently empty."); }
	
	T data = backingArray[front];
        backingArray[front] = null;
        front = (front + 1) % backingArray.length;
        size -= 1;

        return data;
    }

    public T[] getBackingArray() {
        // DO NOT MODIFY THIS METHOD!
        return backingArray;
    }

    public int size() {
        // DO NOT MODIFY THIS METHOD!
        return size;
    }
}
