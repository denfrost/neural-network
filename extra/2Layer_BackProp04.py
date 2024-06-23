import numpy as np

def tanh_derivative(x):
    return 1 - np.tanh(x)**2

# Примеры использования:
x1 = 2
print(f"Производная tanh({x1}) = {tanh_derivative(x1)}")

x2 = -1
print(f"Производная tanh({x2}) = {tanh_derivative(x2)}")

x3 = 0
print(f"Производная tanh({x3}) = {tanh_derivative(x3)}")

x4 = np.array([-2, -1, 0, 1, 2])
print(f"Производная tanh({x4}) = {tanh_derivative(x4)}")
