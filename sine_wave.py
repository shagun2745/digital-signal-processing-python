import numpy as np
import matplotlib.pyplot as plt

# time values
t = np.linspace(0, 1, 500)

# sine wave
signal = np.sin(2 * np.pi * 5 * t)

# plot
plt.plot(t, signal)
plt.title("Sine Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.show()
