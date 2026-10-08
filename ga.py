import random

# Get input from user
N = int(input("Enter population size (N): "))
p_m = float(input("Enter mutation rate (p_m): "))
p_c = float(input("Enter crossover rate (p_c): "))
G_max = int(input("Enter maximum generations (G_max): "))

CHROMOSOME_LENGTH = int(input("Enter chromosome length: "))


# Create a random chromosome
def create_chromosome():
    return [random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]


# Create initial population
def initialize_population():
    return [create_chromosome() for _ in range(N)]


# Convert binary chromosome to decimal
def decode(chromosome):
    return int("".join(map(str, chromosome)), 2)


# Fitness function
def fitness(chromosome):
    x = decode(chromosome)
    return x ** 2


# Select parent using tournament selection
def select_parent(population):
    parent1 = random.choice(population)
    parent2 = random.choice(population)

    if fitness(parent1) > fitness(parent2):
        return parent1
    else:
        return parent2


# Crossover
def crossover(parent1, parent2):

    if random.random() < p_c:

        point = random.randint(1, CHROMOSOME_LENGTH - 1)

        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]

        return child1, child2

    else:
        return parent1[:], parent2[:]


# Mutation
def mutate(chromosome):

    for i in range(CHROMOSOME_LENGTH):

        if random.random() < p_m:
            chromosome[i] = 1 - chromosome[i]

    return chromosome


# Genetic Algorithm
def genetic_algorithm():

    # Initialize population
    population = initialize_population()

    best_solution = None
    best_fitness = -1

    # Run generations
    for generation in range(G_max):

        # Evaluate fitness
        for chromosome in population:

            current_fitness = fitness(chromosome)

            if current_fitness > best_fitness:
                best_fitness = current_fitness
                best_solution = chromosome[:]

        # Create next generation
        next_population = []

        while len(next_population) < N:

            # Select two parents
            parent1 = select_parent(population)
            parent2 = select_parent(population)

            # Crossover
            child1, child2 = crossover(parent1, parent2)

            # Mutation
            child1 = mutate(child1)
            child2 = mutate(child2)

            # Add offspring
            next_population.append(child1)

            if len(next_population) < N:
                next_population.append(child2)

        # Replace old population
        population = next_population

    return best_solution, best_fitness


# Run Genetic Algorithm
best_solution, best_fitness = genetic_algorithm()


# Display result
print("\n===================================")
print("       GENETIC ALGORITHM RESULT")
print("===================================")
print("Best Chromosome :", best_solution)
print("Best Solution   :", decode(best_solution))
print("Best Fitness    :", best_fitness)