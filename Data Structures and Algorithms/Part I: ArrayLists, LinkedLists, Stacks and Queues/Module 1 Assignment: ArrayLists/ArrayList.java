import java.util.NoSuchElementException;

public class ArrayList<T> {
	public static final int INITIAL_CAPACITY = 9;
	private T[] backingArray;
    	private int size;
	public ArrayList() {
		backingArray = (T[]) new Object[INITIAL_CAPACITY];
	}
	
	public void addToFront(T data) {
		if (data == null) {
			throw new IllegalArgumentException("No data.");
		} 
		if (size < backingArray.length) {
			for (int i = size - 1; i >= 0; i--) {
				backingArray[i+1] = backingArray[i];
			}		
			backingArray[0] = data;
			size += 1; 
		} else if (size == backingArray.length) {
			T[] newArray = (T[]) new Object[backingArray.length * 2];
			for (int i = 0; i < backingArray.length; i++) {
				newArray[i+1] = backingArray[i];
			}
			newArray[0] = data;
			backingArray = newArray;
			size += 1;
		}
	}

	public void addToBack(T data) {
		if (data == null) {
			throw new IllegalArgumentException("No data.");
		} 
		if (size < backingArray.length) {
			backingArray[size] = data;
			size += 1; 	
		} else if (size == backingArray.length) {
			T[] newArray = (T[]) new Object[backingArray.length * 2];
			for (int i = 0; i < backingArray.length; i++) {
				newArray[i] = backingArray[i];
			}
			newArray[size] = data;
			size += 1;
			backingArray = newArray;
		}
	}
	
	public T removeFromFront() {
		if (size == 0) {
			throw new NoSuchElementException("The list is currently empty.");
		} 
		T data = backingArray[0];
		for (int i = 0; i < size-1; i++) {
			backingArray[i] = backingArray[i+1];
		}
		backingArray[size-1] = null;
		size -= 1;
		return data;
	}
   
	public T removeFromBack() {
		if (size == 0) {
			throw new NoSuchElementException("The list is currently empty.");
		}
		T data = backingArray[size-1];
		backingArray[size-1] = null;
		size -= 1;
		return data;
	}

    	public T[] getBackingArray() {
        	return backingArray;
    	}

    	public int size() {
        	return size;
    	}
}
