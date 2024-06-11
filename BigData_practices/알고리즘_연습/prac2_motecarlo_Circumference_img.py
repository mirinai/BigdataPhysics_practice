import matplotlib.pyplot as plt
import random

def piEstimated(num_points, iteration, L):
    total_points = num_points

    estimated_pis = []
    for _ in range(iteration):  # 주어진 횟수만큼 반복하여 추정치 계산
        pointsInCircle = 0  # 각 반복마다 원 안에 들어간 점의 개수를 초기화합니다.
        for _ in range(num_points):  # 주어진 점의 개수만큼 반복합니다.
            x = random.uniform(0, L)  # 0부터 L까지의 범위에서 x값을 랜덤으로 생성합니다.
            y = random.uniform(0, L)  # 0부터 L까지의 범위에서 y값을 랜덤으로 생성합니다.

            if x ** 2 + y ** 2 <= L * L:  # 점이 원 안에 들어가는지 확인합니다.
                pointsInCircle += 1  # 원 안에 들어간 점의 개수를 세어줍니다.

        # 사분원의 넓이를 추정하고, 4를 곱하여 실제 원주율에 가까운 값을 얻습니다.
        estimated_pi = 4 * pointsInCircle / total_points
        estimated_pis.append(estimated_pi)  # 추정된 원주율을 리스트에 추가합니다.

    return estimated_pis

# 파라미터 설정
L = 3  # 사각형의 한 변의 길이
num_points = 100000  # 생성할 점의 개수
iteration = 30  # 추정을 반복할 횟수

# 원주율 추정치 계산
estimated_pis = piEstimated(num_points, iteration, L)

# 그래프 표시
plt.plot(estimated_pis, marker='o')  # 추정치를 그래프로 표시
plt.xlabel('Iteration')  # x축 레이블 설정
plt.ylabel('Estimated Pi')  # y축 레이블 설정
plt.title('Estimated Pi vs Iteration')  # 그래프 제목 설정
plt.grid(True)  # 그리드 표시
plt.show()  # 그래프 표시