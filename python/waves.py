import numpy as np
import matplotlib.pyplot as plt

# Time array
t = np.linspace(0, 1, 1000)

# Input signal (sine wave)
x = np.sin(2 * np.pi * 5 * t)

# Tremolo effect
f = 5  # Frequency of the tremolo effect
tremolo = x * (1 + np.sin(2 * np.pi * f * t))

# Distortion & Overdrive effect
T = 0.5  # Threshold for distortion
distortion = np.where(np.abs(x) < T, x, T * np.sign(x))

# FUZZ effect
fuzz = np.sign(x)

# DELAY effect
alpha = 0.5  # Amplitude of the delayed signal
tau = 0.1  # Delay time in seconds
delay = x + alpha * np.roll(x, int(tau * len(t)))

# Plotting the waveforms
plt.figure(figsize=(12, 8))

plt.subplot(5, 1, 1)
plt.plot(t, x)
plt.title('Original Signal')

plt.subplot(5, 1, 2)
plt.plot(t, tremolo)
plt.title('Tremolo Effect')

plt.subplot(5, 1, 3)
plt.plot(t, distortion)
plt.title('Distortion & Overdrive Effect')

plt.subplot(5, 1, 4)
plt.plot(t, fuzz)
plt.title('FUZZ Effect')

plt.subplot(5, 1, 5)
plt.plot(t, delay)
plt.title('DELAY Effect')

plt.tight_layout()
plt.show()