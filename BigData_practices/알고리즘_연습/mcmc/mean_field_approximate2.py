import numpy as np
import matplotlib.pyplot as plt

def mean_field_solution(T, Tc ,Ms):
    return np.tanh(Tc / T)
    #return Ms*np.square(3)*(Tc/T)**(1.5)*np.square(Tc/T-1)
    #return Ms*np.square(Tc/T-1)

if __name__ == "__main__":
    # 임계 온도 및 포화 자화도 설정
    #KB=1.380649e-23
    Tc = 2.23  # 임의의 값
    Ms = 1  # 임의의 값

    # 온도 범위 설정
    temperature = np.linspace(0.1, 100, 200)

    # 각 온도에 대한 자화율 계산
    magnetization_values = mean_field_solution(temperature, Tc ,Ms)

    # 그래프 그리기
    plt.plot(temperature, magnetization_values)
    plt.xlabel('Temperature')
    plt.ylabel('Magnetization')
    plt.title('Mean Field Solution for Magnetization vs Temperature')
    plt.grid(True)
    plt.show()
