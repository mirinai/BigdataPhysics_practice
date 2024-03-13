import random

def piEstimated(num_points, L):
    pointsInCircle = 0
    total_points = num_points

    for _ in range(num_points):
        x = random.uniform(0, L)
        y = random.uniform(0, L)

        if x ** 2 + y ** 2 <= L * L:
            pointsInCircle += 1

    estimated_pi = 4 * pointsInCircle / total_points#1/4의 넓이 만 구해서 4를 곱한다
    return estimated_pi

L = 3
num_points = 1000000
estimated_pi = piEstimated(num_points, L)
print("Estimated Pi:", estimated_pi)#Estimated Pi: 3.143844
