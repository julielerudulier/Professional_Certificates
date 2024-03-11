import java.util.NoSuchElementException;

public class MinHeap<T extends Comparable<? super T>> {

    public static final int INITIAL_CAPACITY = 13;

    private T[] backingArray;
    private int size;

    public MinHeap() {
        backingArray = (T[]) new Comparable[INITIAL_CAPACITY];
    }

    public void add(T data) {
        if (data == null) { throw new IllegalArgumentException(); }
        if (size == backingArray.length - 1) {
            resizeBackingArray(backingArray.length * 2);
        }
        size++;
        backingArray[size] = data;
        heapifyUp(size);
    }

    public T remove() {
        if (size == 0) { throw new NoSuchElementException(); }
        T minItem = backingArray[1];        
        backingArray[1] = backingArray[size];
        backingArray[size] = null;
        size--;
        heapifyDown(1);
        return minItem;
    }

    public T[] getBackingArray() {
        // DO NOT MODIFY THIS METHOD!
        return backingArray;
    }

    public int size() {
        // DO NOT MODIFY THIS METHOD!
        return size;
    }
        
    private void resizeBackingArray(int newCapacity) {
        T[] newBackingArray = (T[]) new Comparable[newCapacity];
        for (int i = 1; i <= size; i++) {
            newBackingArray[i] = backingArray[i];
        }
        backingArray = newBackingArray;
    }
    
    private void heapifyUp(int index) {
        while (index > 1 && backingArray[index].compareTo(backingArray[index / 2]) < 0) {
            swap(index, index / 2);
            index /= 2;
        }
    }
    
    private void heapifyDown(int index) {
        while (index * 2 <= size) {
            int minChildIndex = getMinChildIndex(index);
            if (backingArray[index].compareTo(backingArray[minChildIndex]) > 0) {
                swap(index, minChildIndex);
                index = minChildIndex;
            } else {
                break;
            }
        }
    }
    
    private int getMinChildIndex(int index) {
        int leftChildIndex = index * 2;
        int rightChildIndex = index * 2 + 1;
        if (rightChildIndex <= size && backingArray[rightChildIndex].compareTo(backingArray[leftChildIndex]) < 0) {
            return rightChildIndex;
        } else {
            return leftChildIndex;
        }
    }
    
    private void swap(int index1, int index2) {
        T temp = backingArray[index1];
        backingArray[index1] = backingArray[index2];
        backingArray[index2] = temp;
    }
}
