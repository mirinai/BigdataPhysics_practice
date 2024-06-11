import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 100  # 격자 크기
nsteps = 1000  # 몬테카를로 단계 수
n_measurements = 100  # 측정 횟수
#temperatures = np.linspace(0.1, 5.0, 30)  # 온도 범위
temperatures = np.arange(0.1, 10, 0.1)
# 자화 계산 함수
def magnetization(spins):
    return np.sum(spins)

# 몬테카를로 시뮬레이션
magnetizations = []

for T in temperatures:
    spins = np.random.choice([-1, 1], size=(L, L))

    for _ in range(nsteps):
        i, j = np.random.randint(0, L, size=2)
        dE = 2 * spins[i, j] * (
            spins[(i - 1) % L, j]
            + spins[(i + 1) % L, j]
            + spins[i, (j - 1) % L]
            + spins[i, (j + 1) % L]
        )

        if dE <= 0 or np.random.rand() < np.exp(-dE / T):
            spins[i, j] *= -1

    measurements = [magnetization(spins) for _ in range(n_measurements)]
    magnetizations.append(np.mean(measurements))

# 그래프 그리기
plt.plot(temperatures, magnetizations)
plt.xlabel('Temperature')
plt.ylabel('Magnetization')
plt.title('Magnetization vs Temperature (Ising Model)')
plt.show()