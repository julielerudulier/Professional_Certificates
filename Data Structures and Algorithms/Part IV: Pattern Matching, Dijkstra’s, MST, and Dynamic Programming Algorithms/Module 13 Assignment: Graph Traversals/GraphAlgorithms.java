import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

public class GraphAlgorithms {
  public static <T> List<Vertex<T>> bfs(Vertex<T> start, Graph<T> graph) {
    List<Vertex<T>> result = new ArrayList<>();
	  Set<Vertex<T>> VS = new HashSet<>();
	  Queue<Vertex<T>> q = new ArrayDeque<>();
	  VS.add(start);
	  q.add(start);
	  while (q.isEmpty() == false) {
      Vertex<T> v = q.remove();
	    result.add(v);
	    for (VertexDistance<T> vDist : graph.getAdjList().get(v)) {
	      Vertex<T> w = vDist.getVertex();
	    	if (VS.contains(w) == false) {
	    	  VS.add(w);
	    		q.add(w);
	    	}
	    }
	  }
	  return result; 
  }
  
  public static <T> List<Vertex<T>> dfs(Vertex<T> start, Graph<T> graph) {
    List<Vertex<T>> list = new ArrayList<>();
    Set<Vertex<T>> VS = new HashSet<>();
    List<Vertex<T>> result = dfsHelper(start, graph, VS, list);
    return result;
  }

  private static <T> List<Vertex<T>> dfsHelper(Vertex<T> s, Graph<T> G, Set<Vertex<T>> VS, List<Vertex<T>> L){
    VS.add(s);
    L.add(s);
    for(VertexDistance<T> vDist : G.getAdjList().get(s)){
      Vertex<T> w = vDist.getVertex();
      if(VS.contains(w) == false){
        dfsHelper(w, G, VS, L);
      }
    }
    return L;
  }

}
