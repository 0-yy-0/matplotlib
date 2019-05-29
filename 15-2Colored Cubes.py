import matplotlib.pyplot as plt

# Define Date
x_values = list(range(5001))
cubes = [x**3 for x in x_values]

# make plot
plt.scatter(x_values, cubes, edgecolors="none", c=cubes, cmap=plt.cm.BuGn, s=4)

# customize plot
plt.title("Cubes", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cubes of Value", fontsize=14)
plt.tick_params(axis="both", labelsize=14)
plt.axis([0,5100, 0, 5100**3])

# show plot
plt.show()