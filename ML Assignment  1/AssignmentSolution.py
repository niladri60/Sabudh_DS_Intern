# 1. Write a function to generate an m+1m+1 dimensional data set, of size nn, consisting of mm continuous independent variables (XX) and one dependent variable (YY) defined as:
# yi=xiβ+e
# yi​=xi​β+e

# where:

#     ee is a Gaussian distribution with mean 0 and standard deviation σσ, representing the unexplained variation in YY.
#     ββ is a random vector of dimensionality m+1m+1, representing the coefficients of the linear relationship between XX and YY.
#     ∀i∈[1,n],xi0=1∀i∈[1,n],xi0​=1.

# Function Parameters

#     σ: The spread of noise in the output variable.
#     n: The size of the data set.
#     m: The number of independent variables.

# Function Output

# The function should output:

#     X: An n×mn×m numpy array of independent variable values (with a 1 in the first column).
#     Y: The n×1n×1 numpy array of output values.
#     β: The random coefficients used to generate YY from XX.


import numpy as np

def generate_dataset(sigma, n, m):
    # Generate the independent variables (X)
    X = np.random.rand(n, m)  # Generate random values between 0 and 1 for n rows and m columns
    X = np.c_[np.ones(n), X]  # Add a column of ones to X to account for the intercept term

    # Generate the coefficients (β) as a random vector of dimensionality (m+1)
    beta = np.random.rand(m + 1)

    # Generate the noise (e) using Gaussian distribution with mean 0 and standard deviation sigma
    e = np.random.normal(0, sigma, n)

    # Calculate the dependent variable (Y) as Y = Xβ + e
    Y = X.dot(beta) + e

    return X, Y, beta

# Example usage
sigma = 1.0  # Standard deviation of the noise
n = 100  # Number of data points
m = 3    # Number of independent variables

X, Y, beta = generate_dataset(sigma, n, m)
X[:5], Y[:5], beta  # Display the first 5 rows of X and Y, and the generated beta vector


# output

(array([[1.        , 0.63766073, 0.52650149, 0.46671656],
        [1.        , 0.36836046, 0.40537162, 0.97024028],
        [1.        , 0.24825243, 0.44946802, 0.33971434],
        [1.        , 0.10300681, 0.23884826, 0.21818654],
        [1.        , 0.63145995, 0.25377699, 0.09404164]]),
 array([-1.35103402,  1.17954042,  0.82759973, -0.905757  , -0.45825481]),
 array([0.01598857, 0.17125071, 0.80757561, 0.04395195]))

#  2. Write a function that learns the parameters of a linear regression line given inputs
# • X: An n × m numpy array of independent variable values
# • Y : The n × 1 numpy array of output values
# • k: the number of iteractions (epochs)
# • τ : the threshold on change in Cost function value from the previous to current iteration
# • λ: the learning rate for Gradient Descent
# The function should implement the Gradient Descent algorithm as discussed in class that initialises β with
# random values and then updates these values in each iteraction by moving in the the direction defined by
# the partial derivative of the cost function with respect to each of the coefficients. The function should use
# only one loop that ends after a number of iterations (k) or a threshold on the change in cost function value
# (τ ).
# The output should be an m + 1 dimensional vector of coefficients and the final cost function value.

# Re-import necessary libraries and redefine the function after the environment reset

import numpy as np

def gradient_descent(X, Y, k, tau, learning_rate):
    
    # Function to learn the parameters of a linear regression model using Gradient Descent.
    
    # Parameters:
    # X (numpy array): An n × m array of independent variable values.
    # Y (numpy array): An n × 1 array of output values.
    # k (int): The number of iterations (epochs).
    # tau (float): The threshold for the change in cost function value.
    # learning_rate (float): The learning rate for Gradient Descent.
    
    # Returns:
    # beta (numpy array): An (m + 1) dimensional vector of coefficients.
    # final_cost (float): The final cost function value.
    
    
    # Initialize beta with random values
    m = X.shape[1]
    beta = np.random.rand(m + 1)
    
    # Add a column of ones to X to account for the intercept term
    X = np.c_[np.ones(X.shape[0]), X]
    
    # Calculate the initial cost function value
    def compute_cost(X, Y, beta):
        n = len(Y)
        predictions = X.dot(beta)
        cost = (1 / (2 * n)) * np.sum((predictions - Y) ** 2)
        return cost
    
    cost_prev = compute_cost(X, Y, beta)
    
    for iteration in range(k):
        # Calculate predictions
        predictions = X.dot(beta)
        
        # Compute the gradient
        errors = predictions - Y
        gradient = (1 / len(Y)) * X.T.dot(errors)
        
        # Update beta values
        beta -= learning_rate * gradient
        
        # Calculate the new cost
        cost_current = compute_cost(X, Y, beta)
        
        # Check for convergence based on the threshold (tau)
        if abs(cost_prev - cost_current) < tau:
            break
        
        # Update the previous cost
        cost_prev = cost_current

    final_cost = cost_prev
    return beta, final_cost

