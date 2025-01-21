import matplotlib.pyplot as plt

# Vos données
n = [0, 1, 2, 3, 4]
x = [1, 3, 1, 0, -2]
plt.stem(n, x)
plt.xlabel('n')
plt.ylabel('g(n)')
plt.title('Signal discret')
plt.grid(True)
plt.show()