
# greedy and 2-opt

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

    for tour in all:
        search.append(tour)

    for tour in search :
        score = sum(distance(cities[tour[i]], cities[tour[(i+1) % length]]) for i in range(length)) # if i = length - 1, tour[i+1] = tour[length] ← out of index
                                                                                                    # and the last index should be connected with the first one → tour[0]
        # if we found better way, update best_score and best_tour.
        if score < best_score:
            best_score = score
            best_tour = tour

    print(best_score)
    return  best_tour


def calculate_score(tour, cities):
    length = len(tour)
    score = 0
    for i in range(length):
        city1 = cities[tour[i]]
        city2 = cities[tour[(i + 1) % length]]
        score += distance(city1, city2)
    return score


def two_opt(tour, cities):
    length = len(tour)
    improved = True
    while improved: 
        improved = False
        for i in range(length - 2):
            for j in range(i + 2, length):
                way1 = distance(cities[tour[i]], cities[tour[i + 1]]) + distance(cities[tour[j]], cities[tour[(j + 1) % length]])
                way2 = distance(cities[tour[i]], cities[tour[j]]) + distance(cities[tour[i + 1]], cities[tour[(j + 1) % length]])
                if way1 > way2:
                    tour[i + 1:j + 1] = reversed(tour[i + 1:j + 1])
                    improved = True
    best_score = calculate_score(tour,cities)
    print(best_score)
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
            next_city = min(unvisited_cities, key=lambda city: dist[current_city][city])
            unvisited_cities.remove(next_city)
            tour.append(next_city)
            current_city = next_city

        tour = two_opt(tour, cities)
    return tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    index = sys.argv[1][6]
    file_name = "output_" + index + ".csv"
    write_output(file_name, tour)