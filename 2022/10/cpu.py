#!/usr/bin/env python3

import fileinput

def run(args):
    x = 1
    cycle = 0
    for line in fileinput.input(args):
        cycle += 1
        yield (cycle, x)
        if line[0:4] == 'addx':
            cycle += 1
            yield (cycle, x)
            x += int(line[5:-1])
