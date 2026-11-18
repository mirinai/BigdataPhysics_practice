import random

class MonteCarloSimulation:
    def __init__(self, num_points):
        self.num_points = num_points
        self.points_inside_circle = 0

    def generate_points(self):
        for _ in range(self.num_points):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)

            if x**2 + y**2 <= 1:
                self.points_inside_circle += 1

    def estimate_pi(self):
        # 원의 넓이는 사각형의 넓이(4)에 원 안에 포함된 점의 비율을 곱한 값이 됩니다.
        # 원의 넓이 = (4 * 원 안에 포함된 점의 개수) / 전체 시도한 점의 개수
        pi_estimate = 4 * self.points_inside_circle / self.num_points
        return pi_estimate

# 몬테카를로 시뮬레이션 객체 생성
num_points = 10000
simulation = MonteCarloSimulation(num_points)

# 무작위 점 생성
simulation.generate_points()

# 원주율(π) 추정
pi_estimate = simulation.estimate_pi()

print("Estimated value of Pi:", pi_estimate)#Estimated value of Pi: 3.1568