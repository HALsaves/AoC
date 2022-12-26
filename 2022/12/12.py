#!/usr/bin/env python3
"""Advent of Code"""
import csv
import sys
from pprint import pprint


def main():
    """MAIN"""
    ex_data = read_in_data("./ex")
    my_data = read_in_data("./in")

    # Part 1
    print("Example 1:")
    pprint(ex_data)
    elevations, graph = create_graph(ex_data)
    start_index = elevations.index(ord("a") - 1)
    end_index = elevations.index(ord("z") + 1)
    dijkstra = Graph(len(graph))
    dijkstra.graph = graph
    dijkstra.dijkstra(start_index, [end_index])
    # part1(ex_data)
    print("\nSolution 1:")
    elevations, graph = create_graph(my_data)
    start_index = elevations.index(ord("a") - 1)
    end_index = elevations.index(ord("z") + 1)
    dijkstra = Graph(len(graph))
    dijkstra.graph = graph
    dijkstra.dijkstra(start_index, [end_index])

    # Part 2
    print("\nExample 2:")
    elevations, graph = create_graph_reverse(ex_data)
    elevations = [ord("a") if i == ord("a") - 1 else i for i in elevations]  # make the 'S' point equal to one minus 'a'
    start_index = elevations.index(ord("z") + 1)
    end_indexes = [i for i in range(len(elevations)) if elevations[i] in (ord("a"), ord("a") - 1)]
    dijkstra = Graph(len(graph))
    dijkstra.graph = graph
    dijkstra.dijkstra(start_index, end_indexes)
    print("\nSolution 2:")
    elevations, graph = create_graph_reverse(my_data)
    start_index = elevations.index(ord("z") + 1)
    end_indexes = [i for i in range(len(elevations)) if elevations[i] in (ord("a"), ord("a") - 1)]
    dijkstra = Graph(len(graph))
    dijkstra.graph = graph
    dijkstra.dijkstra(start_index, end_indexes)


def create_graph(data):
    """create graph of distances from vertice to vertice"""
    cols = len(data[0])
    rows = len(data)
    elevations = [i for row in data for i in row]
    num_vertices = cols * rows
    graph = [[0 for column in range(num_vertices)] for row in range(num_vertices)]
    for vert in range(len(graph)):
        # up
        if vert - cols >= 0:
            graph[vert][vert - cols] = dist_forward(elevations[vert], elevations[vert - cols])
        # down
        if vert + cols <= len(graph) - 1:
            graph[vert][vert + cols] = dist_forward(elevations[vert], elevations[vert + cols])
        # left
        if vert % cols - 1 >= 0:
            graph[vert][vert - 1] = dist_forward(elevations[vert], elevations[vert - 1])
        # right
        if vert % cols + 1 <= cols - 1:
            graph[vert][vert + 1] = dist_forward(elevations[vert], elevations[vert + 1])
    return elevations, graph


def dist_forward(a, b):
    """distance calc"""
    if b - a <= 1:
        return 1
    return 999999


def create_graph_reverse(data):
    """create graph of distances from vertice to vertice"""
    cols = len(data[0])
    rows = len(data)
    elevations = [i for row in data for i in row]
    num_vertices = cols * rows
    graph = [[0 for column in range(num_vertices)] for row in range(num_vertices)]
    for vert in range(len(graph)):
        # up
        if vert - cols >= 0:
            graph[vert][vert - cols] = dist_reverse(elevations[vert], elevations[vert - cols])
        # down
        if vert + cols <= len(graph) - 1:
            graph[vert][vert + cols] = dist_reverse(elevations[vert], elevations[vert + cols])
        # left
        if vert % cols - 1 >= 0:
            graph[vert][vert - 1] = dist_reverse(elevations[vert], elevations[vert - 1])
        # right
        if vert % cols + 1 <= cols - 1:
            graph[vert][vert + 1] = dist_reverse(elevations[vert], elevations[vert + 1])
    return elevations, graph


def dist_reverse(a, b):
    """distance calc"""
    if b - a >= -1:
        return 1
    return 999999


def read_in_data(data_file):
    """Read in the data"""
    raw_data = []
    with open(data_file, encoding="utf-8", mode="r") as input_file:
        reader = csv.reader(input_file, delimiter=" ")
        for row in reader:
            ords = [ord(i) for i in list(row[0])]
            ords = [ord("a") - 1 if i == ord("S") else i for i in ords]  # make the 'S' point equal to one minus 'a'
            ords = [ord("z") + 1 if i == ord("E") else i for i in ords]  # make the start point equal to one minus 'a'
            raw_data.append(ords)
    final_data = alter_data(raw_data)
    return final_data


def alter_data(raw_data):
    """Alter the data to fit the problem"""
    final_data = raw_data
    return final_data


class Graph:
    """Dijkstra'a"""

    def __init__(self, vertices):
        """init"""
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def print_solution(self, dist, src, ends):
        """Dump shortest path"""
        print("Vertex \tDistance from Source", src)
        minimum = 99999
        minimum_i = 0
        for node in ends:
            # print(node, "\t", dist[node])
            if dist[node] < minimum:
                minimum = dist[node]
                minimum_i = node
        print(minimum_i, "\t", dist[minimum_i])

    def min_distance(self, dist, sptset):
        """min distance function"""
        minimum = sys.maxsize
        for i in range(self.vertices):
            if dist[i] < minimum and not sptset[i]:
                minimum = dist[i]
                minimum_index = i
        return minimum_index

    def dijkstra(self, src, end):
        """dijkstra"""
        dist = [sys.maxsize] * self.vertices
        dist[src] = 0
        sptset = [False] * self.vertices
        for _ in range(self.vertices):
            x = self.min_distance(dist, sptset)
            sptset[x] = True
            for y in range(self.vertices):
                if self.graph[x][y] > 0 and not sptset[y] and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
        self.print_solution(dist, src, end)


if __name__ == "__main__":
    main()
