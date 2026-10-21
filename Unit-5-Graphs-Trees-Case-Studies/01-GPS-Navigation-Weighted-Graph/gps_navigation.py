import heapq
from collections import deque


class CityGraph:
    def __init__(self):
        self.graph = {}

    def add_location(self, location):
        if location not in self.graph:
            self.graph[location] = []

    def add_road(self, source, destination, distance):
        self.add_location(source)
        self.add_location(destination)

        self.graph[source].append((destination, distance))
        self.graph[destination].append((source, distance))

    def display(self):
        print("\n--- City Map ---")
        for location, roads in self.graph.items():
            print(f"{location}: ", end="")
            if not roads:
                print("No roads")
                continue

            for destination, distance in roads:
                print(f"{destination}({distance} km)", end=" -> ")
            print("None")

    # Breadth First Search
    def bfs(self, start):
        if start not in self.graph:
            return []

        visited = set()
        queue = deque([start])
        order = []

        while queue:
            current = queue.popleft()

            if current in visited:
                continue

            visited.add(current)
            order.append(current)

            for neighbor, _ in self.graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

        return order

    # Depth First Search
    def dfs(self, start):
        if start not in self.graph:
            return []

        visited = set()
        order = []

        def visit(current):
            visited.add(current)
            order.append(current)

            for neighbor, _ in self.graph[current]:
                if neighbor not in visited:
                    visit(neighbor)

        visit(start)
        return order

    # Dijkstra's shortest path algorithm
    def dijkstra(self, start):
        if start not in self.graph:
            return {}, {}

        distances = {vertex: float("inf") for vertex in self.graph}
        previous = {vertex: None for vertex in self.graph}
        distances[start] = 0

        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current = heapq.heappop(priority_queue)

            if current_distance > distances[current]:
                continue

            for neighbor, weight in self.graph[current]:
                new_distance = current_distance + weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current
                    heapq.heappush(
                        priority_queue, (new_distance, neighbor)
                    )

        return distances, previous

    def shortest_path(self, source, destination):
        distances, previous = self.dijkstra(source)

        if destination not in distances:
            return [], float("inf")

        if distances[destination] == float("inf"):
            return [], float("inf")

        path = []
        current = destination

        while current is not None:
            path.append(current)
            current = previous[current]

        path.reverse()
        return path, distances[destination]

    # Prim's Minimum Spanning Tree
    def prim_mst(self):
        if not self.graph:
            return [], 0

        start = next(iter(self.graph))
        visited = {start}
        edges = []
        mst = []
        total = 0

        for destination, weight in self.graph[start]:
            heapq.heappush(edges, (weight, start, destination))

        while edges and len(visited) < len(self.graph):
            weight, source, destination = heapq.heappop(edges)

            if destination in visited:
                continue

            visited.add(destination)
            mst.append((source, destination, weight))
            total += weight

            for neighbor, neighbor_weight in self.graph[destination]:
                if neighbor not in visited:
                    heapq.heappush(
                        edges,
                        (neighbor_weight, destination, neighbor)
                    )

        if len(visited) != len(self.graph):
            return [], 0

        return mst, total

    # Kruskal's Minimum Spanning Tree
    def kruskal_mst(self):
        parent = {vertex: vertex for vertex in self.graph}
        rank = {vertex: 0 for vertex in self.graph}

        edges = []
        seen = set()

        for source in self.graph:
            for destination, weight in self.graph[source]:
                edge_id = tuple(sorted((source, destination)))

                if edge_id not in seen:
                    seen.add(edge_id)
                    edges.append((weight, source, destination))

        edges.sort()
        mst = []
        total = 0

        def find(vertex):
            while parent[vertex] != vertex:
                parent[vertex] = parent[parent[vertex]]
                vertex = parent[vertex]
            return vertex

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False

            if rank[root_a] < rank[root_b]:
                parent[root_a] = root_b
            elif rank[root_a] > rank[root_b]:
                parent[root_b] = root_a
            else:
                parent[root_b] = root_a
                rank[root_a] += 1

            return True

        for weight, source, destination in edges:
            if union(source, destination):
                mst.append((source, destination, weight))
                total += weight

                if len(mst) == len(self.graph) - 1:
                    break

        if len(mst) != len(self.graph) - 1:
            return [], 0

        return mst, total


def build_sample_city():
    city = CityGraph()

    roads = [
        ("College", "Station", 4),
        ("College", "Hospital", 7),
        ("Station", "Market", 3),
        ("Station", "Mall", 6),
        ("Market", "Mall", 2),
        ("Market", "Hospital", 5),
        ("Mall", "Airport", 8),
        ("Hospital", "Airport", 10),
        ("Hospital", "Bus Stand", 4),
        ("Bus Stand", "Airport", 5),
    ]

    for source, destination, distance in roads:
        city.add_road(source, destination, distance)

    return city


def print_mst(title, mst, total):
    print(f"\n--- {title} ---")

    if not mst:
        print("MST cannot be formed. The graph may be disconnected.")
        return

    for source, destination, weight in mst:
        print(f"{source} -- {destination} : {weight} km")

    print(f"Total weight: {total} km")


def main():
    city = build_sample_city()

    while True:
        print("\n===== GPS / Navigation System =====")
        print("1. Display City Map")
        print("2. BFS Traversal")
        print("3. DFS Traversal")
        print("4. Shortest Path (Dijkstra)")
        print("5. Minimum Spanning Tree (Prim)")
        print("6. Minimum Spanning Tree (Kruskal)")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            city.display()

        elif choice == "2":
            start = input("Enter starting location: ").strip()
            print("BFS:", " -> ".join(city.bfs(start)))

        elif choice == "3":
            start = input("Enter starting location: ").strip()
            print("DFS:", " -> ".join(city.dfs(start)))

        elif choice == "4":
            source = input("Enter source: ").strip()
            destination = input("Enter destination: ").strip()

            path, distance = city.shortest_path(source, destination)

            if path:
                print("Shortest path:", " -> ".join(path))
                print(f"Distance: {distance} km")
            else:
                print("Path not found.")

        elif choice == "5":
            mst, total = city.prim_mst()
            print_mst("Prim's MST", mst, total)

        elif choice == "6":
            mst, total = city.kruskal_mst()
            print_mst("Kruskal's MST", mst, total)

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
