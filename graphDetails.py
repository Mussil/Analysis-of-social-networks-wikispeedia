import networkx as nx
import numpy as np
import collections

from createGraph import createGraph
from matplotlib import pyplot as plt
from readPaths import read_finished_path

def graphDegreeDistribution(g, name):
    degree_sequence = sorted([d for n, d in g.degree()])  # degree sequence
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())
    plt.bar(deg, cnt, width=0.80, color="#FF7D40")
    plt.title(f"Degree distribution in {name} graph")
    plt.ylabel("Frequency")
    plt.xlabel("Degrees")
    # plt.show()

def largestCC(g):
    number = nx.number_strongly_connected_components(g)
    print('number of connected components:', number)

    largest = max(nx.strongly_connected_components(g), key=len)
    print('number of egdes in greatest connected component:', len(largest))
    largestSubGraph = g.subgraph(largest)
    # print(largestSubGraph)
    return largestSubGraph


def calcClicksForEdge(g, n):

    edges_dict = {}
    for edge in g.edges:
        edges_dict[edge] = 0

    games = read_finished_path()
    for game in games:
        if '<' not in game and len(game) == n:
            for step in game:
                current_step = game.index(step)
                if current_step != len(game) - 1:
                    edge = (step, game[current_step + 1])
                    if edge in edges_dict.keys():
                        edges_dict[edge] += 1

    # print(edges_dict)

    edge_amount = {}
    for k, v in edges_dict.items():
        if v in edge_amount.keys():
            edge_amount[v] += 1
        else:
            edge_amount[v] = 1
    edge_amount = dict(sorted(edge_amount.items()))
    # print(edge_amount)

    keys = edge_amount.keys()
    vals = edge_amount.values()

    plt.bar(keys, vals, label="Edges amount clicks")

    plt.yscale("log")
    plt.xlabel('Amount of clicks')
    plt.ylabel('Number of edges')
    plt.xticks(list(keys))
    plt.legend(bbox_to_anchor=(1, 1), loc="upper right", borderaxespad=0.)

    # plt.show()
if __name__ == '__main__':
    g = createGraph()

    # degree distrebution calc
    graphDegreeDistribution(g, 'origional')

    # largest CC
    largestCcGraph = largestCC(g)
    graphDegreeDistribution(largestCcGraph, 'CC')

    calcClicksForEdge(g, 8)


