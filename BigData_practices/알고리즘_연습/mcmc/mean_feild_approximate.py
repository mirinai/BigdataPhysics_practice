import numpy as np
import matplotlib.pyplot as plt

def mean_field_solution(T, coordinate_num):
    Tc = coordinate_num / T
    magnetization = np.square(3) * (T / Tc) ** (3/2) * np.square(Tc / T - 1)
    return magnetization

if __name__ == "__main__":
    coordinate_num = 4  # 2D에서
    temperature = np.linspace(0.1, 5.0, 50)
    magnetization_values = []
    #외부 자기장 0
    for temp in temperature:
        magnetization_values.append(mean_field_solution(temp, coordinate_num))

    plt.plot(temperature, magnetization_values)
    plt.xlabel('Temperature')
    plt.ylabel('Magnetization')
    plt.title('Mean Field Solution for Magnetization vs Temperature')
    plt.grid(True)
    plt.show()
