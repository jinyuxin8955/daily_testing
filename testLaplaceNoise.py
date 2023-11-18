import numpy as np

def add_laplacian_noise(gradients, epsilon, sensitivity):
    """
    Add Laplace noise to gradients to achieve differential privacy.

    Parameters:
    gradients (numpy array): Gradients to which noise will be added.
    epsilon (float): Privacy parameter controlling the privacy guarantee.
    sensitivity (float): Sensitivity of the function being computed.

    Returns:
    noisy_gradients (numpy array): Gradients with added Laplace noise.
    """
    # Calculate the scale parameter for Laplace distribution
    scale = sensitivity / epsilon

    # Generate Laplace noise for each gradient
    noise = np.random.laplace(0, scale, gradients.shape)

    # Add noise to the gradients
    noisy_gradients = gradients + noise

    return noisy_gradients


# Example usage
# Assume gradients is a numpy array representing the gradients
gradients = np.array([1.2, -0.5, 0.8, 2.1])

# Parameters for differential privacy
epsilon = 10  # Privacy parameter
sensitivity = 0.1  # Sensitivity of the function being computed (e.g., max gradient value)

# Add Laplace noise to gradients
noisy_gradients = add_laplacian_noise(gradients, epsilon, sensitivity)

print("Original gradients:", gradients)
print("Noisy gradients:", noisy_gradients)
