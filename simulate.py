#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'Tomasz Lichon'

from sys import *
import random

n = int(argv[1])
collision_type = argv[2]
m = int(argv[3])
good_percentage = float(argv[4])
steps = int(argv[5])

class Board:
    def __init__(self, energy):
        self.map = {}
        self.energy = energy

    def add(self, individual):
        field = self.map.get(individual.pos, [])
        self.map[individual.pos] = field + [individual]


class Individual(object):
    def __init__(self, pos, energy):
        self.pos = pos
        self.energy = energy
        self.valid_moves = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    def alive(self):
        return self.energy > 0

    def move(self, n):
        while True:
            dx, dy = random.choice(self.valid_moves)
            x, y = self.pos
            if 0 <= x + dx < n and 0 <= y + dy < n:
                self.pos = x + dx, y + dy
                self.energy -= 1
                return self

    def add_energy(self, energy):
        self.energy += energy


class GoodIndividual(Individual):
    pass


class BadIndividual(Individual):
    pass


def fair_collision(individuals, energy):
    for ind in individuals:
        ind.energy += energy / len(individuals)


def bad_collision(individuals, energy):
    best = max(individuals, key=lambda ind: ind.energy)
    best.energy += energy


def very_bad_collision(individuals, energy):
    best = max(individuals, key=lambda ind: ind.energy)
    total_energy = sum([ind.energy for ind in individuals])
    best.energy = total_energy + energy


def altruistic_collision(individuals, energy):
    total_energy = sum([ind.energy for ind in individuals]) + energy
    for ind in individuals:
        ind.energy = float(total_energy) / len(individuals)


# definitions
energy = n*n
board = Board(energy)
collision_functions = {
    'fair_collision': lambda individuals, energy: fair_collision(individuals, energy),
    'bad_collision': lambda individuals, energy: bad_collision(individuals, energy),
    'very_bad_collision': lambda individuals, energy: very_bad_collision(individuals, energy),
    'altruistic_collision': lambda individuals, energy: altruistic_collision(individuals, energy)
}

# initial fill
initial_energy = board.energy / m
for i in range(int(m * good_percentage)):
    pos = random.randrange(0, n), random.randrange(0, n)
    board.add(GoodIndividual(pos, initial_energy))
for i in range(int(m * (1 - good_percentage))):
    pos = random.randrange(0, n), random.randrange(0, n)
    board.add(BadIndividual(pos, initial_energy))
board.energy = 0

# steps
for i in range(steps):
    # move
    moving = []
    for field in board.map.values():
        for individual in field:
            moving.append(individual.move(n))
    population = len(moving)
    board.map.clear()
    board.energy += population

    # remove dead
    moving = [ind for ind in moving if ind.alive()]
    alive = len(moving)
    good = len([ind for ind in moving if isinstance(ind, GoodIndividual)])
    bad = alive - good

    # add to board
    for individual in moving:
        board.add(individual)

    # handle collisions
    collisions = [field for field in board.map.values() if len(field) > 1]
    collisions_number = len(collisions)
    if collisions_number:
        collision_energy = float(board.energy) / collisions_number
        for collision in collisions:
            collision_fun = collision_functions[collision_type]
            collision_fun(collision, collision_energy)
        board.energy = 0

    print('{0} {1} {2} {3} {4} {5} {6} {7}'.format(n, m, collision_type, i, alive, good, bad, collisions_number))
