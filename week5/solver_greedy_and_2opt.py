#!/usr/bin/env python3

import sys
import math
import itertools

from common import print_tour, read_input, write_output


def distance(city1, city2):
    x = city1[0] - city2[0]
    y = city1[1] - city2[1]
    return math.sqrt(x ** 2 + y ** 2)


#if the data is less than 10, calcurate all patterns and get the best way.
def search_all(cities):
    length = len(cities)
    all = itertools.permutations(range(length))
    search = []
    best_score = float('inf')

    # We don't have to search all (we have to focus on the way which start at one cities. )
    for tour in all:
        if tour[0] == 1:
            search.append(tour)
    # we get (1, 7, 5, 2, 6, 3, 4, 0), (1, 7, 5, 2, 6, 4, 0, 3), (1, 7, 5, 2, 6, 4, 3, 0), (1, 7, 5, 3, 0, 2, 4, 6),,,,

    for tour in search :
        score = sum(distance(cities[tour[i]], cities[tour[(i+1) % length]]) for i in range(length)) # if i = length - 1, tour[i+1] = tour[length] ← out of index
                                                                                                    # and the last index should be connected with the first one → tour[0]
        # if we found better way, update best_score and best_tour.
        if score < best_score:
            best_score = score
            best_tour = tour

    return  best_tour


# if crossed, reconnect.
#      < way1 >                          < way2 >
#  --→ tour[i]     tour[j]  ←---      ---→ tour[i]  --- tour[j] →------
#                ×             |                                  　   |
#  ←-- tour[j+1]　　tour[i+1] --       ←--- tour[j+1] --- tour[i+1] ←---　　
#
def two_opt(tour, dist): # O(N^2)
    length = len(tour)
    while True:
        count = 0
        # try all patterns (i is always smaller than j)
        for i in range(length-2):
            for j in range(i+2, length):
                way1 = dist[tour[i]][tour[i + 1]] + dist[tour[j]][tour[(j + 1) % length]]
                way2 = dist[tour[i]][tour[j]] + dist[tour[i + 1]][tour[(j + 1) % length]]
                if way1 > way2:
                    new_tour = tour[i+1 : j+1] # the part that should be in reverse order
                    tour[i+1 : j+1] = new_tour[::-1] # replace the part
                    count += 1
        if count == 0:
            break
    return tour


def solve(cities):
    N = len(cities)
    
    # Initialize the list of dist (N*N)
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    tour = [current_city]

    if N < 10:
        tour = search_all(cities)
    else:
    # greedy
        while unvisited_cities:
            next_city = min(unvisited_cities,
                            key=lambda city: dist[current_city][city])
            unvisited_cities.remove(next_city)
            tour.append(next_city)
            current_city = next_city
    # two_opt
        tour = two_opt(tour, dist)
    return tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
    index = sys.argv[1][6]
    file_name = "output_" + index + ".csv"
    write_output(file_name,tour)
