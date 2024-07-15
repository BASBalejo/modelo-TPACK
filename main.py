import numpy as np
import matplotlib.pyplot as plt

# Function to generate heart shape coordinates
def heart_shape(t):
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x, y

# Generate values
t = np.linspace(0, 2 * np.pi, 1000)
x, y = heart_shape(t)

# Plot the heart shape
plt.figure(figsize=(6, 6))
plt.plot(x, y, color='red', linewidth=2)
plt.fill(x, y, 'r', alpha=0.3)  # Fill the heart with a transparent red color
plt.title('Heart Shape')
plt.axis('equal')  # Ensure the aspect ratio is equal
plt.axis('off')  # Turn off the axis
plt.show()
