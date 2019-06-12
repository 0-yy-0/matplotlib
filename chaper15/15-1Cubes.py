import matplotlib.pyplot as plt

# Define date
x_value = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]

# Make plot
plt.scatter(x_value, cubes, edgecolor='none', s=40)

# Customize plot
plt.title("Cubes", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cubes of Value", fontsize=14)
plt.tick_params(axis="both", labelsize=14)

# Show plot
plt.show()