#!/usr/bin/env python3

import collections, heapq

Infinity = float('infinity')

Vertex = collections.namedtuple('Vertex', ('r', 'c'))

def codepoint(character):
    return character.encode("utf-8")[0]

class Graph:
    def __init__(self, short_circuit=lambda v: False):
        self.n_rows = 0
        self.n_cols = 0
        self.heights = dict()
        self.neighbors = dict()
        self.distances = dict()
        self.start = None
        self.end = None
        self.short_circuit = short_circuit

    def compute(self):
        cycle = 0
        pq = [(0, self.start)]
        while len(pq) > 0:
            cycle += 1
            d, v = heapq.heappop(pq)

            if d > self.distances[v]:
                continue

            if self.short_circuit(v):
                self.end = v
                break

            for neighbor in self.neighbors[v]:
                if d+1 < self.distances[neighbor]:
                    self.distances[neighbor] = d+1
                    heapq.heappush(pq, (d+1, neighbor))

if __name__ == '__main__':
    pass
