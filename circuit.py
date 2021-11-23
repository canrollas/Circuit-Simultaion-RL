import numpy as np
import matplotlib.pyplot as plt

R1 = 2000
L1 = 5 * 10 ** (-6)
T = L1 / R1
t = np.linspace(-np.pi * 10, np.pi * 10, 100)
I0 = np.sin(0.8 * t) * 3 / 2
I = (1 - np.exp(-1 / T)) * I0
I2 = (1 - np.exp(-1 / T)) * np.full_like(t, 5)
VR = I * 2

VR2 = I2 / (2)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
Vin = np.sin(0.8 * t) * 3
plt.plot(t, Vin, '-b', label="Voltage-1")
plt.axhline(y=5, color='r', linestyle='-', label="Voltage-2")
plt.plot(t, I, color="g", label="Current-1")

plt.legend(bbox_to_anchor=(0.5, 0., 0.5, 0.04))

plt.show()
It = (Vin / R1) * (1 - np.exp(-R1 * t / L1))
It2 = (np.full_like(t, 5) / R1) * (1 - np.exp(-R1 * t / L1))
plt.plot(t, VR, color="m", label="VOLTAGE OF THE RECISTOR-1")
plt.plot(t, VR2, color="r", label="VOLTAGE OF THE RECISTOR-2")
plt.legend(bbox_to_anchor=(0.5, 0., 0.5, 0.04))
plt.show()
plt.plot(t, It, label="Current 1")
plt.plot(t, It2, label="Current 2")
plt.legend(bbox_to_anchor=(0.5, 0., 0.5, 0.04))
plt.show()
