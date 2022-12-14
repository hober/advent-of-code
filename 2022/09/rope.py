#!/usr/bin/env python3

import fileinput

class PointSet:
    def __init__(self):
        self.points = set()

    def add(self, point):
        self.points.add(tuple(point))

    def count(self):
        return len(self.points)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        yield self.x
        yield self.y

class Rope:
    def __init__(self, n_knots):
        self.tailPositions = PointSet()
        self.knots = []
        tail = None
        for i in range(n_knots):
            tail = Point(0, 0)
            self.knots.append(tail)
        self.tailPositions.add(tail)

    def get_head(self):
        return self.knots[0]
    head = property(get_head)

    def get_tail(self):
        return self.knots[-1]
    tail = property(get_tail)

    def move(self, direction):
        if direction == 'U':
            self.head.y += 1
        elif direction == 'D':
            self.head.y -= 1
        elif direction == 'L':
            self.head.x -= 1
        elif direction == 'R':
            self.head.x += 1

        for k in range(1, len(self.knots)):
            prev_knot = self.knots[k-1]
            this_knot = self.knots[k]
            dx = prev_knot.x - this_knot.x
            dy = prev_knot.y - this_knot.y
            if dx == -2:
                this_knot.x -= 1
                if dy < 0:
                    this_knot.y -= 1
                if dy > 0:
                    this_knot.y += 1
            elif dx == 2:
                this_knot.x += 1
                if dy < 0:
                    this_knot.y -= 1
                if dy > 0:
                    this_knot.y += 1
            elif dy == -2:
                this_knot.y -= 1
                if dx < 0:
                    this_knot.x -= 1
                if dx > 0:
                    this_knot.x += 1
            elif dy == 2:
                this_knot.y += 1
                if dx < 0:
                    this_knot.x -= 1
                if dx > 0:
                    this_knot.x += 1

    def numberOfTailPositions(self, args):
        for line in fileinput.input(args):
            direction = line[0]
            how_far = int(line[2:-1])
            for ignore in range(how_far):
                self.move(direction)
                self.tailPositions.add(self.tail)
        return self.tailPositions.count()

if __name__ == '__main__':
    pass

