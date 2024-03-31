import numpy as np
import matplotlib.pyplot as plt
import random

class IsingModel2D:
    def __init__(self, size, temperature, external_field, exchange_interaction):
        self.size = size
        self.temperature = temperature
        self.external_field = external_field
        self.exchange_interaction = exchange_interaction
        # 격자 내 스핀 상태를 모두 위로 향하도록 초기화
        self.spins = np.ones((size, size))

    '''def energy(self):
        total_energy = 0
        # 각 스핀의 에너지 계산
        for i in range(self.size):
            for j in range(self.size):
                spin = self.spins[i, j]
                neighbor_sum = (
                    self.spins[(i+1)%self.size, j] + 
                    self.spins[(i-1)%self.size, j] + 
                    self.spins[i, (j+1)%self.size] + 
                    self.spins[i, (j-1)%self.size]
                )
                # 교환 상호작용 항 추가
                total_energy += -self.exchange_interaction * spin * neighbor_sum
                # 외부 자기장과의 상호작용 항 추가
                total_energy += -self.external_field * spin
        return total_energy / 2  # Each bond is counted twice'''

    def metropolis_step(self):
        # 무작위로 스핀을 선택하여 에너지 변화 계산 후 스핀을 뒤집을지 결정
        i, j = random.randint(0, self.size-1), random.randint(0, self.size-1)
        spin = self.spins[i, j]
        neighbor_sum = (
            self.spins[(i+1)%self.size, j] + 
            self.spins[(i-1)%self.size, j] + 
            self.spins[i, (j+1)%self.size] + 
            self.spins[i, (j-1)%self.size]
        )
        energy_change = 2 * spin * (self.exchange_interaction*neighbor_sum + self.external_field)
        
        # min(1, exp(-ΔE / T))보다 클 때에만 스핀을 뒤집음
        if energy_change > 0 and random.random() < np.exp(-energy_change / self.temperature):
            spin *= -1  # 스핀을 뒤집음
        
        self.spins[i, j] = spin  # 수정된 스핀을 저장

    def simulate(self, steps):
        magnetizations = []
        # 주어진 스텝 수만큼 메트로폴리스 알고리즘 반복
        for _ in range(steps):
            self.metropolis_step()
            magnetizations.append(np.mean(self.spins))
        return magnetizations

# 모델 파라미터 설정
size = 20
external_field = 0.5
exchange_interaction = 0.5
steps = 10000

# 온도를 변화시키면서 자화를 계산
temperatures = np.linspace(0.1, 5.0, 50)
magnetizations_vs_temperature = []

for temperature in temperatures:
    # 모델 생성
    ising_model = IsingModel2D(size, temperature, external_field, exchange_interaction)
    # 메트로폴리스 알고리즘으로 시뮬레이션 실행
    magnetizations = ising_model.simulate(steps)
    # 결과 저장
    magnetizations_vs_temperature.append(np.mean(magnetizations))

# 그래프 그리기
plt.plot(temperatures, magnetizations_vs_temperature)
plt.xlabel('Temperature')
plt.ylabel('Magnetization')
plt.title('Magnetization vs Temperature')
plt.show()
