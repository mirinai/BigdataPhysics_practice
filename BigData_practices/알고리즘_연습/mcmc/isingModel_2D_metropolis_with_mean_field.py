import numpy as np
import random
import matplotlib.pyplot as plt
class IsingModel2D:
    def __init__(self, size, temperature, external_field, exchange_interaction):
        self.size = size
        self.temperature = temperature
        self.external_field = external_field
        self.exchange_interaction = exchange_interaction
        self.spins = np.random.choice([-1, 1], size=(size, size))

    def calculate_energy_change(self, i, j):
        top = self.spins[(i-1)%self.size, j]
        bottom = self.spins[(i+1)%self.size, j]
        left = self.spins[i, (j-1)%self.size]
        right = self.spins[i, (j+1)%self.size]
        neighbor_sum = top + bottom + left + right
        delta_energy = 2 * self.spins[i, j] * (self.exchange_interaction * neighbor_sum + self.external_field)
        return delta_energy

    def metropolis_step(self):
        for _ in range(self.size**2):
            i, j = random.randint(0, self.size-1), random.randint(0, self.size-1)
            delta_energy = self.calculate_energy_change(i, j)
            if delta_energy < 0 or random.random() < np.exp(-delta_energy / self.temperature):
                self.spins[i, j] *= -1

    def simulate(self, steps, equilibration_steps):
        magnetizations = []
        for step in range(steps + equilibration_steps):
            self.metropolis_step()
            if step >= equilibration_steps:
                total_magnetization = np.sum(self.spins)
                magnetizations.append(abs(total_magnetization) / self.size**2)
        return magnetizations

def mft_magnetization(temperature, Tc=2.26):
    if temperature > Tc:
        return 0  # Tc를 초과하는 온도에서는 자기화를 0으로 설정
    else:
        m = np.tanh(Tc / temperature)
        return abs(m)

size = 20
temperatures = np.linspace(0.1, 3, 50)  # Tc를 포함하여 더 넓은 범위의 온도를 고려
external_field = 0
exchange_interaction = 1
steps = 1000
equilibration_steps = 100
Tc = 2.26
magnetizations_vs_temperature = []
mft_results = []

for temperature in temperatures:
    model = IsingModel2D(size, temperature, external_field, exchange_interaction)
    magnetizations = model.simulate(steps, equilibration_steps)
    avg_magnetization = np.mean(magnetizations)
    magnetizations_vs_temperature.append(avg_magnetization)
    mft_results.append(mft_magnetization(temperature, Tc))

# 결과 시각화 코드
plt.figure(figsize=(10, 5))
plt.plot(temperatures, magnetizations_vs_temperature, marker='o', linestyle='none', label='Ising Model (Simulated)')
plt.plot(temperatures, mft_results, linestyle='-', label='Mean Field Theory')
plt.xlabel('Temperature')
plt.ylabel('Average Magnetization per Spin (Absolute Value)')
plt.title('Comparison of Ising Model and Mean Field Theory (Absolute Magnetization)')
plt.grid(True)
plt.legend()
plt.show()
