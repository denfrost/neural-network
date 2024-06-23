import numpy as np
import matplotlib.pyplot as plt

def act(x):
    return 0 if x <= 0 else 1

C1 = [(1,0), (0,1)]
C2 = [(0,0), (1,1)]

def go(C):
    x = np.array([C[0], C[1], 1])
    w1 = [1, 1, -1.5]
    w2 = [1, 1, -0.5]
    w_hidden = np.array([w1, w2])
    w_out = np.array([-1, 1, -0.5])

    sum_hidden = np.dot(w_hidden, x)
    out_hidden = [act(x) for x in sum_hidden]
    out_hidden.append(1)
    out_hidden = np.array(out_hidden)

    sum_output = np.dot(w_out, out_hidden)
    y = act(sum_output)

    print("Значения сумм на скрытых нейронах:", sum_hidden)
    print("Значения на выходах скрытых нейронов:", out_hidden)
    print("Сумма на выходном нейроне:", sum_output)
    print("Выходное значение НС:", y)

    # Визуализация сети
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(-1, 3)
    ax.set_ylim(-1, 4)

    # Позиции нейронов
    input_neurons = [(-0.5, 3), (-0.5, 2), (-0.5, 1)]
    hidden_neurons = [(1, 3), (1, 2), (1, 1)]
    output_neuron = [(2.5, 2)]

    # Отрисовка нейронов и меток
    for idx, (x_pos, y_pos) in enumerate(input_neurons):
        ax.add_patch(plt.Circle((x_pos, y_pos), 0.1, color='blue', ec='black', label='Input Neuron' if idx == 0 else ""))
        ax.text(x_pos - 0.4, y_pos, f'{x[idx]}', fontsize=12, va='center')

    for idx, (x_pos, y_pos) in enumerate(hidden_neurons):
        ax.add_patch(plt.Circle((x_pos, y_pos), 0.1, color='green', ec='black', label='Hidden Neuron' if idx == 0 else ""))
        ax.text(x_pos + 0.2, y_pos, f'\n{out_hidden[idx]}', fontsize=12, va='center', ha='center')

    for idx, (x_pos, y_pos) in enumerate(output_neuron):
        ax.add_patch(plt.Circle((x_pos, y_pos), 0.1, color='red', ec='black', label='Output Neuron' if idx == 0 else ""))
        ax.text(x_pos + 0.2, y_pos, f'{sum_output:.2f}\n{y}', fontsize=12, va='center', ha='center')

    # Отрисовка связей и их значений
    def draw_connection(ax, p1, p2, weight, activation):
        line_width = max(0.1, abs(weight))  # Толщина линии пропорциональна значению веса
        color = 'black' if activation == 1 else 'gray'
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], linewidth=line_width, color=color)
        mid_point = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
        ax.text(mid_point[0], mid_point[1], f'{weight:.2f}', fontsize=10, va='center', ha='center')

    # Соединения от входного слоя к скрытому
    for i in range(len(input_neurons)):
        draw_connection(ax, input_neurons[i], hidden_neurons[0], w_hidden[0][i], x[i])
        draw_connection(ax, input_neurons[i], hidden_neurons[1], w_hidden[1][i], x[i])

    # Соединения от скрытого слоя к выходному
    for i in range(len(hidden_neurons)):
        draw_connection(ax, hidden_neurons[i], output_neuron[0], w_out[i], out_hidden[i])

    # Настройки графика
    ax.set_aspect('equal')
    ax.axis('off')

    # Добавление легенды
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys(), loc='upper right')

    plt.show()

    return y

print(go(C1[0]), go(C1[1]))
print(go(C2[0]), go(C2[1]))
