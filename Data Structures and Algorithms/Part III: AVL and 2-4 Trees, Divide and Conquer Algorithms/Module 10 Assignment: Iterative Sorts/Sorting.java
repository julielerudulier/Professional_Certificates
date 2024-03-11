import java.util.Comparator;

public class Sorting {
	public static <T> void bubbleSort(T[] arr, Comparator<T> comparator) {
    		int stopIndex = arr.length - 1;
	  	while (stopIndex != 0) {
			int i = 0;
		  	int lastSwapped = 0;
	    		while (i < stopIndex) {
		    		if (comparator.compare(arr[i], arr[i + 1]) > 0) {
			    		swap(arr, i, i+1);
				  	lastSwapped = i;
	    			}
		    		i++;
	    		}
	    		stopIndex = lastSwapped;
    		}
  	}
	
	public static <T> void selectionSort(T[] arr, Comparator<T> comparator) {
   		for (int n = arr.length - 1; n > 0; n--) {
			int maxIdx = n;
	    		for (int i = 0; i < n; i++) {
    	  			if (comparator.compare(arr[i], arr[maxIdx]) > 0) {
	    	  			maxIdx = i;
		    		}
    			}
	    		swap(arr, n, maxIdx);
    		}
  	}

	public static <T> void insertionSort(T[] arr, Comparator<T> comparator) {
    		for (int n = 1; n < arr.length; n++) {
	    		int i = n;
	    		while ((i != 0) && (comparator.compare(arr[i], arr[i-1]) < 0)) {
	      			swap(arr, i, i-1);
	    			i--;
	    		}
	  	} 
  	}
    
  	private static <T> void swap(T[] arr, int index1, int index2) {
		T temp = arr[index1];
  		arr[index1] = arr[index2];
  		arr[index2] = temp;
  	}

}
