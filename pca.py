
import numpy as np
import matplotlib.pyplot as plt

# 1. Define the optimization function
def fitness(x):
    return np.sum(x ** 2)

# 2. Initialize parameters
num_cells = 25
grid_size = 5
iterations = 100
dimensions = 2

# 3. Initialize population randomly
population = np.random.uniform(
    -10, 10, (num_cells, dimensions)
)

# Store best solution
best_solution = None
best_fitness = float('inf')

# Store convergence values
convergence = []

# 4. Evaluate initial fitness
for i in range(num_cells):
    value = fitness(population[i])

    if value < best_fitness:
        best_fitness = value
        best_solution = population[i].copy()

# 5. Iterate PCA
for iteration in range(iterations):

    new_population = population.copy()

    for i in range(num_cells):

        # Find neighboring cells in a ring
        left = (i - 1) % num_cells
        right = (i + 1) % num_cells

        # Select the best neighbor
        neighbors = [
            population[i],
            population[left],
            population[right]
        ]

        neighbor_fitness = [
            fitness(n) for n in neighbors
        ]

        best_neighbor = neighbors[
            np.argmin(neighbor_fitness)
        ]

        # Update cell position
        new_population[i] = (
            population[i]
            + np.random.rand(dimensions)
            * (best_neighbor - population[i])
            + np.random.uniform(-0.1, 0.1, dimensions)
        )

        # Keep values within search space
        new_population[i] = np.clip(
            new_population[i], -10, 10
        )

    # Update population
    population = new_population

    # Evaluate fitness
    for i in range(num_cells):
        value = fitness(population[i])

        if value < best_fitness:
            best_fitness = value
            best_solution = population[i].copy()

    # Record convergence
    convergence.append(best_fitness)

# 6. Display best solution
print("Best Solution:", best_solution)
print("Best Fitness:", best_fitness)

# 7. Plot convergence graph
plt.plot(
    range(1, iterations + 1),
    convergence,
    color='blue',
    linewidth=2
)

plt.title("PCA Convergence Graph")
plt.xlabel("Iterations")
plt.ylabel("Best Fitness Value")
plt.grid(True)
plt.show()
