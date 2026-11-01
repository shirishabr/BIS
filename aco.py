import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Calculate distance between two points
def distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))


# Ant Colony Optimization
def ant_colony_optimization(points, n_ants, n_iterations, alpha, beta,
                            evaporation_rate, Q):

    n_points = len(points)
    pheromone = np.ones((n_points, n_points))

    best_path = None
    best_path_length = np.inf

    # Main iteration
    for iteration in range(n_iterations):

        paths = []
        path_lengths = []

        # Each ant finds a path
        for ant in range(n_ants):

            visited = [False] * n_points

            current_point = int(np.random.randint(n_points))
            visited[current_point] = True

            path = [current_point]
            path_length = 0

            while False in visited:

                unvisited = np.where(np.logical_not(visited))[0]
                probabilities = np.zeros(len(unvisited))

                for i, unvisited_point in enumerate(unvisited):

                    d = distance(
                        points[current_point],
                        points[unvisited_point]
                    )

                    d = max(d, 1e-10)

                    probabilities[i] = (
                        pheromone[current_point, unvisited_point] ** alpha
                        / d ** beta
                    )

                probabilities /= np.sum(probabilities)

                next_point = int(np.random.choice(unvisited, p=probabilities))

                path.append(next_point)

                path_length += distance(
                    points[current_point],
                    points[next_point]
                )

                visited[next_point] = True
                current_point = next_point

            # Return to starting point
            path_length += distance(
                points[path[-1]],
                points[path[0]]
            )

            paths.append(path)
            path_lengths.append(path_length)

            # Find best path
            if path_length < best_path_length:
                best_path = path.copy()
                best_path_length = path_length

        # Pheromone evaporation
        pheromone *= evaporation_rate

        # Pheromone update
        for path, path_length in zip(paths, path_lengths):

            for i in range(n_points - 1):
                pheromone[path[i], path[i + 1]] += Q / path_length

            pheromone[path[-1], path[0]] += Q / path_length

    # Convert all path values to normal integers
    best_path = [int(x) for x in best_path]

    # Display results
    print("\nFINAL RESULTS:")
    print("Best Path:", best_path)
    print("Best Path Length:", best_path_length)

    # Plot 3D graph
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(
        points[:, 0],
        points[:, 1],
        points[:, 2],
        c='r',
        marker='o'
    )

    # Draw best path
    for i in range(n_points - 1):

        ax.plot(
            [points[best_path[i], 0], points[best_path[i + 1], 0]],
            [points[best_path[i], 1], points[best_path[i + 1], 1]],
            [points[best_path[i], 2], points[best_path[i + 1], 2]],
            c='g',
            linestyle='-',
            linewidth=2,
            marker='o'
        )

    # Connect last point to first point
    ax.plot(
        [points[best_path[0], 0], points[best_path[-1], 0]],
        [points[best_path[0], 1], points[best_path[-1], 1]],
        [points[best_path[0], 2], points[best_path[-1], 2]],
        c='g',
        linestyle='-',
        linewidth=2,
        marker='o'
    )

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title('Ant Colony Optimization - Best Path')

    plt.show()


# Example usage
if __name__ == "__main__":

    points = np.random.rand(10, 3)

    ant_colony_optimization(
        points,
        n_ants=10,
        n_iterations=100,
        alpha=1,
        beta=1,
        evaporation_rate=0.5,
        Q=1
    )