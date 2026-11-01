import numpy as np
from multiprocessing import Pool, cpu_count
from scipy.optimize import differential_evolution


# Calculate predicted demand
def pred_eval_fun_P(x):
    return x[0]**2 + x[1]**2


# Calculate actual demand
def orig_eval_fun_P(x):
    return (x[0] - 2)**2 + (x[1] - 3)**2


# First inequality constraint: x[0] + x[1] <= 10
def eval_g_ineq1(x):
    return x[0] + x[1] - 10


# Second inequality constraint: x[0] >= 0
def eval_g_ineq2(x):
    return -x[0]


# Fitness function to maximize
def fitness_P(x):
    f = pred_eval_fun_P(x)

    penalty1 = 1000 * max(0, eval_g_ineq1(x))
    penalty2 = 1000 * max(0, eval_g_ineq2(x))

    return -f + penalty1 + penalty2


# Lower and upper bounds
lb = [0, 0]
ub = [10, 10]

bounds = list(zip(lb, ub))

# Optimization parameters
no_cores = max(1, cpu_count() - 1)
max_gen = 100

# Run optimization
if __name__ == "__main__":
    with Pool(processes=no_cores) as pool:
        result = differential_evolution(
            fitness_P,
            bounds,
            maxiter=max_gen,
            popsize=15,
            disp=True,
            workers=pool.map,
            updating="deferred",
            seed=42
        )

    final_reco = result.x

    print("\nOptimization completed successfully!")
    print("Optimal Solution:", final_reco)
    print("Maximum Fitness:", -result.fun)
    print("Success:", result.success)
    print("Message:", result.message)