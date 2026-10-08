import random

N = int(input("Population size: "))
G = int(input("Maximum generations: "))

L = int(input("Chromosome length: "))

pop = [[random.randint(0, 1) for _ in range(L)] for _ in range(N)]

def fitness(x):
    return int(''.join(map(str, x)), 2) ** 2

for g in range(1, G + 1):

    # Dynamic rates from research paper
    pm = g / G
    pc = 1 - pm

    new_pop = []

    while len(new_pop) < N:

        # Selection
        p1 = max(random.sample(pop, 2), key=fitness)
        p2 = max(random.sample(pop, 2), key=fitness)

        # Crossover
        if random.random() < pc:
            point = random.randint(1, L - 1)
            c1 = p1[:point] + p2[point:]
            c2 = p2[:point] + p1[point:]
        else:
            c1, c2 = p1[:], p2[:]

        # Mutation
        for c in [c1, c2]:
            for i in range(L):
                if random.random() < pm:
                    c[i] = 1 - c[i]
            new_pop.append(c)

    pop = new_pop[:N]

best = max(pop, key=fitness)

print("Best Chromosome:", best)
print("Best Fitness:", fitness(best))