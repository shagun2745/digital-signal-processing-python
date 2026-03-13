import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 500)

signal = np.sin(2 * np.pi * 5 * t)

noise = np.random.normal(0, 0.3, 500)

noisy_signal = signal + noise

plt.plot(t, noisy_signal)
plt.title("Signal with Noise")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.show()
