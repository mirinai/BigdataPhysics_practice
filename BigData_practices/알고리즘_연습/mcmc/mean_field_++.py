import numpy as np
import matplotlib.pyplot as plt

fc = lambda m, T, C: np.tanh(C * m / T)

def fixed_point1(x0, c, f1):
    x = x0
    diff = 100
    tol = 1e-6
    i = 0
    while diff > tol:
        x = f1(x, c)
        diff = np.abs(f1(x, c) - x)
        i = i + 1
    return x

T = np.arange(0.1, 5, 0.02)
m0_values = [1, 3, 10, 0]
C_values = [2, 3, 4]

plt.figure(figsize=(10, 6))

for C in C_values:
    m_values = []
    for m0 in m0_values:
        m = np.zeros(T.size)
        for i in np.arange(T.size):
            m[i] = fixed_point1(m0, T[i], lambda x, c: fc(x, T[i], c))
        m_values.append(m)

    for i, m0 in enumerate(m0_values):
        plt.plot(T, m_values[i], label=f'C={C}, m0={m0}')

plt.xlabel("Temperature")
plt.ylabel("Magnetization")
plt.legend()
plt.show()
