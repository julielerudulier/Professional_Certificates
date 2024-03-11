import java.util.Comparator;
import java.util.List;
import java.util.LinkedList;
import java.util.Queue;

public class Sorting {

  public static <T> void mergeSort(T[] arr, Comparator<T> comparator) {
    if (arr.length < 2) {
      return;
    }
    int length = arr.length;
    int midIndex = arr.length / 2;
    T[] left = sliceArray(arr, 0, midIndex);
    T[] right = sliceArray(arr, midIndex, length);
    mergeSort(left, comparator);
    mergeSort(right, comparator);
    int i = 0;
    int j = 0;
    while (i < left.length && j < right.length) {
      if (comparator.compare(left[i], right[j]) <= 0) {
        arr[i + j] = left[i];
        i++;
      } else {
        arr[i + j] = right[j];
        j++;
      }
    }
    while (i < left.length) {
      arr[i + j] = left[i];
      i++;
    }
    while (j < right.length) {
      arr[i + j] = right[j];
      j++;
    }
  }

  private static <T> T[] sliceArray(T[] arr, int start, int end) {
    T[] result = (T[]) new Object[end - start];
    for (int i = 0; i < end - start; i++) {
      result[i] = arr[i + start];
    }
    return result;
  }
  
  public static void lsdRadixSort(int[] arr) {
    LinkedList<Integer>[] buckets = new LinkedList[19];
    for (int i = 0; i < buckets.length; i++) {
      buckets[i] = new LinkedList<Integer>();
    }
    int k = -1;
    for (int i = 0; i < arr.length; i++) {
      if (String.valueOf(arr[i]).length() > k) {
        if (Character.toString(String.valueOf(arr[i]).charAt(0)) == "-") {
          k = String.valueOf(arr[i]).length() - 1;
        } else {
        k = String.valueOf(arr[i]).length();
        }
      }
    }
    for (int iteration = 0; iteration < k; iteration++) {
      for (int i = 0; i < arr.length; i++) {
        int digit;
        if (iteration == 9) {
          digit = arr[i] / pow(iteration);
        } else {
          digit = arr[i] % pow(iteration + 1) / pow(iteration);
        }
        buckets[digit + 9].add(arr[i]);
      }
      int idx = 0;
      for (LinkedList<Integer> bucket : buckets) {
        while (bucket.size() != 0) {
          arr[idx] = bucket.remove();
          idx++;
        }
      }
    }
  }

  private static int pow(int n) {
    int result = 1;
    for (int i = 0; i < n; i++) {
      result *= 10;
    }
    return result;
  }

}
