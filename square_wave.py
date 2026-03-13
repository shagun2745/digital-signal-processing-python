import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 500)

signal = np.sign(np.sin(2 * np.pi * 5 * t))

plt.plot(t, signal)
plt.title("Square Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.show()
