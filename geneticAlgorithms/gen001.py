import random

POPULATION_SIZE = 100
GENOME_LENGTH = 20
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.7
GENERATIONS = 200


def random_genome(length):
    return [random.randint(0, 1) for _ in range(length)]


def init_population(population_size, genome_length):
    return [random_genome(genome_length) for _ in range(population_size)]


def fitness(genome):
    return sum(genome)


def select_parent(population, fitness_values):
    total_fitness = sum(fitness_values)
    pick = random.uniform(0, total_fitness)
    current = 0
    for individual, fitness_value in zip(population, fitness_values):
        current += fitness_value
        if current > pick:
            return individual


def crossover(parent1, parent2):
    if random.random() < MUTATION_RATE:
        pass
    else:
        return parent1, parent2
