import numpy as np
import matplotlib.pyplot as plt

def act(x):
    return 0 if x < 0.5 else 1

def go(house, rock, attr):
    x123 = np.array([house, rock, attr])
    w11 = [0.3, 0.3, 0]
    w12 = [0.4, -0.5, 1]
    weight1 = np.array([w11, w12])  # матрица 2x3
    weight2 = np.array([-1, 1])     # вектор 1х2

    # Суммы на входах нейронов скрытого слоя
    sum_hidden = np.dot(weight1, x123)
    print("Значения сумм на нейронах 1-го скрытого слоя: " + str(sum_hidden))

    # Выходы нейронов скрытого слоя
    out_hidden = np.array([act(x) for x in sum_hidden])
    print("Значения на выходах нейронов 1-го скрытого слоя: " + str(out_hidden))

    # Суммы на входах нейронов выходного слоя
    sum_end = np.dot(weight2, out_hidden)
    print("Значения сумм на нейронах скрытого 2-го слоя: " + str(sum_end))

    # Выходное значение сети
    y = act(sum_end)
    print("Выходное значение НС: " + str(y))

    # Визуализация активации нейронов
    fig, axs = plt.subplots(2, figsize=(8, 6))

    # Визуализация скрытого слоя
    axs[0].bar(range(len(sum_hidden)), sum_hidden, color='blue', alpha=0.7)
    axs[0].set_xticks(range(len(sum_hidden)))
    axs[0].set_xticklabels([f'Neuron {i+1}' for i in range(len(sum_hidden))])
    axs[0].set_title('Активация нейронов 1-го скрытого слоя')
    axs[0].set_ylabel('Сумма входов')

    # Визуализация выходного слоя
    axs[1].bar([0], [sum_end], color='green', alpha=0.7)
    axs[1].set_xticks([0])
    axs[1].set_xticklabels(['Output Neuron'])
    axs[1].set_title('Активация нейрона выходного слоя')
    axs[1].set_ylabel('Сумма входов')

    plt.tight_layout()
    plt.show()

    return y

# Входное значение
house = 1
rock = 0
attr = 1

res = go(house, rock, attr)
if res == 1:
    print("Ты мне нравишься")
else:
    print("Созвонимся")