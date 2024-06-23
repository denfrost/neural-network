import numpy as np

def act(x):
    return 0 if x < 0.5 else 1

def go(house, rock, attr):
    x123 = np.array([house, rock, attr])
    w11 = [0.3, 0.3, 0]
    w12 = [0.4, -0.5, 1]
    weight1 = np.array([w11, w12])  # матрица 2x3
    weight2 = np.array([-1, 1])     # вектор 1х2

    sum_hidden = np.dot(weight1, x123)       # вычисляем сумму на входах нейронов скрытого слоя
    print("Значения сумм на нейронах 1-го скрытого слоя: "+str(sum_hidden))

    out_hidden = np.array([act(x123) for x123 in sum_hidden])
    print("Значения на выходах нейронов 1-го скрытого слоя: "+str(out_hidden))

    sum_end = np.dot(weight2, out_hidden)
    print("Значения сумм на нейронах скрытого 2-го слоя: " + str(sum_end))
    y = act(sum_end)
    print("Выходное значение НС: "+str(y))
    return y

#Входное значение
house = 0
rock = 1
attr = 1

res = go(house, rock, attr)
if res == 1:
    print("Ты мне нравишься")
else:
    print("Созвонимся")
