#!/usr/bin/env python3

import fileinput

class Forest:
    def __init__(self, trees):
        self.trees = trees
        self.n_rows = len(self.trees)
        self.n_cols = len(self.trees[0])

def parse(args):
    rows = []
    for line in fileinput.input(args):
        line = line[0:-1]
        rows.append([int(c) for c in line])
    return Forest(rows)
