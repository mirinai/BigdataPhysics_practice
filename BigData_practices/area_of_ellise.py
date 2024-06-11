import numpy as np

import matplotlib.pyplot as plt

class EllipticalDistribution:
    def __init__(self, a, b, num_points):
        self.a = a  # 가로 축 반지름
        self.b = b  # 세로 축 반지름
        self.num_points = num_points
        self.x = None
        self.y = None
        self.area = None
    def generate_points(self):
        # 정규 분포를 따르는 난수 생성
        self.x = np.random.normal(loc=0, scale=1, size=self.num_points)
        self.y = np.random.normal(loc=0, scale=1, size=self.num_points)

        # 스케일링하여 타원 분포 생성
        self.x *= self.a
        self.y *= self.b

    def calculate_area(self):
        # 타원 안에 위치한 점의 개수 세기
        points_inside_ellipse = sum((self.x / self.a) ** 2 + (self.y / self.b) ** 2 <= 1)

        # 타원의 넓이 계산
        self.area = (points_inside_ellipse / self.num_points) * (4 * self.a * self.b)


    def plot_distribution(self):
        plt.scatter(self.x, self.y, s=5)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Random Points in Elliptical Distribution')
        plt.show()

# 타원의 가로와 세로 축의 크기 설정
a = 2  # 가로 축 반지름
b = 1  # 세로 축 반지름

# 타원 분포 생성 및 넓이 계산
num_points = 100000
ellipse = EllipticalDistribution(a, b, num_points)
ellipse.generate_points()
ellipse.calculate_area()

# 생성된 타원 분포 시각화
ellipse.plot_distribution()

# 추정된 타원의 넓이 출력
print("Estimated Area of the Ellipse:", ellipse.area)
print("--------------------")