
import random
import matplotlib.pyplot as plt

# 1. Define fitness function
def fitness(x, y):
    return x**2 + y**2

# 2. Initialize parameters
population_size = 20
num_genes = 2
mutation_rate = 0.1
crossover_rate = 0.8
generations = 100

# 3. Initialize population
population = [
    [random.uniform(-10, 10) for _ in range(num_genes)]
    for _ in range(population_size)
]

# Store best solution
best_solution = None
best_fitness = float('inf')
convergence = []

# 4. Gene expression and fitness evaluation
for generation in range(generations):

    # Evaluate fitness
    scores = [
        fitness(chromosome[0], chromosome[1])
        for chromosome in population
    ]

    # Find best chromosome
    for i in range(population_size):
        if scores[i] < best_fitness:
            best_fitness = scores[i]
            best_solution = population[i][:]

    convergence.append(best_fitness)

    # 5. Selection (Tournament Selection)
    new_population = []

    while len(new_population) < population_size:

        # Select two parents
        candidates1 = random.sample(range(population_size), 3)
        candidates2 = random.sample(range(population_size), 3)

        parent1 = min(candidates1, key=lambda i: scores[i])
        parent2 = min(candidates2, key=lambda i: scores[i])

        p1 = population[parent1][:]
        p2 = population[parent2][:]

        # 6. Crossover
        if random.random() < crossover_rate:
            point = random.randint(1, num_genes - 1)

            child1 = p1[:point] + p2[point:]
            child2 = p2[:point] + p1[point:]
        else:
            child1 = p1[:]
            child2 = p2[:]

        # 7. Mutation
        for child in [child1, child2]:
            for j in range(num_genes):
                if random.random() < mutation_rate:
                    child[j] = random.uniform(-10, 10)

            # Keep genes within limits
            child[:] = [
                max(-10, min(10, gene))
                for gene in child
            ]

            # 8. Add offspring
            new_population.append(child)

            if len(new_population) >= population_size:
                break

    # Update population
    population = new_population

# 9. Display best solution
print("Best Genetic Sequence:", best_solution)
print("Best Solution:", best_solution)
print("Best Fitness:", best_fitness)
print("Total Generations:", generations)

# 10. Plot convergence graph
plt.plot(
    range(1, generations + 1),
    convergence,
    color='blue',
    linewidth=2
)

plt.title("GEA Convergence Graph")
plt.xlabel("Generations")
plt.ylabel("Best Fitness Value")
plt.grid(True)
plt.show()
