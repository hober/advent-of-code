#!/usr/bin/env python3

import fileinput

class CPU:
    def __init__(self):
        self.x = 1

    def run(self, args):
        cycle = 0
        for line in fileinput.input(args):
            cycle += 1
            yield (cycle, self.x)
            if line[0:4] == 'addx':
                cycle += 1
                yield (cycle, self.x)
                self.x += int(line[5:-1])

if __name__ == '__main__':
    pass

