import numpy as np
import matplotlib.pyplot as plt

def act(x):
    return 0 if x <= 0 else 1

C1 = [(1, 0), (0, 1)]
C2 = [(0, 0), (1, 1)]

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
    return y, sum_hidden, w_hidden

# Визуализация
fig, ax = plt.subplots(figsize=(10, 8))

# Отображение точек классов C1 и C2
C1_x = [p[0] for p in C1]
C1_y = [p[1] for p in C1]
C2_x = [p[0] for p in C2]
C2_y = [p[1] for p in C2]

ax.scatter(C1_x, C1_y, color='red', label='Class C1')
ax.scatter(C2_x, C2_y, color='blue', label='Class C2')

# Получение гиперплоскостей
_, sum_hidden1, w_hidden1 = go(C1[0])
_, sum_hidden2, w_hidden2 = go(C1[1])

# Определение границ для графика
x_vals = np.linspace(-0.5, 1.5, 400)

# Гиперплоскости
for i, (w, s) in enumerate(zip(w_hidden1, sum_hidden1)):
    y_vals = (-w[0] * x_vals - w[2]) / w[1]
    ax.plot(x_vals, y_vals, label=f'Hyperplane H1_{i+1}', linestyle='--')

for i, (w, s) in enumerate(zip(w_hidden2, sum_hidden2)):
    y_vals = (-w[0] * x_vals - w[2]) / w[1]
    ax.plot(x_vals, y_vals, label=f'Hyperplane H2_{i+1}', linestyle='-.')

# Настройки графика
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)
ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
ax.legend()
ax.set_title('Гиперплоскости и точки классов C1 и C2')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

plt.show()

# Проверка результатов
print(go(C1[0])[0], go(C1[1])[0])
print(go(C2[0])[0], go(C2[1])[0])
