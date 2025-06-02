
# simulated_annealing and 2-opt

import sys
import math
import random
import itertools

from common import read_input, write_output


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
    print("2-opt:",best_score)
    return tour


def simulated_annealing(cities, initial_temperature, cooling_rate, num_iterations):
    N = len(cities)
    
    # Random initial solution
    current_tour = list(range(N))
    random.shuffle(current_tour)
    best_tour = current_tour[:]
    current_score = calculate_score(current_tour, cities)
    best_score = current_score
    
    temperature = initial_temperature

    for _ in range(num_iterations):
        next_tour = current_tour[:]
        
        # Generate a neighboring tour by performing a 2-opt swap (chose 2 points at random)
        i = random.randint(0, N - 1)
        j = random.randint(0, N - 1)
        # If we do not choose the same points
        if i != j:
            next_tour[min(i, j):max(i, j) + 1] = reversed(next_tour[min(i, j):max(i, j) + 1])

        next_score = calculate_score(next_tour, cities)
        
        # Decide whether to accept the neighboring tour as the new current tour
        # If the score is improved
        if next_score < current_score:
            current_tour = next_tour
            current_score = next_score
            if next_score < best_score:
                best_tour = next_tour
                best_score = next_score
        
        # If the score is not inproved
        # Update the current_tour and current_score even if it does not have better score.
        # By doing this, we can prevent falling into a local solution.
        else:
            probability = math.exp((current_score - next_score) / temperature)
            if random.random() < probability:
                current_tour = next_tour
                current_score = next_score
        
        # Update the temperature
        temperature *= cooling_rate
    print("simulated_annealing:", best_score)
    return best_tour


def solve(cities):
    N = len(cities)
    # Initialize the list of dist (N*N)
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    tour = [current_city]

    if N < 10:
        tour = search_all(cities)
    else:
        best_score = float('inf')
        best_tour = 0
        for i in range(100):
            tour = simulated_annealing(cities, initial_temperature=100000, cooling_rate=0.99, num_iterations=10000)
            score = calculate_score(tour, cities)
            if score < best_score:
                best_score = score
                best_tour = tour
        print("best in simulated_annealing:", best_score)
        tour = two_opt(best_tour, cities)
    return tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    index = sys.argv[1][6]
    file_name = "output_" + index + ".csv"
    write_output(file_name, tour)