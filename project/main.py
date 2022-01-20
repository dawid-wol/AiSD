from enum import Enum
from typing import Any, Optional, Dict, List


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int

    def __init__(self, data: Any, index: int):
        self.data = data
        self.index = index


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source: Vertex, destination: Vertex, weight: Optional[float]):
        self.source = source
        self.destination = destination
        self.weight = weight


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self, data):
        new_vertex = Vertex(data, 0)
        self.adjacencies = {new_vertex: []}

    def create_vertex(self, data: Any) -> Vertex:
        index = len(self.adjacencies)
        new_vertex = Vertex(data, index)
        self.adjacencies.update({new_vertex: []})
        return new_vertex

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        new_edge = Edge(source, destination, weight)
        (self.adjacencies[source]).append(new_edge)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        new_edge = Edge(source, destination, weight)
        (self.adjacencies[source]).append(new_edge)
        new_edge1 = Edge(destination, source, weight)
        (self.adjacencies[destination]).append(new_edge1)

    def add(self, edge, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge == 1:
            self.add_directed_edge(source, destination, weight)
        if edge == 2:
            self.add_undirected_edge(source, destination, weight)


def graph_p(g: Graph):
    a = list(g.adjacencies)
    b = list(g.adjacencies.values())
    for i in a:
        print(i.data, end=' = ')
        c = list(b[i.index])
        print("[", end=" ")
        for j in c:
            print(j.destination.data, end=" ")
        print("]", end=" ")
    print("")


def find_vector(value: Any, g: Graph):
    vertex = list(g.adjacencies)
    for i in vertex:
        if i.data == value:
            return i


def list_p(address: list):
    for i in address:
        print(i.data, end=" ")
    print("")


def path(g: Graph, cross_id: Any, vertex: Vertex) -> Optional[List[Vertex]]:
    list_items = list(g.adjacencies.values())
    list_vertex = list(g.adjacencies)
    vertex_l = []
    vertex_s = list_vertex.index(vertex)
    if cross_id == vertex:
        list_a = [vertex]
        return list_a
    else:
        for k in list_items[vertex_s]:
            v = path(g, cross_id, k.destination)
            if v is not None:
                vertex_l += v
                vertex_l.insert(0, vertex)
                return vertex_l
        return None


def dead_path(g: Graph, cross_id: Any) -> Optional[List[Vertex]]:
    cross = find_vector(cross_id, g)
    list_items = list(g.adjacencies.values())
    list_vertex = list(g.adjacencies)
    vertex_list_s = list_vertex.index(cross)
    list1 = [cross]
    for i in list_items[vertex_list_s]:
        v = path(g, cross, i.destination)
        if v is not None:
            list1 += v

        if len(list1) > 1:
            return list1
    return None


road = Graph(2)
road.create_vertex(4)
road.create_vertex(6)
road.create_vertex(8)
road.create_vertex(10)
vertex_list = list(road.adjacencies)
road.add(1, vertex_list[0], vertex_list[2])
road.add(1, vertex_list[2], vertex_list[3])
road.add(1, vertex_list[3], vertex_list[1])
road.add(1, vertex_list[1], vertex_list[4])
road.add(1, vertex_list[0], vertex_list[1])
road.add(1, vertex_list[3], vertex_list[0])
road.add(1, vertex_list[0], vertex_list[4])
s = dead_path(road, 2)

list_p(s)


road2 = Graph(1)
road2.create_vertex(3)
road2.create_vertex(5)
road2.create_vertex(7)
road2.create_vertex(9)
road2.create_vertex(11)
road2.create_vertex(13)
road2_vertex = list(road2.adjacencies)
road2.add(1, road2_vertex[2], road2_vertex[5])
road2.add(1, road2_vertex[0], road2_vertex[5])
road2.add(1, road2_vertex[0], road2_vertex[6])
road2.add(1, road2_vertex[6], road2_vertex[3])
road2.add(1, road2_vertex[3], road2_vertex[1])
road2.add(1, road2_vertex[4], road2_vertex[1])
road2.add(1, road2_vertex[4], road2_vertex[2])
road2.add(1, road2_vertex[6], road2_vertex[4])
road2.add(1, road2_vertex[2], road2_vertex[0])
path_road2 = dead_path(road2, 7)
print(path_road2)
p = dead_path(road2, 9)
list_p(p)

road3 = Graph(1)
road3.create_vertex(2)
road3.create_vertex(3)
road3.create_vertex(4)
road3.create_vertex(5)
abc = list(road3.adjacencies)
road3.add(1, abc[0], abc[1])
road3.add(1, abc[1], abc[3])
road3.add(1, abc[3], abc[2])
road3.add(1, abc[2], abc[0])
road3.add(1, abc[2], abc[4])
road3.add(1, abc[1], abc[4])

road3_path = dead_path(road3, 5)
print(road3_path)
road3_path2 = dead_path(road3, 2)
list_p(road3_path2)
