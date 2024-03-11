import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class PatternMatching {
  public static List<Integer> boyerMoore(CharSequence pattern, CharSequence text, CharacterComparator comparator) {
    ArrayList<Integer> result = new ArrayList<>();
    Map<Character, Integer> last = buildLastTable(pattern);
    int i = 0;
    int m = pattern.length();
    int n = text.length();
    while (i <= (n - m)) {
      int j = m - 1;
	      while (j >= 0 && comparator.compare(text.charAt(i + j), pattern.charAt(j)) == 0) {
	    	  j--;
	    	}
	    	if (j == -1) {
	    		result.add(i);
	    		i++;
	    	} else {
	    		int shift = last.getOrDefault(text.charAt(i + j), -1);
	    		if (shift < j) {
	    			i = i + j - shift;
	    		} else {
	    			i++;
	    		}
   	    }
    }
	  return result;
  }
  
  public static Map<Character, Integer> buildLastTable(CharSequence pattern) {
    int m = pattern.length();
    HashMap<Character, Integer> last = new HashMap<>();
    for (int i = 0; i < m; i++){
      last.put(pattern.charAt(i), i);
    }
    return last;
    }
}
