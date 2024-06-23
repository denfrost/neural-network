import numpy as np

def act(x):
    return 0 if x < 0.5 else 1

def go(house, rock, attr):
    x = np.array([house, rock, attr])
    w11 = [0.5, -0.5, 0.5]
    weight1 = np.array([w11])  # матрица 2x3

    sum_hidden = np.dot(weight1, x)       # вычисляем сумму на входах нейронов скрытого слоя
    print("Значения сумм на нейроне единственного скрытого слоя: "+str(sum_hidden))

    y = act(sum_hidden)
    print("Выходное значение НС: "+str(y))

    return y

#Входное значение
house = 1
rock = 1
attr = 1

#Inference
res = go(house, rock, attr)
if res == 1:
    print("Ты мне нравишься")
else:
    print("Созвонимся")
