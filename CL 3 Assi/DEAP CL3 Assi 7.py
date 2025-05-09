

# first install deap framework 
# pip install deap


import random
from deap import base, creator, tools, algorithms

# Step 1: Define Optimization Problem
creator.create("FitnessMax", base.Fitness, weights=(1.0,))  # Maximize function
creator.create("Individual", list, fitness=creator.FitnessMax)

# Step 2: Initialize Population
def generate_individual():
    return [random.uniform(-10, 10)]  # One random number between -10 and 10

toolbox = base.Toolbox()
toolbox.register("individual", tools.initIterate, creator.Individual, generate_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Step 3: Define Fitness Function
def fitness_function(individual):
    x = individual[0]
    return x**2,  # Squaring the number (goal: maximize)

toolbox.register("evaluate", fitness_function)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Step 4: Run Evolutionary Algorithm
def run_evolution():
    population = toolbox.population(n=10)  # Create initial population
    algorithms.eaSimple(population, toolbox, cxpb=0.5, mutpb=0.2, ngen=20, verbose=True)
    best_individual = tools.selBest(population, k=1)[0]
    print("\nBest Solution:", best_individual, "Fitness:", fitness_function(best_individual))

run_evolution()
