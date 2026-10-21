# GPS / Navigation System Using a Weighted Graph

## SPPU - Second Year Computer Engineering (2024 Pattern)
### PCC-201-COM: Data Structures
### Unit V - Graphs and Trees

## Case Study

A GPS/navigation system can model a city as a **weighted graph**.
Locations such as colleges, stations, hospitals, markets and airports
are represented as vertices. Roads connecting the locations are
represented as weighted edges, where the weight represents distance.

This implementation demonstrates core graph algorithms:

- Breadth First Search (BFS)
- Depth First Search (DFS)
- Dijkstra's shortest path algorithm
- Prim's Minimum Spanning Tree
- Kruskal's Minimum Spanning Tree

## Graph Representation

An adjacency list is used.

Example:

```text
College -> Station (4 km), Hospital (7 km)
Station -> College (4 km), Market (3 km), Mall (6 km)
```

## Algorithms

### BFS
Traverses the graph level by level using a queue.

### DFS
Traverses the graph depth-first using recursion.

### Dijkstra
Finds the shortest path between two locations when edge weights are
non-negative.

### Prim
Builds a Minimum Spanning Tree by repeatedly selecting the minimum
weight edge that connects a visited vertex to an unvisited vertex.

### Kruskal
Builds a Minimum Spanning Tree by sorting edges by weight and using
the Union-Find technique to avoid cycles.

## Complexity

| Algorithm | Complexity |
|---|---|
| BFS | O(V + E) |
| DFS | O(V + E) |
| Dijkstra (binary heap) | O((V + E) log V) |
| Prim (binary heap) | O((V + E) log V) |
| Kruskal | O(E log E) |

## How to Run

```bash
python gps_navigation.py
```

## Conclusion

The GPS case study shows how a real-world city map can be represented
using a weighted graph. Traversal algorithms can explore the map,
Dijkstra can find a shortest route, and Prim/Kruskal can construct a
minimum spanning tree.
