from random import sample, randint
from matplotlib import pyplot as plt

values = randint(10, 25)

x = sample(range(0, 100), values)
y = sample(range(20, 140), values)
x.sort()

plt.xlabel("Time")
plt.ylabel("Price")
plt.title("Price of Thing\nOver Time")
plt.plot(x, y, color = "#ac6b46", linestyle = "--", label = "Thing")
plt.legend()
plt.show()

print(x)
print(y)
