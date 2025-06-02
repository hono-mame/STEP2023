/* greedy and 2-opt */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

struct City {
    double x;
    double y;
};

double distance(struct City city1, struct City city2) {
    double x = city1.x - city2.x;
    double y = city1.y - city2.y;
    return sqrt(x * x + y * y);
}

double calculate_score(int* tour, struct City* cities, int length) {
    double score = 0.0;
    for (int i = 0; i < length; i++) {
        int city1_index = tour[i];
        int city2_index = tour[(i + 1) % length];
        struct City city1 = cities[city1_index];
        struct City city2 = cities[city2_index];
        score += distance(city1, city2);
    }
    return score;
}

/* I could not finish writing this part :( , so the scores of input_0.csv and input_2.csv is 0. */
/* I couldn't come up with a way to find all the tours. */
int* search_all(struct City* cities, int length) {
    int n = 0;// number of tours
    int* best_tour = (int*)malloc(sizeof(int) * length);
    int* all_tour = (int*)malloc(sizeof(int) * length * n);
    double best_score = INFINITY;
    
    return best_tour;
}


void greedy(struct City* cities, double** dist, int length, int* tour) {
    int i, j;
    int current_city = 0;
    int* unvisited_cities = (int*)malloc(sizeof(int) * (length - 1));
    int unvisited_count = length - 1;

    for (i = 0; i < length - 1; i++) {
        unvisited_cities[i] = i + 1;
    }
    for (i = 0; i < length - 1; i++) {
        int next_city = unvisited_cities[0];
        double min_dist = dist[current_city][next_city];
        int min_index = 0;
        for (j = 1; j < unvisited_count; j++) {
            int city = unvisited_cities[j];
            double d = dist[current_city][city];
            if (d < min_dist) {
                next_city = city;
                min_dist = d;
                min_index = j;
            }
        }
        unvisited_cities[min_index] = unvisited_cities[unvisited_count - 1];
        unvisited_count--;
        tour[i] = next_city;
        current_city = next_city;
    }
    tour[length - 1] = 0;

    free(unvisited_cities);
}

void two_opt(int* tour, double** dist, int length) {
    int i, j, k;
    int count;
    while (1) {
        count = 0;
        for (i = 0; i < length - 2; i++) {
            for (j = i + 2; j < length; j++) {
                double way1 = dist[tour[i]][tour[i + 1]] + dist[tour[j]][tour[(j + 1) % length]];
                double way2 = dist[tour[i]][tour[j]] + dist[tour[i + 1]][tour[(j + 1) % length]];
                if (way1 > way2) {
                    int* new_tour = (int*)malloc(sizeof(int) * (j - i));
                    for (k = i + 1; k <= j; k++) {
                        new_tour[k - i - 1] = tour[k];
                    }
                    for (k = i + 1; k <= j; k++) {
                        tour[k] = new_tour[j - k];
                    }
                    free(new_tour);
                    count++;
                }
            }
        }
        if (count == 0) {
            break;
        }
    }
}

void solve(struct City* cities, int length, int* tour) {
    int i, j;

    double** dist = (double**)malloc(sizeof(double*) * length);
    for (i = 0; i < length; i++) {
    dist[i] = (double*)malloc(sizeof(double) * length);
    for (j = 0; j < length; j++) {
        dist[i][j] = distance(cities[i], cities[j]);
        }
    }

    greedy(cities, dist, length, tour);
    two_opt(tour, dist, length);

    for (i = 0; i < length; i++) {
        free(dist[i]);
    }
    free(dist);
}


int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("usage: %s [input_file]\n", argv[0]);
        return 1;
    }

    char* input_file = argv[1];
    FILE* fp = fopen(input_file, "r");
    if (fp == NULL) {
        printf("Failed to open an input file: %s\n", input_file);
        return 1;
    }

    // Skip the first line
    char line[256];
    fgets(line, sizeof(line), fp);

    int N = 0;
    struct City* cities = NULL;

    while (fgets(line, sizeof(line), fp) != NULL) {
        char* x_str = strtok(line, ",");
        char* y_str = strtok(NULL, ",");
        if (x_str != NULL && y_str != NULL) {
            double x = atof(x_str);
            double y = atof(y_str);
            cities = (struct City*)realloc(cities, sizeof(struct City) * (N + 1));
            cities[N].x = x;
            cities[N].y = y;
            N++;
        }
    }

    fclose(fp);

    int* tour = (int*)malloc(sizeof(int) * N);

    if (N < 10) {
    int* best_tour = search_all(cities, N);
    double score = calculate_score(best_tour, cities, N);
    printf("score: %f\n", score);
    free(best_tour); 
}
    else {
        solve(cities, N, tour);
        double score = calculate_score(tour,cities, N);
        printf("score: %f\n", score);
    }

    char index = input_file[strlen(input_file) - 5];
    char output_file[20];
    sprintf(output_file, "output_%c.csv", index);

    fp = fopen(output_file, "w");
    if (fp == NULL) {
        printf("Failed to open an output file: %s\n", output_file);
        free(cities);
        free(tour);
        return 1;
    }
    fprintf(fp, "index\n");
    for (int i = 0; i < N; i++) {
        fprintf(fp, "%d\n", tour[i]);
    }
    fclose(fp);

    free(cities);
    free(tour);

    return 0;
}