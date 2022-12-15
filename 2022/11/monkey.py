#!/usr/bin/env python3

import fileinput, math

class Operation:
    def __init__(self, expr):
        self.expr = expr[6:]
        (self.lhs, op, self.rhs) = self.expr.split()
        if self.lhs != 'old':
            self.lhs = int(self.lhs)
        if self.rhs != 'old':
            self.rhs = int(self.rhs)
        if op == '+':
            self.op = lambda x, y: x + y
        elif op == '*':
            self.op = lambda x, y: x * y

    def __call__(self, old):
        lhs = self.lhs
        rhs = self.rhs
        if self.lhs == 'old':
            lhs = old
        if self.rhs == 'old':
            rhs = old
        return self.op(lhs,rhs)

class Monkey:
    def __init__(self, label):
        self.label = label
        self.things = []
        self.operation = None
        self.test = None
        self.if_true = None
        self.if_false = None
        self.count = 0

    def take(self, thing):
        self.things.append(thing)

class KeepAway:
    def __init__(self, n_rounds, divisor):
        self.troop = dict()
        self.n_rounds = n_rounds
        self.bound = 1
        self.divisor = divisor

    def play(self, args):
        # Prepare to play

        monkey = None
        for line in fileinput.input(args):
            if line[:-1] == '':
                pass
            elif line[0] == 'M': # Monkey
                k = int(line[7:-2])
                monkey = Monkey(k)
                self.troop[k] = monkey
            elif line[2] == 'S': # Starting things
                monkey.things = [int(n) for n in line[18:-1].split(", ")]
            elif line[2] == 'O': # Operation
                monkey.operation = Operation(line[13:-1])
            elif line[2] == 'T': # Test
                monkey.test = int(line[21:-1])
                self.bound = self.bound * monkey.test
            elif line[7] == 't': # If true
                monkey.if_true = int(line[29:-1])
            elif line[7] == 'f': # If false
                monkey.if_false = int(line[30:-1])

        # Play the game

        for turn in range(self.n_rounds):
            for k, monkey in self.troop.items():
                things = monkey.things
                monkey.things = []
                for thing in things:
                    monkey.count += 1
                    worry = math.floor(monkey.operation(thing) / self.divisor) % self.bound
                    if worry % monkey.test == 0:
                        self.troop[monkey.if_true].take(worry)
                    else:
                        self.troop[monkey.if_false].take(worry)

        # Scoring

        ultimate = 0
        penultimate = 0

        for k, monkey in self.troop.items():
            if monkey.count >= penultimate:
                penultimate = monkey.count
            if monkey.count >= ultimate:
                penultimate = ultimate
                ultimate = monkey.count

        print(ultimate * penultimate)

if __name__ == '__main__':
    pass

