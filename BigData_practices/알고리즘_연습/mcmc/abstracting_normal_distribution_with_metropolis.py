import numpy as np
import matplotlib.pyplot as plt

# 목표 분포: 정규 분포 N(5, 1)
def target_distribution(x):
    return np.exp(-0.5 * ((x - 5) ** 2) / 1) / np.sqrt(2 * np.pi)

# 제안 분포: 현재 상태에서 정규 분포에서 추출한 값으로부터 생성 (가우시안 이동)
def proposal_distribution(x_current, sigma=1):
    return np.random.normal(x_current, sigma)

# Metropolis-Hastings 알고리즘
def metropolis_hastings(iterations, initial_state, proposal_sigma):
    samples = [initial_state]
    current_state = initial_state

    for i in range(iterations):
        proposed_state = proposal_distribution(current_state, proposal_sigma)
        acceptance_ratio = min(1, target_distribution(proposed_state) / target_distribution(current_state))
        
        if np.random.rand() < acceptance_ratio:
            current_state = proposed_state

        samples.append(current_state)

    return samples

# 알고리즘 실행
iterations = 10000
initial_state = 0  # 초기 상태
proposal_sigma = 1  # 제안 분포의 표준편차

samples = metropolis_hastings(iterations, initial_state, proposal_sigma)

# 결과 시각화
plt.figure(figsize=(10, 6))
plt.hist(samples, bins=50, density=True, alpha=0.6, color='g', label='MCMC Samples')
x = np.linspace(min(samples), max(samples), 1000)
plt.plot(x, target_distribution(x), 'r-', label='Target Distribution (N(5, 1))')
plt.title('Metropolis-Hastings Algorithm')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()
