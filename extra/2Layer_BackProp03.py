import numpy as np
import matplotlib.pyplot as plt


def tanh(x):
    return np.tanh(x)


def tanh_derivative(x):
    return 1 - np.tanh(x) ** 2


W1 = np.array([[-0.2, 0.3, -0.4], [0.1, -0.3, -0.4]])
W2 = np.array([0.2, 0.3])


def go_forward(inp):
    sum = np.dot(W1, inp)
    out = np.array([tanh(x) for x in sum])

    sum = np.dot(W2, out)
    y = tanh(sum)
    return (y, out)


def train(epoch):
    global W2, W1
    lmd = 0.25  # шаг обучения
    N = 30  # число итераций при обучении
    count = len(epoch)

    # Списки для хранения весов после каждой эпохи
    W1_history = [W1.copy()]
    W2_history = [W2.copy()]

    for k in range(N):
        x = epoch[np.random.randint(0, count)]  # случайный выбор входного сигнала из обучающей выборки
        y, out = go_forward(x[0:3])  # прямой проход по НС и вычисление выходных значений нейронов
        e = y - x[-1]  # ошибка
        delta = e * tanh_derivative(y)  # локальный градиент
        W2[0] = W2[0] - lmd * delta * out[0]  # корректировка веса первой связи
        W2[1] = W2[1] - lmd * delta * out[1]  # корректировка веса второй связи

        delta2 = W2 * delta * tanh_derivative(out)  # вектор из 2-х величин локальных градиентов

        # корректировка связей первого слоя
        W1[0, :] = W1[0, :] - np.array(x[0:3]) * delta2[0] * lmd
        W1[1, :] = W1[1, :] - np.array(x[0:3]) * delta2[1] * lmd

        # Сохранение весов после каждой эпохи
        W1_history.append(W1.copy())
        W2_history.append(W2.copy())

    return W1_history, W2_history


# обучающая выборка (она же полная выборка)
epoch = [(-1, -1, -1, -1),
         (-1, -1, 1, 1),
         (-1, 1, -1, -1),
         (-1, 1, 1, 1),
         (1, -1, -1, -1),
         (1, -1, 1, 1),
         (1, 1, -1, -1),
         (1, 1, 1, 1)]

W1_history, W2_history = train(epoch)  # запуск обучения сети и получение истории весов

# проверка полученных результатов
for x in epoch:
    y, out = go_forward(x[0:3])
    print(f"Выходное значение НС: {y} => {x[-1]}")

# Построение графика весов по эпохам
epochs = range(len(W1_history))

# Для каждого веса из W1 (W1[0,0], W1[0,1], W1[0,2], W1[1,0], W1[1,1], W1[1,2])
for i in range(W1.shape[0]):
    for j in range(W1.shape[1]):
        weights = [W1_history[e][i, j] for e in epochs]
        plt.plot(epochs, weights, label=f'W1[{i},{j}]')

# Для каждого веса из W2 (W2[0], W2[1])
for j in range(W2.shape[0]):
    weights = [W2_history[e][j] for e in epochs]
    plt.plot(epochs, weights, label=f'W2[{j}]')

plt.xlabel('Эпоха')
plt.ylabel('Значение веса')
plt.title('Изменение весов нейронной сети по эпохам')
plt.legend()
plt.grid(True)
plt.show()
