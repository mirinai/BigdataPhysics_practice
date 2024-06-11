import numpy as np
import matplotlib.pyplot as plt

# 목표 분포: 정규 분포(N(0, 1))
def target_distribution(x):
    return np.exp(-0.5 * x**2) / np.sqrt(2 * np.pi)

# 제안 분포: 현재 상태에서 작은 변화를 가하는 정규 분포(N(0, 0.5))
def proposal_distribution(x):
    return np.random.normal(loc=x, scale=0.5)
'''np.random.normal(loc=x, scale=0.5)은 평균이 loc이고 표준 편차가 scale인 정규 분포로부터 무작위 표본을 추출하는 NumPy 함수'''

# 메트로폴리스-헤이스팅스 알고리즘
def metropolis_hastings(target_distribution, proposal_distribution, num_samples):
    samples = []
    current_state = np.random.normal()  # 초기 상태 설정

    for _ in range(num_samples):
        # 새로운 상태 제안
        proposed_state = proposal_distribution(current_state)

        # 헤이스팅스 비 계산
        alpha = (target_distribution(proposed_state) / target_distribution(current_state)) * \
                (proposal_distribution(current_state) / proposal_distribution(proposed_state))
        # \ : 줄바꿈

        # 새로운 상태를 받아들일지 여부 결정, 그냥 엔터 쳐도
        if np.random.rand() < min(1, alpha):#min(1, alpha)는 alpha와 1 중에서 작은 값을 선택하는 것을 의미
            current_state = proposed_state

        samples.append(current_state)

    return samples

# 표본 생성
num_samples = 10000
samples = metropolis_hastings(target_distribution, proposal_distribution, num_samples)

# 표본 분포 시각화
plt.figure(figsize=(10, 6))
plt.hist(samples, bins=50, density=True, alpha=0.7, color='skyblue', label='Samples')
x = np.linspace(-5, 5, 1000)
plt.plot(x, target_distribution(x), color='red', linewidth=2, label='Target Distribution')
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Metropolis-Hastings Sampling')
plt.legend()
plt.grid(True)
plt.show()
