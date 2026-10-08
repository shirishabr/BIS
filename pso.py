import random

N = int(input("Number of particles: "))
I = int(input("Number of iterations: "))
c1 = float(input("c1: "))
c2 = float(input("c2: "))

particles = [random.uniform(-10, 10) for _ in range(N)]
velocity = [random.uniform(-1, 1) for _ in range(N)]

def fitness(x):
    return x * x

pbest = particles[:]
gbest = min(particles, key=fitness)

for i in range(I):

    for j in range(N):

        r1 = random.random()
        r2 = random.random()

        velocity[j] = (velocity[j]
                       + c1 * r1 * (pbest[j] - particles[j])
                       + c2 * r2 * (gbest - particles[j]))

        particles[j] = particles[j] + velocity[j]

        if fitness(particles[j]) < fitness(pbest[j]):
            pbest[j] = particles[j]

    gbest = min(pbest, key=fitness)

print("Best Solution:", gbest)
print("Best Fitness:", fitness(gbest))