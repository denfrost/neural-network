import numpy as np
import matplotlib.pyplot as plt

def act(x):
    return 0 if x < 0.5 else 1

def go(house, rock, attr):
    x = np.array([house, rock, attr])
    w11 = [0.5, -0.5, 0.5]
    weight1 = np.array([w11])  # матрица 1x3

    # Сумма на входе нейрона скрытого слоя
    sum_hidden = np.dot(weight1, x)[0]
    y = act(sum_hidden)

    print("Значения сумм на нейроне единственного скрытого слоя: " + str(sum_hidden))
    print("Выходное значение НС: " + str(y))

    # Визуализация сети
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(-1, 3)
    ax.set_ylim(-1, 3)

    # Позиции нейронов
    input_params = [(-0.5, 2), (-0.5, 1), (-0.5, 0)]
    hidden_Perceptron = [(1, 1)]
    output_result = [(2.5, 1)]

    # Отрисовка нейронов и меток
    for idx, (x_pos, y_pos) in enumerate(input_params):
        ax.add_patch(plt.Circle((x_pos, y_pos), 0.1, color='blue', ec='black', label='Params' if idx == 0 else ""))
        ax.text(x_pos - 0.2, y_pos, f'{x[idx]}', fontsize=12, va='center')

    for idx, (x_pos, y_pos) in enumerate(hidden_Perceptron):
        ax.add_patch(plt.Circle((x_pos, y_pos), 0.1, color='green', ec='black', label='Hidden Neuron' if idx == 0 else ""))
        ax.text(x_pos + 0.2, y_pos, f'{sum_hidden:.2f}\n{act(sum_hidden)}', fontsize=12, va='center', ha='center')

    for idx, (x_pos, y_pos) in enumerate(output_result):
        ax.add_patch(plt.Circle((x_pos, y_pos), 0.1, color='red', ec='black', label='Result' if idx == 0 else ""))
        ax.text(x_pos + 0.2, y_pos, f'{y}', fontsize=12, va='center', ha='center')

    # Отрисовка связей и их значений
    def draw_connection(ax, p1, p2, weight, activation):
        line_width = max(0.1, abs(weight))  # Толщина линии пропорциональна значению веса
        color = 'black' if activation == 1 else 'gray'
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], linewidth=line_width, color=color)
        mid_point = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
        ax.text(mid_point[0], mid_point[1], f'{weight:.2f}', fontsize=10, va='center', ha='center')

    # Соединения от входного слоя к скрытому
    for i in range(len(input_params)):
        draw_connection(ax, input_params[i], hidden_Perceptron[0], weight1[0][i], x[i])

    # Соединения от скрытого слоя к выходному
    draw_connection(ax, hidden_Perceptron[0], output_result[0], 1, act(sum_hidden))

    # Настройки графика
    ax.set_aspect('equal')
    ax.axis('off')

    # Добавление легенды
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys(), loc='upper right')

    plt.show()

    return y

# Входное значение
house = 1
rock = 1
attr = 1

# Инференс
res = go(house, rock, attr)
if res == 1:
    print("Ты мне нравишься")
else:
    print("Созвонимся")
