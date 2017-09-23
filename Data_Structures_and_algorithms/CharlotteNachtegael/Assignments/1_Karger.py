"""
INFO-F413 : Data Structures and Algorithms
Assignment 1 : Karger's Algorithm
Problem of the minimum cut (cutset subset of edges whose removal disconnects
the graph) based on the random contraction of an edge until two vertices left, the
set of edges left  is the ouput
This algorithm has a probability of success of 2/(n(n-1))
"""

from random import choice
from copy import deepcopy
from math import log


def make_graph(file):
    """
    Create a dictionary from the data file
    :param file: string of the name of the data file
    :return: dictionary with vertex as key and a set of the vertices they are connected to as values
    """
    dico = {}
    with open(file, 'r') as data:
        for line in data:
            line = line.strip().split(' ')
            dico[line[0]] = line[1:]
    return dico


def contract(vertex1, vertex2, graph):
    """
    Contraction of an edge
    :param vertex1: string of the vertex 1
    :param vertex2: string of the vertex 2
    :param graph: dictionary with the vertices as keys and the list of the vertices they are connected to as values
    :return: dictionary of the graph with the vertices 1 and 2 combined
    """

    new_edge_vertex = graph[vertex1] + graph[vertex2]

    # remove the edge between vertex 1 and 2
    while vertex1 in new_edge_vertex:
        new_edge_vertex.remove(vertex1)
    while vertex2 in new_edge_vertex:
        new_edge_vertex.remove(vertex2)

    # remove the vertex 2, update the content to only have the vertex 1, combination of vertex 1 and 2
    del graph[vertex2]
    graph[vertex1] = new_edge_vertex
    for vertex in graph:
        edges = graph[vertex]
        while vertex2 in edges:
            edges.remove(vertex2)
            edges.append(vertex1)

    return graph


def minimum_cut(graph):
    """
    Look for the minimum cutset by contracting randomly two vertices of the graph until only two vertices are left
    :param graph: dictionary with vertices as keys and list of neighbours as values
    :return: integer of number of edges to cut to disconnect the graph
    """

    while len(graph) > 2:
        vertices = list(graph.keys())
        vertex1 = choice(vertices)
        vertex2 = choice(graph[vertex1])
        graph = contract(vertex1, vertex2, graph)

    return len(graph.popitem()[1])


def summary(results, n, runs):
    """
    Print the summary of the results
    :param results: list of the results obtained with the different runs of the karger's algorithms
    :param n: size of the graph
    :param runs: number of runs done
    """
    final = min(results)
    print('The minimal cut is of %s edges' % final)
    right = 0
    for res in results:
        if res == final:
            right += 1

    observed_success = right/runs
    lower_bound = 2/(n*(n-1))

    if observed_success >= lower_bound:
        print('The lower bound of the probability of success is respected !\n'
              'Observed success frequency = %s\n'
              'Lower bound probability of success = %s\n' % (observed_success, lower_bound))


def main():
    """
    Run several times the Karger's algorithm for a graph
    """

    file = str(input('Name of the file with the vertex and their neighbours : '))
    graph = make_graph(file)
    n = len(graph)
    res = []
    run = n*(n-1)*log(n)
    i = 0

    while i < run:
        working = deepcopy(graph)
        res.append(minimum_cut(working))
        i += 1

    summary(res, n, i)

if __name__ == "__main__":
    main()
