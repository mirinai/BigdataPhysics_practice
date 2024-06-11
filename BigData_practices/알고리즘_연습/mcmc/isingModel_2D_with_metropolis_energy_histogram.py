import numpy as np
import matplotlib.pyplot as plt
import random

class IsingModel2D:
    def __init__(self, size, temperature, external_field):
        self.size = size
        self.temperature = temperature
        self.external_field = external_field
        # 격자 내 스핀 상태를 무작위로 초기화
        self.spins = np.random.choice([-1, 1], size=(size, size))

    def energy(self):
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
                # 외부 자기장과의 상호작용 항 추가
                total_energy += -spin * neighbor_sum - self.external_field * spin
        return total_energy / 2  # Each bond is counted twice

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
        energy_change = 2 * spin * (neighbor_sum + self.external_field)
        # 스핀을 뒤집을지 결정하는 메트로폴리스 알고리즘 적용
        if energy_change < 0 or random.random() < np.exp(-energy_change / self.temperature):
            self.spins[i, j] *= -1

    def simulate(self, steps):
        energies = []
        # 주어진 스텝 수만큼 메트로폴리스 알고리즘 반복
        for _ in range(steps):
            self.metropolis_step()
            energies.append(self.energy())
        return energies

# 모델 파라미터 설정
size = 20
temperature = 2.0
external_field = 0.5
steps = 10000

# 모델 생성
ising_model = IsingModel2D(size, temperature, external_field)

# 메트로폴리스 알고리즘으로 시뮬레이션 실행
energies = ising_model.simulate(steps)

# 에너지 히스토그램 플롯
plt.hist(energies, bins=50)
plt.xlabel('Energy')
plt.ylabel('Frequency')
plt.title('Energy Distribution in 2D Ising Model')
plt.show()
