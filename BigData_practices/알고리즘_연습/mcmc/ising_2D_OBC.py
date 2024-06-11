import numpy as np
import matplotlib.pyplot as plt
import random

class IsingModel2D:
    def __init__(self, size, temperature, external_field, exchange_interaction, boundary='OBC'):
        self.size = size
        self.temperature = temperature
        self.external_field = external_field
        self.exchange_interaction = exchange_interaction
        self.boundary = boundary
        self.spins = np.random.choice([-1, 1], size=(size, size))

    def calculate_energy_change(self, i, j):
        if self.boundary == 'OBC':
            # 인접 스핀을 열린 경계 조건으로 계산
            top = self.spins[i-1, j] if i > 0 else 0
            bottom = self.spins[i+1, j] if i < self.size - 1 else 0
            left = self.spins[i, j-1] if j > 0 else 0
            right = self.spins[i, j+1] if j < self.size - 1 else 0
        elif self.boundary == 'PBC':
            # 인접 스핀을 주기적 경계 조건으로 계산
            top = self.spins[(i-1) % self.size, j]
            bottom = self.spins[(i+1) % self.size, j]
            left = self.spins[i, (j-1) % self.size]
            right = self.spins[i, (j+1) % self.size]
        
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
                magnetization = np.mean(self.spins)
                magnetizations.append(magnetization)
        return magnetizations

# 시뮬레이션 매개변수
size = 20
temperatures = np.linspace(0.1, 3.0, 100)
external_field = 0  # 외부 자기장
exchange_interaction = 1  # 교환 상호작용 상수
steps = 1000
equilibration_steps = 100

magnetizations_vs_temperature_OBC = []
magnetizations_vs_temperature_PBC = []

# OBC 시뮬레이션
for temperature in temperatures:
    model_OBC = IsingModel2D(size, temperature, external_field, exchange_interaction, boundary='OBC')
    magnetizations_OBC = model_OBC.simulate(steps, equilibration_steps)
    avg_magnetization_OBC = np.mean(magnetizations_OBC)
    magnetizations_vs_temperature_OBC.append(avg_magnetization_OBC)

# PBC 시뮬레이션
for temperature in temperatures:
    model_PBC = IsingModel2D(size, temperature, external_field, exchange_interaction, boundary='PBC')
    magnetizations_PBC = model_PBC.simulate(steps, equilibration_steps)
    avg_magnetization_PBC = np.mean(magnetizations_PBC)
    magnetizations_vs_temperature_PBC.append(avg_magnetization_PBC)

# 그래프 그리기
plt.plot(temperatures, magnetizations_vs_temperature_OBC, marker='o', linestyle='none', label='OBC (size=%d)' % size)
plt.plot(temperatures, magnetizations_vs_temperature_PBC, marker='x', linestyle='none', label='PBC (size=%d)' % size)
plt.xlabel('Temperature')
plt.ylabel('Average Magnetization')
plt.title('Average Magnetization vs. Temperature (OBC vs PBC)')
plt.grid(True)
plt.legend()
plt.show()
