import java.util.HashSet;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Set;

public class GraphAlgorithms {
  public static <T> Set<Edge<T>> prims(Vertex<T> start, Graph<T> graph) {
    Set<Vertex<T>> VS = new HashSet<Vertex<T>>();
    Set<Edge<T>> MST = new HashSet<Edge<T>>();
    PriorityQueue<Edge<T>> PQ = new PriorityQueue<Edge<T>>();

    for (VertexDistance<T> vDist : graph.getAdjList().get(start)) {
      Vertex<T> vertex = vDist.getVertex();
      int weight = vDist.getDistance();
      PQ.add(new Edge<T>(start, vertex, weight));
    }

    VS.add(start);
    while ((!PQ.isEmpty()) && (VS.size() < graph.getAdjList().size())) {
      Edge<T> edge = PQ.remove();
      if (!VS.contains(edge.getV())) {
        VS.add(edge.getV());
        MST.add(edge);
        MST.add(new Edge<>(edge.getV(), edge.getU(), edge.getWeight()));

        for (VertexDistance<T> vDist : graph.getAdjList().get(edge.getV())) {
          Vertex<T> vertex = vDist.getVertex();
          int weight = vDist.getDistance();
          if (!VS.contains(vertex)) {
            PQ.add(new Edge<T>(edge.getV(), vertex, weight));
          }
        }
      }
    }
    if (VS.size() < graph.getVertices().size()) {
      return null;
    }
    return MST;
  }
}
