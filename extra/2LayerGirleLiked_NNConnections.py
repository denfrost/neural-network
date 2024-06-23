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
    out_hidden = np.array([act(x) for x in sum_hidden])

    # Суммы на входах нейронов выходного слоя
    sum_end = np.dot(weight2, out_hidden)
    y = act(sum_end)

    # Визуализация сети
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(-1, 3)
    ax.set_ylim(-1, 3)

    # Позиции нейронов
    input_neurons = [(-0.5, 2), (-0.5, 1), (-0.5, 0)]
    hidden_neurons = [(1, 1.5), (1, 0.5)]
    output_neuron = [(2.5, 1)]

    # Отрисовка нейронов и меток
    for idx, (x, y) in enumerate(input_neurons):
        ax.add_patch(plt.Circle((x, y), 0.1, color='blue', ec='black'))
        ax.text(x - 0.2, y, f'{x123[idx]}', fontsize=12, va='center')
    for idx, (x, y) in enumerate(hidden_neurons):
        ax.add_patch(plt.Circle((x, y), 0.1, color='green', ec='black'))
        ax.text(x + 0.2, y, f'{sum_hidden[idx]:.2f}\n{out_hidden[idx]}', fontsize=12, va='center', ha='center')
    for idx, (x, y) in enumerate(output_neuron):
        ax.add_patch(plt.Circle((x, y), 0.1, color='red', ec='black'))
        ax.text(x + 0.2, y, f'{sum_end:.2f}\n{y}', fontsize=12, va='center', ha='center')

    # Отрисовка связей и их значений
    def draw_connection(ax, p1, p2, weight, act, idx):
        line_width = max(0.1, abs(weight))  # Толщина линии пропорциональна значению веса
        color = 'black' if act == 1 else 'gray'
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], linewidth=line_width, color=color)
        mid_point = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
        ax.text(mid_point[0], mid_point[1], f'{weight:.2f}', fontsize=10, va='center', ha='center')

    # Соединения от входного слоя к скрытому
    for i in range(len(input_neurons)):
        for j in range(len(hidden_neurons)):
            draw_connection(ax, input_neurons[i], hidden_neurons[j], weight1[j][i], act(x123[i]), i)

    # Соединения от скрытого слоя к выходному
    for i in range(len(hidden_neurons)):
        draw_connection(ax, hidden_neurons[i], output_neuron[0], weight2[i], out_hidden[i], i + len(input_neurons))

    # Настройки графика
    ax.set_aspect('equal')
    ax.axis('off')
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
