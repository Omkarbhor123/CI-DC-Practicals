import random

# Step 1: Define an objective function (maximize)
def objective_function(x):
    return -((x - 3) ** 2) + 10  # Peak at x=3

# Step 2: Initialize population
def initialize_population(size):
    return [random.uniform(0, 6) for _ in range(size)]  # Random values

# Step 3: Clone best candidates
def clone_population(population, num_clones):
    return [x for x in population for _ in range(num_clones)]  # Clone each solution

# Step 4: Apply mutation
def mutate_population(clones, mutation_rate):
    return [x + random.uniform(-0.5, 0.5) if random.random() < mutation_rate else x for x in clones]

# Step 5: Select best solutions
def select_best(population, size):
    return sorted(population, key=objective_function, reverse=True)[:size]

# Step 6: Run Clonal Selection Algorithm
def clonal_selection_algorithm(pop_size=10, generations=10, num_clones=3, mutation_rate=0.3):
    population = initialize_population(pop_size)

    for gen in range(generations):
        clones = clone_population(population, num_clones)
        mutated_clones = mutate_population(clones, mutation_rate)
        population = select_best(mutated_clones, pop_size)
        best_solution = population[0]
        print(f"Generation {gen+1}: Best Solution = {best_solution:.4f}")

    return best_solution

# Run the algorithm
best_solution = clonal_selection_algorithm()
print(f"\nOptimal Solution Found: x = {best_solution:.4f}")
