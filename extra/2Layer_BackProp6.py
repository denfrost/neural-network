import numpy as np
import matplotlib.pyplot as plt

# Функция ReLU
def step_function(x):
    return np.where(x < 0, 0, 1) #x*(x > 0) #1 if x >= 0 else 0

def leaky_relu(x):
    alpha=0.1
    return np.where(x > 0, x, alpha*x) #x*(x > 0) #1 if x >= 0 else 0

def relu(x):
    return np.maximum(x,0)

# Генерация данных для построения графика
x = np.linspace(-5, 5, 100)  # создаем массив x от -5 до 5
y = step_function(x)  # вычисляем значения ReLU для каждого значения x

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='ReLU', color='b', linewidth=2)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # горизонтальная линия y=0
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # вертикальная линия x=0
plt.title('ReLU Function')
plt.xlabel('x')
plt.ylabel('ReLU(x)')
plt.legend()
plt.grid(True)
plt.show()
