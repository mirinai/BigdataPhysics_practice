import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 10  # 격자 크기
nsteps = 1000  # 메트로폴리스 알고리즘 단계 수

# 초기 상태 설정
spins = np.random.choice([-1, 1], size=(L, L))

# 에너지 계산 함수
def energy(spins):
    return -np.sum(spins * (np.roll(spins, 1, axis=0) + np.roll(spins, 1, axis=1)))
'''np.roll 함수는 배열의 요소들을 주어진 횟수만큼 "굴림"시킵니다. 예를 들어, 배열 [1, 2, 3, 4, 5]가 있다고 할 때, 
np.roll(arr, 2)는 배열을 오른쪽으로 두 칸씩 굴려 [4, 5, 1, 2, 3]을 반환합니다.

이 함수는 주로 이징 모델과 같은 격자 모델에서 사용됩니다. 격자의 각 위치는 이웃한 위치와 상호작용하는데, 
이 때 배열의 요소를 굴리는 것으로 이웃한 위치를 쉽게 처리할 수 있습니다. 
따라서 np.roll은 격자 모델에서 이웃한 위치와의 상호작용을 계산하는 데 유용하게 사용됩니다.'''

# 자화 계산 함수
def magnetization(spins):
    return np.sum(spins)

# 온도 범위 설정
temps = np.arange(1.0, 4.1, 0.1)

# 자화 저장 리스트
magnetizations = []

# 각 온도에서 메트로폴리스 알고리즘 실행
for T in temps:
    mag = []
    for _ in range(nsteps):
        i, j = np.random.randint(0, L, size=2)  # 무작위 격자 위치(인덱스) 선택, 정수 난수 만들기
        
        #spins[i][j]와 달리 동시에 엘레멘트 접근            
        dE = 2 * spins[i, j] * (    
            spins[(i - 1) % L, j]
            + spins[(i + 1) % L, j]
            + spins[i, (j - 1) % L]
            + spins[i, (j + 1) % L]#만약 (i,j)==(0,0)이면 (i-1,j)==(-1,0)=>(9,0) : PBC
            #따라서 -1%L== 9 그리고 
            # 에너지 변화 계산 (i,j)==(9,9)이면 (i+1,j)==(10,9) =>(0,9) : PBC
            #10%L==0이 되어서 범위를 벗어나지 않는다.
        )   
            
        '''spins[i, j]: 현재 위치 (i, j)의 스핀
        spins[(i - 1) % L, j]: 현재 위치 (i, j)의 위쪽 이웃 스핀
        spins[(i + 1) % L, j]: 현재 위치 (i, j)의 아래쪽 이웃 스핀
        spins[i, (j - 1) % L]: 현재 위치 (i, j)의 왼쪽 이웃 스핀
        spins[i, (j + 1) % L]: 현재 위치 (i, j)의 오른쪽 이웃 스핀
        
        수식에서 2를 곱하는 것은 각 스핀과 이웃한 네 개의 스핀 간의 상호작용을 두 번 반영하는 것을 의미
        '''
        if dE <= 0 or np.random.rand() < np.exp(-dE / T):  # 메트로폴리스 조건
            spins[i, j] *= -1
        mag.append(magnetization(spins))
    magnetizations.append(np.mean(mag))

# 그래프 그리기
plt.plot(temps, magnetizations, marker='o')
plt.xlabel('Temperature')
plt.ylabel('Magnetization')
plt.title('Magnetization vs. Temperature (Ising Model)')
plt.grid(True)
plt.show()
