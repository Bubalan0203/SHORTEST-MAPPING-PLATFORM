import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = []

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append((to_node, distance))
        self.edges[to_node].append((from_node, distance))

    def dijkstra(self, start, end):
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0
        previous_nodes = {}

        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.edges[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        path = []
        current_node = end
        while current_node != start:
            path.insert(0, current_node)
            current_node = previous_nodes[current_node]
        path.insert(0, start)

        return path, distances[end]

def load_data(filename):
    graph = Graph()

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            source = parts[0].split(": ")[1]
            destination = parts[1].split(": ")[1]
            distance = int(parts[2].split(": ")[1])

            graph.add_node(source)
            graph.add_node(destination)
            graph.add_edge(source, destination, distance)

    return graph

def main():
    filename = "distance.txt"
    graph = load_data(filename)
    print('||==========================================================================================||')
    print('||                    MAP = COIMBATORE INSTITUTE OF TECHNOLOGY                              ||')
    print('||                                                                                          ||')
    print('||==========================================================================================||')
    print('||          [1]  ENTERENCE-1                                           [2] ENTERENCE-2      ||')
    print('||==========================================================================================||')
    print('||               ||   ||                 ||                                ||    ||         ||')
    print('||      [3]      ||   ||      [4]        ||       ||=============||        ||    ||         ||')
    print('||     BIKE      ||   ||      CAR        ||       ||             ||        ||    ||         ||')
    print('||    PARKING    ||   ||    PARKING      ||       || AUDITORIUM  ||        ||    ||         ||')
    print('||               ||   ||                 ||       ||    [5]      ||        ||    ||         ||')
    print('||               ||   ||                 ||       ||             ||        ||    ||         ||')
    print('||===============||   ||=================||       ||=============||        ||    ||=========||')
    print('||                                                                                          ||')
    print('||===============||   ||===============================================||                   ||')
    print('||               ||   ||                                               ||                   ||')
    print('||               ||   ||                                               ||                   ||')
    print('||     [6]       ||   ||                     [7]                       ||                   ||')
    print('||               ||   ||                                               ||                   ||')
    print('||     LAB       ||   ||      MAIN                   BLOCK             ||                   ||')
    print('||    BLOCK      ||   ||                                               ||                   ||')
    print('||               ||   ||                                               ||                   ||')
    print('||               ||   ||                                               ||                   ||')
    print('||               ||   ||                                               ||                   ||')
    print('||===============||   ||===============================================||                   ||')
    print('||                                                                                          ||')
    print('||===============||   ||==================||     ||====================||                   ||')
    print('||               ||   ||                  ||     ||                    ||                   ||')
    print('||      [8]      ||   ||        [9]       ||     ||      [10]          ||                   ||')
    print('||               ||   ||                  ||     ||                    ||                   ||')
    print('||      IT       ||   ||      LIBRARY     ||     ||       MSC          ||                   ||')
    print('||     BLOCK     ||   ||       BLOCK      ||     ||     BLOCK          ||                   ||')
    print('||               ||   ||                  ||     ||                    ||                   ||')
    print('||               ||   ||                  ||     ||                    ||                   ||')
    print('||               ||   ||                  ||     ||                    ||                   ||')
    print('||               ||   ||                  ||     ||                    ||                   ||')
    print('||===============||   ||==================||     ||====================||                   ||')
    print('||                                                                                          ||')
    print('||                                                                                          ||')
    print('||          ||============||        ||================================================||    ||')
    print('||          ||            ||        ||                                                ||    ||')
    print('||          ||     [11]   ||        ||                                                ||    ||')
    print('||          ||            ||        ||                                                ||    ||')
    print('||          ||  TEMPLE    ||        ||                                                ||    ||')
    print('||          ||            ||        ||                        [12]                    ||    ||')
    print('||          ||============||        ||========||                                      ||    ||')
    print('||                                            ||                                      ||    ||')
    print('||                                            ||                                      ||    ||')
    print('||==============||       ||=========||        ||                                      ||    ||')
    print('||              ||       ||   [14]  ||        ||                                      ||    ||')
    print('||     C        ||       ||         ||        ||                                      ||    ||')
    print('||     A        ||       ||    F    ||        ||                                      ||    ||')
    print('||     N        ||       ||    O    ||        ||               MAIN                   ||    ||')
    print('||     T        ||       ||    O    ||        ||                                      ||    ||')
    print('||     E        ||       ||    D    ||        ||                                      ||    ||')
    print('||     E        ||       ||         ||        ||              GROUND                  ||    ||')
    print('||     N        ||       ||    S    ||        ||                                      ||    ||')
    print('||              ||       ||    T    ||        ||                                      ||    ||')
    print('||              ||       ||    R    ||        ||                                      ||    ||')
    print('||    [13]      ||       ||    E    ||        ||                                      ||    ||')
    print('||              ||       ||    E    ||        ||                                      ||    ||')
    print('||              ||       ||    T    ||        ||                                      ||    ||')
    print('||==============||       ||=========||        ||                                      ||    ||')
    print('||                                            ||                                      ||    ||')
    print('||                                            ||                                      ||    ||')
    print('||                                ||============                                      ||    ||')
    print('||===============||               ||                                                  ||    ||')
    print('||    [15]       ||               ||                                                  ||    ||')
    print('||               ||               ||                                                  ||    ||')
    print('||  STUDENT      ||               ||                                                  ||    ||')
    print('||       STORE   ||               ||                                                  ||    ||')
    print('||               ||               ||                                                  ||    ||')
    print('||===============||               ||                                                  ||    ||')
    print('||                                ||==================================================||    ||')
    print('||                                                                                          ||')
    print('||                                                                                          ||')
    print('||===========================||        ||===================================================||')
    print('||                           ||        ||                                                   ||')
    print('||                           ||        ||                                                   ||')
    print('||         [16]              ||        ||                      [17]                         ||')
    print('||                           ||        ||                                                   ||')
    print('||                           ||        ||                                                   ||')
    print('||                           ||        ||                                                   ||')
    print('||  GIRLS                    ||        ||       BOYS                       HOSTEL           ||')
    print('||                           ||        ||                                                   ||')
    print('||              HOSTEL       ||        ||                                                   ||')
    print('||                           ||        ||                                                   ||')
    print('||                           ||        ||                                                   ||')
    print('||===========================||        ||===================================================||')
    print('||                                                                                          ||')
    print('||==========================================================================================||')
    print('||      [01] ENTERENCE-1            [02] ENTERENCE-2             [03] BIKE PARKING          ||')
    print('||      [04] CAR PARKING            [05] AUDITORIUM              [06] LAB BLOCK             ||')
    print('||      [07] MAIN BLOCK             [08] IT BLOCK                [09] LIBRARY BLOCK         ||')
    print('||      [10] MSC BLOCK              [11] TEMPLE                  [12] MAIN GROUND           ||')
    print('||      [13] CANTEEN                [14] FOOD STORE              [15] STUDENT STORE         ||')
    print('||      [16] GIRLS HOSTEL           [17] BOYS HOSTEL                                        ||')
    print('||                                                                                          ||')
    print('||==========================================================================================||')

    source = input('||                           Enter the source location:                                     ||\n')
    destination = input('||                      Enter the destination location:                                    ||\n')

    path, distance = graph.dijkstra(source, destination)
    print('||==========================================================================================||')
    print(f'                      Shortest path from {source} to {destination}:')
    print('||==========================================================================================||')
    print("\n || \n || \n \/\n".join(path))
    print('======================================')
    print(f"Total distance: {distance} Meters")
    print('======================================')

if __name__ == "__main__":
    main()