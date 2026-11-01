import numpy as np


# Initialize wolves randomly
def initialize_wolves(search_space, num_wolves):

    dimensions = len(search_space)

    wolves = np.zeros((num_wolves, dimensions))

    for i in range(num_wolves):
        wolves[i] = np.random.uniform(
            search_space[:, 0],
            search_space[:, 1]
        )

    return wolves


# Fitness function (minimize)
def fitness_function(x):

    return np.sum(x ** 2)


# Grey Wolf Optimizer algorithm
def gwo_algorithm(search_space, num_wolves, max_iterations):

    dimensions = len(search_space)

    # Initialize wolves
    wolves = initialize_wolves(search_space, num_wolves)

    alpha_wolf = np.zeros(dimensions)
    beta_wolf = np.zeros(dimensions)
    gamma_wolf = np.zeros(dimensions)

    alpha_score = float("inf")
    beta_score = float("inf")
    gamma_score = float("inf")

    # Main optimization loop
    for iteration in range(max_iterations):

        # Calculate parameter a
        a = 2 - (iteration / max_iterations) * 2

        # Find alpha, beta and gamma wolves
        for i in range(num_wolves):

            fitness = fitness_function(wolves[i])

            if fitness < alpha_score:

                gamma_score = beta_score
                gamma_wolf = beta_wolf.copy()

                beta_score = alpha_score
                beta_wolf = alpha_wolf.copy()

                alpha_score = fitness
                alpha_wolf = wolves[i].copy()

            elif fitness < beta_score:

                gamma_score = beta_score
                gamma_wolf = beta_wolf.copy()

                beta_score = fitness
                beta_wolf = wolves[i].copy()

            elif fitness < gamma_score:

                gamma_score = fitness
                gamma_wolf = wolves[i].copy()

        # Update wolf positions
        for i in range(num_wolves):

            for j in range(dimensions):

                # Alpha wolf
                r1 = np.random.random()
                r2 = np.random.random()

                A1 = 2 * a * r1 - a
                C1 = 2 * r2

                D_alpha = abs(
                    C1 * alpha_wolf[j] - wolves[i, j]
                )

                X1 = alpha_wolf[j] - A1 * D_alpha

                # Beta wolf
                r1 = np.random.random()
                r2 = np.random.random()

                A2 = 2 * a * r1 - a
                C2 = 2 * r2

                D_beta = abs(
                    C2 * beta_wolf[j] - wolves[i, j]
                )

                X2 = beta_wolf[j] - A2 * D_beta

                # Gamma wolf
                r1 = np.random.random()
                r2 = np.random.random()

                A3 = 2 * a * r1 - a
                C3 = 2 * r2

                D_gamma = abs(
                    C3 * gamma_wolf[j] - wolves[i, j]
                )

                X3 = gamma_wolf[j] - A3 * D_gamma

                # Update position
                wolves[i, j] = (X1 + X2 + X3) / 3

                # Apply search space boundaries
                wolves[i, j] = np.clip(
                    wolves[i, j],
                    search_space[j, 0],
                    search_space[j, 1]
                )

    return alpha_wolf, alpha_score


# Example usage
if __name__ == "__main__":

    search_space = np.array([
        [-5, 5],
        [-5, 5]
    ])

    num_wolves = 10
    max_iterations = 100

    # Run GWO algorithm
    optimal_solution, best_fitness = gwo_algorithm(
        search_space,
        num_wolves,
        max_iterations
    )

    # Display results
    print("Optimal Solution:", optimal_solution)
    print("Best Fitness:", best_fitness)