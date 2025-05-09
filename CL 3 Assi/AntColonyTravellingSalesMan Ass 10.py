import numpy as np

# Distance matrix (4 cities)
distance_matrix = np.array([
    [0, 10, 12, 15],
    [10, 0, 8, 9],
    [12, 8, 0, 7],
    [15, 9, 7, 0]
])

# Number of cities and ants
num_cities = len(distance_matrix)
num_ants = 5
num_iterations = 50
evaporation_rate = 0.5
alpha = 1  # Pheromone influence
beta = 2  # Distance influence

# Initialize pheromone matrix
pheromones = np.ones((num_cities, num_cities))

# Initialize visibility (inverse distance)
visibility = 1 / (distance_matrix + 1e-10)  # Avoid division by zero

# Run ACO
for _ in range(num_iterations):
    paths = []
    distances = []

    for _ in range(num_ants):
        path = [np.random.randint(num_cities)]
        for _ in range(num_cities - 1):
            current_city = path[-1]
            probabilities = (pheromones[current_city] ** alpha) * (visibility[current_city] ** beta)
            probabilities[path] = 0  # Avoid revisiting cities
            next_city = np.argmax(probabilities)  # Choose next city with highest probability
            path.append(next_city)

        distance = sum(distance_matrix[path[i], path[i+1]] for i in range(num_cities - 1)) + distance_matrix[path[-1], path[0]]
        paths.append(path)
        distances.append(distance)

    # Update pheromones
    pheromones *= (1 - evaporation_rate)
    for i in range(len(paths)):
        for j in range(num_cities - 1):
            pheromones[paths[i][j], paths[i][j+1]] += 1 / distances[i]

# Get the best path and distance
best_path = paths[np.argmin(distances)]
best_distance = min(distances)

# Output result
print(f"Best Route: {[int(i) for i in best_path]}")
print(f"Shortest Distance: {best_distance}")
