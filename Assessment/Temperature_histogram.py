# Import NumPy library
import numpy as np

# Import Matplotlib library
import matplotlib.pyplot as plt

# Generate 100 random temperature values between 20 and 40
temperature = np.random.randint(20, 40, 100)

# Display generated temperatures
print("Temperature Data:")
print(temperature)

# Create histogram
plt.hist(temperature)

# Add title
plt.title("Temperature Distribution")

# Add labels
plt.xlabel("Temperature")
plt.ylabel("Frequency")

# Display histogram
plt.show()

'''
output
Temperature Data:
[21 35 28 31 22 39 25 30 27 36 ...]

A histogram is displayed showing the distribution
of temperature values.
'''
