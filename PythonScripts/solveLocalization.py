import numpy as np
from scipy.optimize import minimize

def euclidean_distance(x, y):
    """Calculates the Euclidean distance between two points."""
    return np.sqrt(np.sum((x - y)**2))

def edmc_objective(x, known_distances, known_pairs, num_points):
    """Calculates the objective function for the EDMC problem."""
    x = x.reshape((num_points, 3))  # Reshape x into (num_points, 3) coordinates

    distances = np.zeros((num_points, num_points))
    for i in range(num_points):
        for j in range(i + 1, num_points):
            distances[i, j] = euclidean_distance(x[i], x[j])
            distances[j, i] = distances[i, j]

    objective = 0
    for pair, distance in zip(known_pairs, known_distances):
        if pair[0] < num_points and pair[1] < num_points:
            objective += (distances[pair[0], pair[1]] - distance) ** 2
        else:
            print(f"Warning: pair {pair} is out of bounds.")

    return objective

def solve_edmc(known_distances, known_pairs, num_points):
    """Solves the EDMC problem using gradient descent."""
    initial_guess = np.random.rand(num_points * 3)  # Flatten the initial guess

    result = minimize(edmc_objective, initial_guess, args=(known_distances, known_pairs, num_points))

    return result.x.reshape((num_points, 3))  # Reshape the result into (num_points, 3) coordinates

def find_distance(x, y):
    """Calculates the Euclidean distance between two vectors."""
    return np.sqrt(np.sum((x - y)**2))

def read_distances_from_file(filename):
    """Reads distances from a file and returns the distances and pairs."""
    known_distances = []
    known_pairs = []
    max_index = 0
    with open(filename, 'r') as file:
        for line in file:
            i, j, dist = map(float, line.strip().split())
            i, j = int(i-1), int(j-1)  # Adjust for 0-based indexing
            max_index = max(max_index, i, j)
            known_pairs.append((i, j))
            known_distances.append(dist)
    return known_distances, known_pairs, max_index + 1

# Read distances and pairs from file
known_distances, known_pairs, num_points = read_distances_from_file('../DistanceBounds/distances_constraints.txt')

# Check if the number of points is correct
print(f"Number of points: {num_points}")

# Run multiple iterations of solve_edmc and choose the best solution
best_solution = None
lowest_error = float('inf')

for iteration in range(5):
    print(f"Iteration {iteration + 1}:")
    
    # Solve the EDMC problem
    solution = solve_edmc(known_distances, known_pairs, num_points)

    # Calculate the total error for the solution
    total_error = 0
    for i in range(len(known_pairs)):
        calculated_distance = find_distance(solution[known_pairs[i][0]], solution[known_pairs[i][1]])
        total_error += (known_distances[i] - calculated_distance) ** 2

    print(f"Total Error: {total_error}")

    # Update the best solution if the current one is better
    if total_error < lowest_error:
        lowest_error = total_error
        best_solution = solution

# Print the best solution
print("Best solution coordinates:")
for i, coord in enumerate(best_solution):
    print(f"Point {i+1}: {coord}")

# Save the coordinates to a CSV file up to 3 decimal places
np.savetxt('../DistanceBounds/solution.csv', best_solution, delimiter=',', comments='', fmt='%.3f')

print(f"Lowest Total Error: {lowest_error}")
