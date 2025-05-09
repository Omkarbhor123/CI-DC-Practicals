import numpy as np
import tensorflow as tf
import random

# Define the Neural Network Structure
def create_nn(num_neurons, learning_rate):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(num_neurons, activation='relu', input_shape=(5,)),  # 5 input features
        tf.keras.layers.Dense(1, activation='linear')  # Output layer
    ])
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate), loss='mse')
    return model

# Genetic Algorithm Parameters
POPULATION_SIZE = 10
MUTATION_RATE = 0.2
CROSSOVER_RATE = 0.7
GENERATIONS = 5

# Initialize population
population = [{'num_neurons': random.randint(5, 50), 'learning_rate': random.uniform(0.001, 0.01)} for _ in range(POPULATION_SIZE)]

# Sample dataset (simulating spray drying parameters)
X_train = np.random.rand(100, 5)  # 100 samples, 5 features
y_train = np.random.rand(100, 1)  # Target output

# Fitness function (evaluates model performance)
def fitness(individual):
    model = create_nn(individual['num_neurons'], individual['learning_rate'])
    model.fit(X_train, y_train, epochs=5, verbose=0)
    return model.evaluate(X_train, y_train, verbose=0)  # Lower loss is better

# Evolution process
for gen in range(GENERATIONS):
    print(f"Generation {gen+1}")
    
    # Evaluate fitness for each individual
    scores = [(fitness(ind), ind) for ind in population]
    scores.sort(key=lambda x: x[0])  # Sort by loss (lower is better)
    
    # Selection - keep top 50% of the population
    population = [ind for _, ind in scores[:POPULATION_SIZE//2]]
    
    # Crossover - create new offspring
    offspring = []
    while len(offspring) < POPULATION_SIZE//2:
        p1, p2 = random.sample(population, 2)
        child = {'num_neurons': int((p1['num_neurons'] + p2['num_neurons']) / 2),
                 'learning_rate': (p1['learning_rate'] + p2['learning_rate']) / 2}
        offspring.append(child)
    
    # Mutation - introduce small changes
    for child in offspring:
        if random.random() < MUTATION_RATE:
            child['num_neurons'] += random.randint(-5, 5)
            child['learning_rate'] += random.uniform(-0.001, 0.001)

    population.extend(offspring)  # Add offspring to the new population

# Best Model Found
best_model_params = population[0]
print(f"\nOptimized Parameters: Neurons = {best_model_params['num_neurons']}, Learning Rate = {best_model_params['learning_rate']}")
