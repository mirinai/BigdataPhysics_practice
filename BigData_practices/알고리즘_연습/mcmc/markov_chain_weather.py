import numpy as np

# 초기 분포(Initial Distribution)
pi_0 = np.array([0.5, 0.3, 0.2])#맑음, 흐림, 비

# 전이(transition) 확률 행렬
P = np.array([
    [0.8, 0.1, 0.1],
    [0.4, 0.4, 0.2],
    [0.2, 0.3, 0.5]
])

def predict_weather(pi_0, P, days):
    current_distribution = np.copy(pi_0)
    distributions = []
    for day in range(1, days+1):
        current_distribution = np.dot(current_distribution, P)#스칼라 곱
        distributions.append(current_distribution)
    return distributions

def weather_alarm(weathers):
    for i, weather_probs in enumerate(weathers):#index와 value를 리턴
        print("{}째 날 날씨 확률 : 맑음: {:.1f}%, 흐림: {:.1f}%, 비: {:.1f}%"
              .format(i+1,weather_probs[0]*100,weather_probs[1]*100,weather_probs[2]*100))
        #print(f"{i+1}일 날씨 확률 : 맑음: {weather_probs[0]:.3f}, 흐림: {weather_probs[1]:.3f}, 비: {weather_probs[2]:.3f}")
days = 7  # 7일 동안의 날씨 예측
distributions = predict_weather(pi_0, P, days)
weather_alarm(distributions)
'''
1째 날 날씨 확률 : 맑음: 56.0%, 흐림: 23.0%, 비: 21.0%
2째 날 날씨 확률 : 맑음: 58.2%, 흐림: 21.1%, 비: 20.7%
3째 날 날씨 확률 : 맑음: 59.1%, 흐림: 20.5%, 비: 20.4%
4째 날 날씨 확률 : 맑음: 59.6%, 흐림: 20.2%, 비: 20.2%
5째 날 날씨 확률 : 맑음: 59.8%, 흐림: 20.1%, 비: 20.1%
6째 날 날씨 확률 : 맑음: 59.9%, 흐림: 20.1%, 비: 20.1%
7째 날 날씨 확률 : 맑음: 59.9%, 흐림: 20.0%, 비: 20.0%
'''
