# SHORTEST-MAPPING-PLATFORM-Dijkstra-s-Algorithm
SHORTEST MAPPING PLATFORM  project is a Python-based navigation system that uses Dijkstra's algorithm to find the shortest path between two locations on a CIT College map, with a user-friendly text-based interface and map visualization.

The project appears to be a Python implementation of a navigation system or pathfinding algorithm using Dijkstra's algorithm to find the shortest path between two locations in a given map. Here are some key points about this project:

Graph Representation: The project uses a graph data structure to represent locations (nodes) and distances between them (edges).

Dijkstra's Algorithm: It implements Dijkstra's algorithm, a widely-used algorithm in graph theory and network routing, to find the shortest path between two points on the map.

File Input: The map data is read from a file named "distance.txt," which contains information about locations, their connections, and distances.

User Interface: The program provides a simple text-based user interface where users can input their source and destination locations.

Map Visualization: The program visually represents the map using a grid-like structure with labels for various locations, making it easier for users to select their source and destination.

Path Output: Once the shortest path is computed, it is displayed to the user along with the total distance.

Node and Edge Addition: The Graph class includes methods to add nodes (locations) and edges (connections between locations) to build the graph.

Priority Queue: Dijkstra's algorithm relies on a priority queue (implemented using Python's heapq module) to efficiently explore nodes with the lowest accumulated distance.

Data Parsing: The load_data function reads and parses the map data from the file, extracting information about locations, connections, and distances.

Modularity: The project is well-structured with separate functions and classes for different functionalities (e.g., loading data, finding paths), making it easy to maintain and extend.