# Example usage
n, m = 100, 3  # Number of data points and independent variables
X = np.random.rand(n, m)
Y = np.random.rand(n)

# Gradient descent parameters
k = 1000         # Number of iterations
tau = 1e-6       # Threshold for convergence
learning_rate = 0.01  # Learning rate

beta, final_cost = gradient_descent(X, Y, k, tau, learning_rate)
beta, final_cost


# Output
(array([0.01174094, 0.19954705, 0.30966369, 0.43042265]), 0.05406741884186257)

# The gradient descent function successfully computed the parameters of a linear regression line. Here are the results:

#     β (Coefficients Vector):
#     β=[0.01174094,0.19954705,0.30966369,0.43042265]
#     β=[0.01174094,0.19954705,0.30966369,0.43042265]

#     This vector represents the intercept term and the coefficients for each independent variable.

#     Final Cost Function Value:
#     Final Cost=0.05406741884186257
#     Final Cost=0.05406741884186257

# 3. Create a report investigating how differen values of n and σ impact the ability for your linear regression
# function to learn the coefficients, β, used to generate the output vector Y .

import numpy as np
import matplotlib.pyplot as plt

def generate_dataset(sigma, n, m):
    X = np.random.rand(n, m)
    X = np.c_[np.ones(n), X]
    beta = np.random.rand(m + 1)
    e = np.random.normal(0, sigma, n)
    Y = X.dot(beta) + e
    return X, Y, beta

def gradient_descent(X, Y, k, tau, learning_rate):
    m = X.shape[1]
    beta = np.random.rand(m)
    cost_prev = float('inf')

    def compute_cost(X, Y, beta):
        n = len(Y)
        predictions = X.dot(beta)
        cost = (1 / (2 * n)) * np.sum((predictions - Y) ** 2)
        return cost

    for _ in range(k):
        predictions = X.dot(beta)
        errors = predictions - Y
        gradient = (1 / len(Y)) * X.T.dot(errors)
        beta -= learning_rate * gradient
        cost_current = compute_cost(X, Y, beta)
        if abs(cost_prev - cost_current) < tau:
            break
        cost_prev = cost_current

    final_cost = cost_prev
    return beta, final_cost

def mean_squared_error(beta_true, beta_learned):
    return np.mean((beta_true - beta_learned) ** 2)

# Experiment parameters
m = 3                # Number of independent variables
k = 1000             # Number of iterations
tau = 1e-6           # Threshold for convergence
learning_rate = 0.01 # Learning rate for gradient descent

# Different values of n and σ for the experiment
n_values = [50, 100, 200, 500]
sigma_values = [0.1, 0.5, 1.0, 2.0]

# Store results
results = []

for n in n_values:
    for sigma in sigma_values:
        X, Y, beta_true = generate_dataset(sigma, n, m)
        beta_learned, _ = gradient_descent(X, Y, k, tau, learning_rate)
        mse = mean_squared_error(beta_true, beta_learned)
        results.append((n, sigma, mse))

# Plotting results
plt.figure(figsize=(10, 6))
for sigma in sigma_values:
    mse_values = [result[2] for result in results if result[1] == sigma]
    plt.plot(n_values, mse_values, marker='o', label=f'σ = {sigma}')

plt.title('Impact of Dataset Size (n) and Noise (σ) on Learning Coefficients')
plt.xlabel('Dataset Size (n)')
plt.ylabel('Mean Squared Error (MSE) of Learned Coefficients')
plt.legend()
plt.grid(True)
plt.show()

