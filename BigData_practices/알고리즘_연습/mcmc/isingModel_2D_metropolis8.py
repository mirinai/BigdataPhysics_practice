import numpy as np
import matplotlib.pyplot as plt
import random

class IsingModel2D:
    def __init__(self, size, temperature, external_field, exchange_interaction):
        self.size = size  # 격자 크기
        self.temperature = temperature  # 온도
        self.external_field = external_field  # 외부 자기장
        self.exchange_interaction = exchange_interaction  # 교환 상호작용 상수
        self.spins = np.random.choice([-1, 1], size=(size, size))  # 스핀 배열 초기화

    def calculate_energy_change(self, i, j):
        # 인접한 스핀과의 상호작용으로 인한 에너지 변화 계산
        top = self.spins[(i-1)%self.size, j]
        bottom = self.spins[(i+1)%self.size, j]
        left = self.spins[i, (j-1)%self.size]
        right = self.spins[i, (j+1)%self.size]
        neighbor_sum = top + bottom + left + right

        delta_energy = 2 * self.spins[i, j] * (self.exchange_interaction * neighbor_sum + self.external_field)
        return delta_energy

    def metropolis_step(self):
        # 메트로폴리스 알고리즘 한 스텝 실행
        for _ in range(self.size**2):
            i, j = random.randint(0, self.size-1), random.randint(0, self.size-1)
            delta_energy = self.calculate_energy_change(i, j)
            if delta_energy < 0 or random.random() < np.exp(-delta_energy / self.temperature):
                self.spins[i, j] *= -1

    def simulate(self, steps, equilibration_steps):
        # 시뮬레이션 실행
        magnetizations = []
        for step in range(steps+equilibration_steps):
            self.metropolis_step()
            if step >= equilibration_steps:
                magnetization = np.mean(self.spins)
                magnetizations.append(magnetization)
        return magnetizations

# 시뮬레이션 매개변수
size = 80  # 격자 크기
temperatures = np.linspace(0.1, 3.0, 100)  # 온도 범위
external_fields = [-0.01, 0, 0.01]  # 외부 자기장 값
exchange_interaction = 1  # 교환 상호작용 상수
steps = 1000  # 총 스텝 수
equilibration_steps = 100  # 평형화에 필요한 스텝 수

for external_field in external_fields:
    magnetizations_vs_temperature = []
    for temperature in temperatures:
        model = IsingModel2D(size, temperature, external_field, exchange_interaction)
        magnetizations = model.simulate(steps, equilibration_steps)
        avg_magnetization = np.mean(magnetizations)
        magnetizations_vs_temperature.append(avg_magnetization)
    
    # 결과를 그래프로 표시
    plt.plot(temperatures, magnetizations_vs_temperature, marker='o', linestyle='none', label=f'Field={external_field}')

plt.xlabel('Temperature')
plt.ylabel('Average Magnetization')
plt.title('Average Magnetization vs Temperature for Different External Fields')
plt.grid(True)
plt.legend()
plt.show()
