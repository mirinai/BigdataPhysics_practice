# Circle 클래스는 원을 표현하며, 반지름을 초기화하는 생성자를 갖습니다.
# add_point 메서드는 (x, y) 좌표가 원 안에 있는지 확인하고, 내부 또는 외부 점 리스트에 추가합니다.
# plot_points 메서드는 원 안과 밖의 점들을 산점도로 그립니다.
# creatCirclePoints 함수는 원을 생성하고 내부에 점을 추가하여 리스트에 저장합니다.

import matplotlib.pyplot as plt
import random

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.inside_points = []     # 원 안의 점 리스트 초기화
        self.outside_points = []    # 원 바깥의 점 리스트 초기화

    def add_point(self, x, y):
        if x ** 2 + y ** 2 <= self.radius ** 2:   # 원 안에 있는지 확인
            self.inside_points.append((x, y))    # 원 안의 점 리스트에 추가
        else:
            self.outside_points.append((x, y))   # 원 바깥의 점 리스트에 추가

    def plot_points(self):
        inside_x, inside_y = zip(*self.inside_points)     # 원 안의 x, y 좌표를 분리
        outside_x, outside_y = zip(*self.outside_points)  # 원 바깥의 x, y 좌표를 분리

        # 원 안의 점과 바깥의 점을 각각 산점도로 표시
        plt.scatter(inside_x, inside_y, color='red', alpha=0.5)
        plt.scatter(outside_x, outside_y, color='blue', alpha=0.5)

def creatCirclePoints(num_points, iteration, L):
    circles = []   # 원들을 저장할 리스트 초기화
    for _ in range(iteration):
        circle = Circle(L)   # 원 객체 생성
        for _ in range(num_points):
            x = random.uniform(-L, L)   # 랜덤한 x 좌표 생성
            y = random.uniform(-L, L)   # 랜덤한 y 좌표 생성
            circle.add_point(x, y)      # 원 안에 있는지 확인하고 점 추가
        circles.append(circle)          # 원을 리스트에 추가
    return circles                      # 생성된 원들 반환

if __name__ == "__main__":
    # 파라미터 설정
    L = 5           # 사각형의 한 변의 길이
    num_points = 100  # 생성할 점의 개수
    iteration = 100  # 추정을 반복할 횟수

    # 원 생성 및 플롯
    circles = creatCirclePoints(num_points, iteration, L)
    for circle in circles:
        circle.plot_points()

    # 그래프 표시
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Points in and out of the Circle')
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')  # 원의 형태가 왜곡되지 않도록 가로, 세로 축의 스케일을 동일하게 설정
    plt.show()
    circles = creatCirclePoints(num_points, iteration, L)

    # 원 생성 및 플롯
    for circle in circles:
        circle.plot_points()

    # 그래프 표시
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Points in and out of the Circle')
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')  # 원의 형태가 왜곡되지 않도록 가로, 세로 축의 스케일을 동일하게 설정
    plt.show()