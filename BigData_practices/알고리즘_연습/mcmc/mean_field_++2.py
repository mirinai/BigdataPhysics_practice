import numpy as np
import matplotlib.pyplot as plt

N = 199  # 200 - 1
Tl = 0.0
Th = 2.26
dT = (Th - Tl) / (N + 1)
arr_T = Tl + (np.arange(1, N + 1) * dT)
'''
N = 199: 이 값은 온도가 변하는 구간의 개수를 정의합니다. 즉, 총 199개의 구간으로 온도 범위를 나누겠다는 의미입니다. 
여기서 200 - 1은 200개의 점을 생성하려면, 점과 점 사이의 구간이 199개 있어야 함을 나타냅니다.

Tl = 0.0: 이는 온도 범위의 최소값입니다. Tl은 "Temperature low"의 약자로, 온도 범위의 시작점을 의미합니다.

Th = 2.0: 이는 온도 범위의 최대값입니다. Th는 "Temperature high"의 약자로, 온도 범위의 끝점을 나타냅니다.

dT = (Th - Tl) / (N + 1): 이는 각 온도 구간의 크기를 계산합니다. 전체 온도 범위(Th - Tl)를 구간의 개수(N + 1)로 나누어, 
각 구간 사이의 온도 차이를 구합니다. 여기서 N + 1로 나누는 이유는 N개의 구간이 N + 1개의 점을 정의하기 때문입니다.

arr_T = Tl + (np.arange(1, N + 1) * dT): 이는 계산된 각 온도 구간의 값을 가지는 배열을 생성합니다. 
np.arange(1, N + 1)은 1부터 N까지의 값을 생성하고, 이 각각에 dT를 곱하여 시작 온도 Tl부터 각 구간별 온도를 계산합니다. 
결과적으로 arr_T 배열은 온도가 Tl부터 Th까지 변할 때의 모든 온도 값을 포함합니다.

간단히 말해, 이 변수들은 특정 온도 범위(0.0도부터 2.0도까지)를 199개의 작은 구간으로 나누고, 
이 각각의 구간에 해당하는 온도 값을 계산하여 배열에 저장하는 데 사용됩니다. 
이렇게 해서, 온도에 따른 물리적 성질(예: 자화)을 계산하고 분석할 수 있습니다.
'''
S = 0.1  # 초기 자화값
N_lim = 100  # 최대 반복 횟수
E_lim = 1e-8  # 에너지 차이 한계값, 이 값 이하로 떨어지면 반복을 멈춤

arr_S = np.zeros(N)  # 자화값 저장을 위한 배열

# 온도에 따른 자화 계산
for i in range(N):
    for j in range(1, N_lim):
        S_temp = S
        S = np.tanh(S / arr_T[i])  # 자화값 갱신
        if np.abs(S - S_temp) < E_lim:
            break  # 에너지 차이가 한계값 이하이면 멈춤

    arr_S[i] = S

# 온도에 따른 자화 그래프 그리기
plt.figure(figsize=(8, 6))
plt.plot(arr_T, arr_S, label='Magnetization')
plt.xlabel('Temperature')
plt.ylabel('Magnetization')
plt.title('Magnetization vs Temperature')
plt.legend()
plt.grid(True)
plt.show()
